from models import Repository, User
from views import ConfirmEmailPage
import flet as ft

class ConfirmEmailController:
    def __init__(self, page: ft.Page, repository: Repository, confirm_email_page: ConfirmEmailPage):
        self.page = page
        self.repository = repository
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
        code = argument_list[1]
        if code == int(self.confirm_email_page.code_sent_textfield.value):
            if command_type == "COMMAND_REGISTER":
                self.register(argument_list)
            elif command_type == "COMMAND_CHANGE_PASSWORD":
                self.change_password(argument_list)
            else:
                self.confirm_email_page.display_on_dialog("Can't Do operation", "The process to be done is not expected.")
        else:
            if command_type == "COMMAND_REGISTER":
                self.confirm_email_page.display_on_dialog("Can't Register", "The code sent must match the entered code.")
            elif command_type == "COMMAND_CHANGE_PASSWORD":
                self.confirm_email_page.display_on_dialog("Can't Change Password", "The code sent must match the entered code.")
    
    def register(self, argument_list: list):
        for user in self.repository.users:
            if user.email == str(argument_list[2]).replace(".", ","):
                self.confirm_email_page.display_on_dialog("Can't Register", "An account is already linked to the credentials given.")
                return

        new_user = User(
            email=str(argument_list[2]).replace(".", ","),
            first_run=True,
            gcash_number="",
            password=argument_list[4],
            picture_link="",
            qr_image_id="",
            username=argument_list[3]
        )

        self.repository.update_user(new_user)
        self.confirm_email_page.display_on_dialog("Success!", "Your account has been created. You may now log in.")
    
    def change_password(self, argument_list: list):
        for user in self.repository.users:
            if user.email == str(argument_list[2]).replace(".", ","):
                user.password = argument_list[3]
                self.repository.update_user(user)
                
                self.confirm_email_page.display_on_dialog("Success!", "Your password has been updated. You may now log in again.")
                return

        self.confirm_email_page.display_on_dialog("Can't Change Password", "An account bound to the email doesn't exist.")