import firebase_admin
import random
import smtplib
import ssl
from email.message import EmailMessage
from firebase_admin import db, credentials

app_password = "iktq ghqx nzhv tyar"
email_sender = "neverbackdownneverwhatteyvat@gmail.com"

class Database:
    def __init__(self):
        cred = credentials.Certificate("resources/credentials.json")
        firebase_admin.initialize_app(cred, {"databaseURL" : "https://morax-shared-financial-manager-default-rtdb.asia-southeast1.firebasedatabase.app/"})
        self.update_refs()
    
    def update_refs(self):
        ref = db.reference("/")
        self.dictionary = dict(ref.get())
    
    def query_login(self, email: str, password: str):
        users = self.dictionary["Users"]
        email = email.replace('.', ',')
        if email in users and users[email]['Password'] == password:
            return "Found"
        elif email in users and users[email]['Password'] != password:
            return "Wrong Password"
        
        return "Not found"
    
    def get_username_of_email(self, email: str):
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
            db.reference(f"/Users/").update({email : { "Username" : username, "Password": password}})
            return "Successful"
        
        return "Account already exists."
    
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
        groups = dict()
        for group in self.dictionary["Groups"]:
            for member in self.dictionary['Groups'][group]["Members"]:
                if email.replace('.', ',') in self.dictionary['Groups'][group]['Members'][member]:
                    groups[group] = self.dictionary['Groups'][group]
        
        return groups
    
    def is_group_existing(self, group_code: str):
        for group in self.dictionary['Groups']:
            if self.dictionary['Groups'][group]['Unique code'] == group_code:
                return True
            
        return False
    
    def get_members(self, group: str):
        if not group in self.dictionary['Groups']:
            return "Group doesn't exist."
        
        return self.dictionary['Groups'][group]["Members"]
    
    def get_transactions(self, group: str):
        if not group in self.dictionary['Groups']:
            return "Group doesn't exist."
        
        transactions = self.dictionary['Groups'][group]["Transactions"]
        return transactions