import firebase_admin
import random
import string
import smtplib
import ssl
import io
import base64

from resources.secrets import app_password as ap
from resources.secrets import email_sender as es

from email.message import EmailMessage
from firebase_admin import db, credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
from googleapiclient.errors import HttpError
from PIL import Image

app_password = ap
email_sender = es

class Database:
    def __init__(self):
        cred = credentials.Certificate("resources/credentials.json")
        firebase_admin.initialize_app(cred, {"databaseURL" : "https://morax-shared-financial-manager-default-rtdb.asia-southeast1.firebasedatabase.app/"})
        scope = ['https://www.googleapis.com/auth/drive']
        drive_credentials = service_account.Credentials.from_service_account_file(filename="resources/credentials.json", scopes=scope)
        self.service = build('drive', 'v3', credentials=drive_credentials)
        self.update_refs()
    
    def update_refs(self):
        ref = db.reference("/")
        self.dictionary = dict(ref.get())
        results = self.service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, mimeType)", q='name contains "de"').execute()
        self.drive_files = results.get('files', [])
    
    def query_login(self, email: str, password: str):
        users = self.dictionary["Users"]
        email = email.replace('.', ',')
        if email in users and users[email]['Password'] == password:
            return "Found"
        elif email in users and users[email]['Password'] != password:
            return "Wrong Password"
        
        return "Not found"
    
    def get_username_of_email(self, email: str):
        self.update_refs()
        users = self.dictionary["Users"]
        email = email.replace('.', ',')
        if email in users:
            return users[email]["Username"]
        
        return "No username exists for this email."
    
    def change_password(self, email: str, new_password: str):
        users = self.dictionary["Users"]
        email = email.replace('.', ',')
        if email in users:
            db.reference(f"/Users/{email}/").update({"Password": new_password})
            return "Password Changed"
        
        return "Account doesn't exist."
    
    def create_account(self, email: str, username: str, password: str):
        email = email.replace('.', ',')
        if email not in self.dictionary["Users"]:
            db.reference(f"/Users/").update({email : { "Username" : username, "Password": password, "Picture Link": "", "First Run": True, "GCash": "", "QR Image id": ""}})
            return "Successful"
        
        return "Account already exists."

    def get_first_run(self, email: str):
        self.update_refs()
        email = email.replace('.', ',')
        return self.dictionary["Users"][email]["First Run"]
    
    def confirm_first_run(self, email: str):
        email = email.replace('.', ',')
        db.reference(f"/Users/{email}/").update({"First Run": False})
    
    def create_group_with_email(self, group_name: str, group_description: str, email: str):
        username = self.get_username_of_email(email)
        unique_code = self.generate_unique_code()
        email = email.replace('.', ',')
        if email in self.dictionary["Users"]:
            db.reference(f"/Groups/").update({group_name : {"Members" : {username : email}, "Transactions": "", "Unique code" : unique_code, "Description": group_description, "Created by": username}})
            
            return "Successful"
        
        return "Cannot create group."
    
    def join_group_with_email(self, unique_code: str, email: str):
        username = self.get_username_of_email(email)
        email = email.replace('.', ',')
        
        group_name = self.get_group_by_code(unique_code)
        
        if email in self.dictionary["Users"]:
            db.reference(f"/Groups/{group_name}/Members").update({username: email})
            
            return "Successful"
        
        return "Cannot create group."
    
    def confirm_email_ownership(self, email):
        code = random.randrange(100000, 999999)
        subject = "Do you want to reset your password with Morax? "
        body = f"""
Someone is trying to change your password within the Morax Application.

If this is you, enter the following code on the app prompt:

    {code}

Ignore this message if not.
        """

        email_message = EmailMessage()
        email_message["From"] = email_sender
        email_message["To"] = email
        email_message["Subject"] = subject
        email_message.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, app_password)
            smtp.sendmail(email_sender, email, email_message.as_string())

        return code
    
    def get_groups_for_email(self, email: str):
        self.update_refs()
        groups = dict()
        for group in self.dictionary["Groups"]:
            for member in self.dictionary['Groups'][group]["Members"]:
                if email.replace('.', ',') in self.dictionary['Groups'][group]['Members'][member]:
                    groups[group] = self.dictionary['Groups'][group]
        
        return groups
    
    def get_group_by_code(self, code: str):
        self.update_refs()
        groups = self.dictionary["Groups"]
        for group in groups:
            if self.dictionary['Groups'][group]['Unique code'] == code:
                return str(group)
            
        return "Unsuccessful"
    
    def is_group_existing(self, group_code: str):
        self.update_refs()
        for group in self.dictionary['Groups']:
            if self.dictionary['Groups'][group]['Unique code'] == group_code:
                return True
            
        return False
    
    def get_members(self, group: str):
        self.update_refs()
        if not group in self.dictionary['Groups']:
            return "Group doesn't exist."
        
        return self.dictionary['Groups'][group]["Members"]
    
    def get_transactions(self, group: str) -> dict:
        self.update_refs()
        if not group in self.dictionary['Groups']:
            return "Group doesn't exist."
        
        transactions = self.dictionary['Groups'][group]["Transactions"]
        return transactions
    
    def generate_unique_code(self):
        res = ''.join(random.choices(
            string.ascii_letters +
            string.digits
            , k=8))
        
        return str(res)
    
    def get_code_by_group_name(self, group_name: str):
        self.update_refs()
        groups = self.dictionary["Groups"]
        for group in groups:
            if self.dictionary['Groups'][group] == group_name:
                return self.dictionary['Groups'][group]['Unique code']
            
        return "Unsuccessful"
    
    def get_picture_id_by_group_name(self, group_name: str):
        self.update_refs()
        groups = self.dictionary["Groups"]
        for group in groups:
            if group == group_name:
                return self.dictionary['Groups'][group]['Picture id']
            
        return "Unsuccessful"
    
    def get_group_image(self, group_name: str):
        picture_id = self.get_picture_id_by_group_name(group_name)
        base64_content = ""
        try:
            request_file = self.service.files().get_media(fileId = picture_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
        except HttpError as error:
            print(F'An error occurred: {error}')
            return ""
        
        return base64_content
    
    def get_group_description(self, group_name: str):
        self.update_refs()
        groups = self.dictionary["Groups"]
        for group in groups:
            if group == group_name:
                return self.dictionary['Groups'][group]['Description']
        
        return "Unsuccessful"
    
    def get_group_creator(self, group_name: str):
        self.update_refs()
        groups = self.dictionary["Groups"]
        for group in groups:
            if group == group_name:
                return self.dictionary['Groups'][group]['Created by']
        
        return "Unsuccessful"
    
    def get_user_image(self, email: str):
        email = email.replace('.', ',')
        picture_id = self.dictionary['Users'][email]['Picture Link']
        base64_content = ""
        try:
            request_file = self.service.files().get_media(fileId = picture_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
        except HttpError as error:
            print(F'An error occurred: {error}')
            return ""
        
        return base64_content
    
    def get_user_images(self):
        images = dict()
        for user in self.dictionary["Users"]:
            images.update({user: self.get_user_image(user)})
            
        return images

    def get_gcash_credentials(self):
        gcash_infos = dict()
        for user in self.dictionary['Users']:
            gcash_qr_id = self.dictionary['Users'][user]['QR Image id']
            gcash_number = self.dictionary['Users'][user]['GCash']

            base64_content = ""
            try:
                request_file = self.service.files().get_media(fileId = gcash_qr_id)
                file = io.BytesIO()
                downloader = MediaIoBaseDownload(file, request_file)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                
                base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
            except HttpError as error:
                print(F'An error occurred: {error}')
                return ""

            gcash_infos.update({user : {"QR Image" : base64_content, "GCash number": gcash_number}})
        
        return gcash_infos
    
    def get_gcash_of_user(self, email: str):
        email = email.replace(".", ",")
        gcash_qr_id = self.dictionary['Users'][email]['QR Image id']
        gcash_number = self.dictionary['Users'][email]['GCash']

        base64_content = ""
        try:
            request_file = self.service.files().get_media(fileId = gcash_qr_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
        except HttpError as error:
            print(F'An error occurred: {error}')
            return ""

        return base64_content, gcash_number
    
    def get_item_picture_by_item_name(self, item_name, group_name):
        self.update_refs()
        return self.dictionary['Groups'][group_name]["Transactions"][item_name]["Image id"]
    
    def change_username(self, email: str, replacement: str):
        email = email.replace('.', ',')
        db.reference(f"/Users/{email}/").update({"Username": replacement})

    def get_item_image(self, item_name: str, group_name: str):
        picture_id = self.get_item_picture_by_item_name(item_name, group_name)
        
        if picture_id == "":
            return ""
        
        base64_content = ""
        try:
            request_file = self.service.files().get_media(fileId = picture_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
        except HttpError as error:
            print(F'An error occurred: {error}')
            return ""
        
        return base64_content

    def get_group_images_for_email(self, email: str):
        images = dict()
        groups = self.get_groups_for_email(email)
        for group in groups:
            image = self.get_group_image(group)
            images[group] = image
        
        return images
    
    def get_item_images_for_group(self, group_name: str):
        images = dict()
        items = self.get_transactions(group_name)
        for item in items:
            image = self.get_item_image(item, group_name)
            images[item] = image
        
        return images
    
    def upload_group_image(self, group_name: str, file: str):
        image_bytes = io.BytesIO()
        image = Image.open(file).convert("RGBA")
        image = image.resize((200, 200))
        image.save(image_bytes, format="PNG")
        
        try:
            media = MediaIoBaseUpload(image_bytes, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': f"{group_name}.png"}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')
            db.reference(f"/Groups/{group_name}").update({"Picture id": id})

            permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email_sender
            }
            self.service.permissions().create(fileId=id, body=permission).execute()
            
        except HttpError as error:
            print(f'An error occurred: {error}')
    
    def upload_item_image(self, group_name: str, item_name: str, file: str):
        image_bytes = io.BytesIO()
        image = Image.open(file).convert("RGBA")
        image = image.resize((200, 200))
        image.save(image_bytes, format="PNG")
        
        try:
            media = MediaIoBaseUpload(image_bytes, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': f"{group_name}|{item_name}.png"}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')
            db.reference(f"/Groups/{group_name}/Transactions/{item_name}").update({"Image id": id})

            permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email_sender
            }
            self.service.permissions().create(fileId=id, body=permission).execute()
            
        except HttpError as error:
            print(f'An error occurred: {error}')
    
    def upload_user_qr_number(self, email: str, qr_bytes: io.BytesIO, number: str):
        email = email.replace(".", ",")

        try:
            media = MediaIoBaseUpload(qr_bytes, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': f"{email}|QRCODE.png"}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')
            db.reference(f"/Users/{email}/").update({"QR Image id": id, "GCash": number})

            permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email_sender
            }
            self.service.permissions().create(fileId=id, body=permission).execute()
            
        except HttpError as error:
            print(f'An error occurred: {error}')
    
    def update_user_image(self, email: str, user_image_buffer: io.BytesIO):
        email = email.replace('.', ',')
        try:
            media = MediaIoBaseUpload(user_image_buffer, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': f"{email}|USERIMAGE.png"}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')
            db.reference(f"/Users/{email}/").update({"Picture Link": id})

            permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email_sender
            }
            self.service.permissions().create(fileId=id, body=permission).execute()
            
        except HttpError as error:
            print(f'An error occurred: {error}')
    
    def mark_paid_with_proof(self, group_name: str, item_name: str, email: str, image_path: str):
        if image_path == "":
            return ""
        
        email = email.replace('.', ',')
        image_bytes = io.BytesIO()
        image = Image.open(image_path).convert("RGBA")
        image = image.resize((200, 200))
        image.save(image_bytes, format="PNG")
        
        try:
            media = MediaIoBaseUpload(image_bytes, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': f"PROOF|{group_name}|{item_name}.png"}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')
            db.reference(f"/Groups/{group_name}/Transactions/{item_name}/Paid by").update({ email : id})

            permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email_sender
            }
            self.service.permissions().create(fileId=id, body=permission).execute()
            
            return "Successful"
        
        except HttpError as error:
            print(f'An error occurred: {error}')
            return ""
    
    def get_image_proof(self, picture_id: str):
        self.update_refs()
        
        if picture_id == "":
            return ""
        
        try:
            request_file = self.service.files().get_media(fileId = picture_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            return file
        except HttpError as error:
            print(F'An error occurred: {error}')
            return ""
    
    def create_receivable(self, email: str, group_name: str, item_name: str, item_date: str, item_amount: str, item_description: str):
        email = email.replace('.', ',')
        if group_name in self.dictionary["Groups"]:
            db.reference(f"/Groups/{group_name}/Transactions").update({item_name : { "Description" : item_description, "Price": item_amount, "Posted by": {"Email": email}, "Time created": item_date, "Image id": "", "Paid by": ""}})
            return "Successful"
        
        return "Cannot add item"
    
    def complete_transaction(self, group_name: str, item_name: str):
        if group_name in self.dictionary["Groups"]:
            db.reference(f"/Groups/{group_name}/Transactions/{item_name}").delete()
    
    def get_usernames(self):
        self.update_refs()
        usernames = dict()
        for user in self.dictionary["Users"]:
            usernames.update({self.dictionary["Users"][user]["Username"] : user})
            
        return usernames