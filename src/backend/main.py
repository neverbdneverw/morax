from DataRetriever import DataRetriever
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    singleton = DataRetriever()
    account = input("What email do you use to login? ")
    password = input("Enter a password: ")
    
    if singleton.is_account_found(singleton, account, password):
        print("Login successful!")
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