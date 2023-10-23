from DataRetriever import DataRetriever

def main():
    data_retriever = DataRetriever()
    account = input("What email do you use to login? ")
    password = input("Enter a password: ")
    
    account_found = data_retriever.is_account_found(account, password)
    
    if account_found == "Found":
        print("Login successful!")
    elif account_found == "Wrong password":
        forgot_password = input("Password might be incorrect. Forgot it? y/n ")
        if forgot_password.lower() == "y":
            code = data_retriever.confirm_email_ownership(account)
            
            print("Wait for the code sent through your email.\nIf you have not receive it, check your spam folder.")
        
            received_code = input("What is the code you received in your email? ")
            
            if code == int(received_code):
                new_password = input("Enter a new password: ")
                confirm_password = input("Confirm your new password: ")
                
                if confirm_password != new_password:
                    print("Make sure the passwords are the same!")
                    return
                
                result = data_retriever.forgot_password(account, new_password)
                print(result)
        else:
            print("Exiting...")
    else:
        print("Account doesn't exist.")
        
        should_create = input("Create new Account? y/n ")
        
        if should_create.lower() == "y":
            email = input("Enter an email: ")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            
            code = data_retriever.confirm_email_ownership(email)
            
            print("Wait for the code sent through your email.\nIf you have not receive it, check your spam folder.")
        
            received_code = input("What is the code you received in your email? ")
            
            if code == int(received_code):
                account_created = data_retriever.create_account(email, username, password)
                
                print(account_created)
        else:
            print("Invalid choice!")
            return

if __name__ == "__main__":
    main()