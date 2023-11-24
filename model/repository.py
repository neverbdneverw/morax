import firebase_admin
import random
import string
import smtplib
import ssl
import io

from resources import app_password, email_sender

from email.message import EmailMessage
from firebase_admin import db, credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
from googleapiclient.errors import HttpError

from . import User, Group, Member, Transaction

from typing import List

class Repository:
    users: List[User] = []
    groups: List[Group] = []
    def __init__(self):
        cred = credentials.Certificate("resources/credentials.json")
        firebase_admin.initialize_app(cred, {"databaseURL" : "https://morax-shared-financial-manager-default-rtdb.asia-southeast1.firebasedatabase.app/"})
        scope = ['https://www.googleapis.com/auth/drive']
        drive_credentials = service_account.Credentials.from_service_account_file(filename="resources/credentials.json", scopes=scope)
        self.service = build('drive', 'v3', credentials=drive_credentials)
        self.update_refs()
        
        self.load_users()
        self.load_groups()
    
    def update_refs(self):
        ref = db.reference("/")
        self.dictionary = dict(ref.get())
        results = self.service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, mimeType)", q='name contains "de"').execute()
        self.drive_files = results.get('files', [])
    
    def update_repo(function):
        def wrapper(*args):
            function(args)
            this: Repository = args[0]
            this.update_refs()
        return wrapper
        
    def load_users(self):
        self.users = []
        repo_users = self.dictionary["Users"]
        
        for user in repo_users:
            self.users.append(
                User(
                    user,
                    repo_users[user]['First Run'],
                    repo_users[user]['GCash'],
                    repo_users[user]['Password'],
                    repo_users[user]['Picture Link'],
                    repo_users[user]['QR Image id'],
                    repo_users[user]['Username']
                )
            )
    
    def load_groups(self):
        self.groups = []
        repo_groups = self.dictionary["Groups"]
        
        for group in repo_groups:
            created_by = repo_groups[group]['Created by']
            description = repo_groups[group]['Description']
            members = [Member(member[0], member[1]) for member in dict(repo_groups[group]['Members']).items()]
            picture_id = repo_groups[group]['Picture id']
            unique_code = repo_groups[group]['Unique code']
            
            transactions = []
            
            transactions_dict = repo_groups[group]['Transactions']
            
            if transactions_dict != "None":
                for transaction in transactions_dict:
                    transaction_name = transaction
                    transaction_description = transactions_dict[transaction]['Description']
                    transaction_image_id = transactions_dict[transaction]['Image id']
                    transaction_price = transactions_dict[transaction]['Price']
                    transaction_time_created = transactions_dict[transaction]['Time created']
                    transaction_paid_by = list(dict(transactions_dict[transaction]['Paid by']).items())
                    
                    transaction_posted_by = ""
                    for user in self.users:
                        if user.email == transactions_dict[transaction]['Posted by']["Email"]:
                            transaction_posted_by = user.email
                    
                    transactions.append(
                        Transaction(
                            transaction_name,
                            transaction_description,
                            transaction_image_id,
                            transaction_paid_by,
                            transaction_posted_by,
                            transaction_price,
                            transaction_time_created
                        )
                    )
            
            self.groups.append(
                Group(
                    group,
                    created_by,
                    description,
                    members,
                    picture_id,
                    unique_code,
                    transactions
                )
            )
    
    def update_group(self, group: Group):
        members = dict()
        transactions = dict()
        
        member: Member = None
        for member in group.members:
            members.update({member.username : member.email})
            
        transaction: Transaction = None
        for transaction in group.transactions:
            paid_users = dict()
            
            paid_user: tuple = None
            for paid_user in transaction.paid_by:
                paid_users.update({paid_user[0] : paid_user[1]})
            
            transactions.update({
                transaction.name : {
                    "Description" : transaction.description,
                    "Image id" : transaction.image_id,
                    "Price" : transaction.price,
                    "Time created": transaction.time_created,
                    "Paid by": paid_users,
                    "Posted by": { "Email" : transaction.posted_by },
                }
            })
        
        if len(transactions.items()) == 0:
            transactions = "None"
        
        db.reference('/Groups/').update({
            group.group_name: {
                "Created by": group.created_by,
                "Description": group.description,
                "Picture id": group.picture_id,
                "Unique code": group.unique_code,
                "Members": members,
                "Transactions": transactions
            }
        })
        
        self.update_refs()
    
    def update_user(self, user: User):
        db.reference('/Users/').update({
            user.email: {
                "First Run": user.first_run,
                "GCash": user.gcash_number,
                "Password": user.password,
                "Picture Link": user.picture_link,
                "QR Image id": user.qr_image_id,
                "Username": user.username
            }
        })
        
        self.update_refs()
    
    def upload_image(self, file_name: str, buffer: io.BytesIO) -> str:
        try:
            media = MediaIoBaseUpload(buffer, mimetype='image/png')
            uploaded_file = self.service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()
            id = uploaded_file.get('id')

            return id
            
        except HttpError as error:
            print(f'An error occurred: {error}')
            
            return
    
    def download_image(self, image_id: str) -> io.BytesIO:
        if image_id == "":
            return
        
        try:
            request_file = self.service.files().get_media(fileId = image_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            return file
        except HttpError as error:
            print(F'An error occurred: {error}')
            return
    
    def delete_transaction(self, group_name: str, transaction: Transaction):
        db.reference(f"/Groups/{group_name}/Transactions/{transaction.name}").delete()
    
    def get_email_confirmation_code(self, email):
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

    def generate_unique_code(self):
        res = ''.join(random.choices(
            string.ascii_letters +
            string.digits
            , k=8))
        
        return str(res)