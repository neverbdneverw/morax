from google.oauth2 import service_account
from email.message import EmailMessage
import gspread
import random
import ssl
import smtplib

app_password = "iktq ghqx nzhv tyar"
email_sender = "neverbackdownneverwhatteyvat@gmail.com"
SERVICE_ACCOUNT_INFO = {
   "type": "service_account",
   "project_id": "morax-shared-financial-manager",
   "private_key_id": "f3e6a038ece746f4c99b5a8226e28f10286d4635",
   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDijt8kt2zpYr8X\nLXnhNIxUk2fxL4KN2EYymszLiC3rP4ijrk43p/QvAP6MF6M+JTox+mpsOoEtvlvu\naYgsApVAIv0Jgr9ydSCu0GhYrX0FO2LU+LpdvikL8UeyIpc326A3dROSWqCZmrdq\nv2E5HzKgKwF9eEHxhF8xvDS1cUaonSCI/BWpg/ADvSJIHt0Dxa6y0idpVg4qD9x5\nHh0EJIPhm0FeZ/PrQ8a6QQUXkf1wTHYhZ9R8Z/VWly/xQGZAW1K6z53EjA/27C3I\nyAUnx7gq3aIPF+oGODMEto1o+agvGT4XHkaoYpQQQw93aGx1OPhEJPNfyUTvKFWk\ny2d9Saz5AgMBAAECggEAEQxGL0mcKO20ymYyIyeknaKf8i6siMbq9VjfqzsalXao\n7gQqP5bkUXsmLF2E+6Kqf+NDidRXLx2BZm3LgOBK4dIgL0yG4nJ83JqzF2UqoK+o\nzrTOtUofZZYo2ncu4NWmdzXYnK00I4rYXXB8POOjmBjUWmAnuihHT4NFhhe5hOt1\no2fcKIEDbMbbD66w8XkhnTQYhQSY8u3jj1j92XYmi5d5i8gKXkg7yfz1WzEyAaWI\nMBayqbiBOeiKxsXz3n4eOmczlfnzzVR2f78aYODoIyaATp5/g2BpGs6LD7Cxe62Z\nDojNbYhmxXb6+CZ7v/6zUhKm/at1KL6rh4V2pZtMAQKBgQD8w+46gq0Vak8Prl5L\nQcpJYDFf22kn9PrQlJzv8wpVQOZ7pJOVm0Uu8GXj6tJWq2wx1G+5pCeg8+FYxbvC\nQZY3sHpStLmPEH1JICp1i2fkwB3PP1uHLaMVS0d5NyjT8lTXarA484vjeg9QR7h5\n9h12aFZ4XYWhuSgh4d2AQKdZ+QKBgQDldRXE6jK25TSq1AJphJ5/BwIt5DIZPBKb\ncNFeW+FdcGbYtkuMeIGCXRbV5VDwxtIaiCdiBOmCzHcl7ciprqvxdVoLLQU0z0Rc\nYYSPK6kLtjHtLRURyxBGv7UdKcGcLhJ2mnnW3uvn2mZ+UQRIOpz7u10NH0Jf5cfq\njoZ8yhGrAQKBgA4G/ZCHsf1PQgX3wkng484ApZzRO1u5T7YFmVQDo94pVOElt/8E\nd+lr8+ubG4MtzjpRtMWTo5NeFXJsvsfABgsfIxq15tpWqu1E+LY/P0vFkaHvvS+a\nS8OhwtyqP/zLJQQzaoYulePQ4UquQEGcc/QfRDU303OvJ9gBhd5ZODBZAoGBAKK8\nN4RA1VcBmCjP1CYh+Ib+4XzKqv1arZewm8zgPSWX4lkwcMRfcvqSKu/og09AsyI+\nDjBma3ZorNgpnHc7epb1M7dZZqfdmA4s22bvACVeQmqD3r2P1ytWK41TYAz0YAPd\n6yuJTqZRLv/HVdIkP9IJQCVeViTNQswH6Tn31jABAoGAXWPOOuenkqAGvrZQWLFK\na3aFAabIlvr1rElm050Ri1yZQTRGt75cHxr2BN35ZQgybeY5PQ7cFlQiXKdmongd\n/k3mgzjwncXFrtaABj7wPZuWfLTFY3qXa+Q+o7Mb0URLJaehKEOB+DgCU/Wsb3fU\nQ2PbSpQUiE94cdXbMU/kp1k=\n-----END PRIVATE KEY-----\n",
   "client_email": "neverbackdownneverwhat@morax-shared-financial-manager.iam.gserviceaccount.com",
   "client_id": "109262128144736006250",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/neverbackdownneverwhat%40morax-shared-financial-manager.iam.gserviceaccount.com",
   "universe_domain": "googleapis.com"
}

class DataRetriever():
    def __init__(self):
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

        credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO, scopes=scope)
        client = gspread.authorize(credentials)

        self.secrets_sheet = client.open("Secrets").sheet1
        
    def is_account_found(self, email: str, password: str):
        accounts = self.secrets_sheet.get_all_values()
        
        for account in accounts:
            if email.strip() == account[0] and password.strip() == account[2]:
                return "Found"
            elif email.strip() == account[0] and password.strip() != account[2]:
                return "Wrong password"
            
        print("\nEmail/Username/Password might be incorrect.\n")
        return "Not found"
    
    def is_email_existing(self, email: str):
        accounts = self.secrets_sheet.get_all_values()
        
        for account in accounts:
            if email.strip() == account[0]:
                return True
        
        return False
    
    def create_account(self, email, username, password):
        if self.is_email_existing(email):
            return "Account already exists."

        new_line = len(self.secrets_sheet.get_all_values()) + 1
        self.secrets_sheet.update(f"A{new_line}:C{new_line}", [[email, username, password]])
        return "Account created."

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
    
    def forgot_password(self, email: str, new_password: str):
        for index, account in enumerate(self.secrets_sheet.get_all_values()):
             if email.strip() == account[0]:
                 final_index = index + 1
                 self.secrets_sheet.update(f"C{final_index}", new_password)