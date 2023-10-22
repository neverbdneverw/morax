from DataRetriever import DataRetriever
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    singleton = DataRetriever()
    account = input("What email do you use to login? ")
    password = input("Enter a password: ")
    
    account_found = singleton.is_account_found(singleton, account, password)
    
    if account_found == "Found":
        print("Login successful!")
    elif account_found == "Wrong password":
        forgot_password = input("Password might be incorrect. Forgot it? y/n ")
        if forgot_password.lower() == "y":
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm your new password: ")
            
            if confirm_password != new_password:
                print("Make sure the passwords are the same!")
                return
            
            singleton.forgot_password(singleton, account, new_password)
        else:
            print("Exiting...")
    else:
        print("Account doesn't exist.")
        
        should_create = input("Create new Account? y/n ")
        
        if should_create.lower() == "y":
            email = input("Enter an email: ")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            
            singleton.create_account(singleton, email, username, password)
        else:
            print("Invalid choice!")
            return

if __name__ == "__main__":
    main()