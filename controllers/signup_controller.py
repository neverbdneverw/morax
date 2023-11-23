from model import Model
from views import SignupPage
import flet as ft

class SignupController:
    def __init__(self, page: ft.Page, model: Model, signup_page: SignupPage):
        self.page = page
        self.model = model
        self.signup_page = signup_page
        
        self.signup_page.email_textfield.on_change = self.validate
        self.signup_page.username_textfield.on_change = self.validate
        self.signup_page.password_textfield.on_change = self.validate
        self.signup_page.confirm_password_textfield.on_change = self.validate
        self.signup_page.agree_eula_check.on_change = self.validate
        self.signup_page.login_button.on_click = self.go_to_login
        self.signup_page.register_btn.on_click = self.register
    
    def validate(self, event):
        verdict = all([
            self.signup_page.get_email_entry() != "",
            self.signup_page.get_username_entry() != "",
            self.signup_page.get_password_entry() != "",
            self.signup_page.get_confirm_password_entry() != "",
            self.signup_page.get_agree_eula_entry(),
            self.signup_page.get_password_entry() == self.signup_page.get_confirm_password_entry()
        ])
        
        if verdict is True:
            self.signup_page.allow_register(True)
        else:
            self.signup_page.allow_register(False)
    
    def register(self, event):
        code = self.model.confirm_email_ownership(self.signup_page.get_email_entry())
        command = [
            "COMMAND_REGISTER",
            self.model.create_account,
            code,
            self.signup_page.get_email_entry(),
            self.signup_page.get_username_entry(),
            self.signup_page.get_password_entry(),
        ]
        self.signup_page.basket.command = command
        self.page.go("/confirm_email")
    
    def go_to_login(self, event):
        self.page.go("/login")