from controllers.Database import Database
from views.confirm_email_page import ConfirmEmailPage
import flet as ft

class ConfirmEmailController:
    def __init__(self, page: ft.Page, database: Database, confirm_email_page: ConfirmEmailPage):
        self.page = page
        self.database = database
        self.confirm_email_page = confirm_email_page
        
        self.confirm_email_page.code_sent_textfield.on_change = self.validate
        self.confirm_email_page.login_button.on_click = self.go_to_login
        self.confirm_email_page.confirm_email_button.on_click = self.confirm_email
    
    def validate(self, event):
        if self.confirm_email_page.get_code_input() != "":
            self.confirm_email_page.allow_confirm(True)
        else:
            self.confirm_email_page.allow_confirm(False)
    
    def go_to_login(self, event):
        self.page.go("/login")
    
    def confirm_email(self, event):
        argument_list = list(self.confirm_email_page.basket.command)
        command_type = argument_list[0]
        code = argument_list[2]
        command = argument_list[1]
        if code == int(self.confirm_email_page.code_sent_textfield.value):
            if command_type == "COMMAND_REGISTER":
                verdict = command(argument_list[3], argument_list[4], argument_list[5])
                
                if verdict == "Successful":
                    self.confirm_email_page.display_on_dialog("Success!", "Your account has been created. You may now log in.")
                    self.database.update_refs()
                else:
                    self.confirm_email_page.display_on_dialog("Can't Register", "An account is already linked to the credentials given.")
            elif command_type == "COMMAND_CHANGE_PASSWORD":
                verdict = command(argument_list[3], argument_list[4])
                
                if verdict == "Password Changed":
                    self.confirm_email_page.display_on_dialog("Success!", "Your password has been updated. You may now log in again.")
                    self.database.update_refs()
                else:
                    self.confirm_email_page.display_on_dialog("Can't Change Password", "An account bound to the email doesn't exist.")
            else:
                self.confirm_email_page.display_on_dialog("Can't Do operation", "The process to be done is not expected.")
        else:
            if command_type == "COMMAND_REGISTER":
                self.confirm_email_page.display_on_dialog("Can't Register", "The code sent must match the entered code.")
            elif command_type == "COMMAND_CHANGE_PASSWORD":
                self.confirm_email_page.display_on_dialog("Can't Change Password", "The code sent must match the entered code.")