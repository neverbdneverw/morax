import gspread
from oauth2client.service_account import ServiceAccountCredentials
from email.message import EmailMessage
import random
import ssl
import smtplib

app_password = "iktq ghqx nzhv tyar"
email_sender = "neverbackdownneverwhatteyvat@gmail.com"

class DataRetriever(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataRetriever, cls).__new__(cls)
            
        cls.__init__(cls)
        
        return cls
    
    def __init__(self):
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", 'https://mail.google.com/']

        credentials = ServiceAccountCredentials.from_json_keyfile_name("./src/backend/credentials.json", scope)
        client = gspread.authorize(credentials)

        self.secrets_sheet = client.open("Secrets").sheet1
        
    def is_account_found(self, email: str, password: str):
        accounts = self.secrets_sheet.get_all_values()
        
        for account in accounts:
            if email.strip() == account[0] and password.strip() == account[2]:
                return True
            elif email.strip() == account[0] and password.strip() != account[2]:
                forgot_password = input("Password might be incorrect. Forgot it? y/n ")
                if forgot_password.lower() == "y":
                    self.forgot_password(self, email)
                    return True
            
        print("\nEmail/Username/Password might be incorrect.\n")
        return False
    
    def create_account(self, email, username, password):
        new_line = len(self.secrets_sheet.get_all_values()) + 1
        self.secrets_sheet.update(f"A{new_line}:C{new_line}", [[email, username, password]])
    
    def forgot_password(self, email: str):
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
        
        print("Wait for the code sent through your email.\nIf you have not receive it, check your spam folder.")
        
        received_code = input("What is the code you received in your email? ")
        
        if int(received_code) == code:
            new_password = input("Enter a new password: ")
            confirm = input("Confirm your new password: ")
            
            if confirm != new_password:
                print("Make sure the passwords are the same!")
                return
            
            for index, account in enumerate(self.secrets_sheet.get_all_values()):
                 if email.strip() == account[0]:
                     final_index = index + 1
                     self.secrets_sheet.update(f"C{final_index}", new_password)