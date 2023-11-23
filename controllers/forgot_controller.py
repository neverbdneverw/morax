from model import Model
from views import ForgotPasswordPage
import flet as ft

class ForgotController:
    def __init__(self, page: ft.Page, model: Model, forgot_password_page: ForgotPasswordPage):
        self.page = page
        self.model = model
        self.forgot_password_page = forgot_password_page
        
        self.forgot_password_page.new_password_textfield.on_change = self.validate
        self.forgot_password_page.confirm_new_password_textfield.on_change = self.validate
        self.forgot_password_page.email_textfield.on_change = self.validate
        self.forgot_password_page.signup_button.on_click = self.go_to_signup
        self.forgot_password_page.change_password_btn.on_click = self.change_password
    
    def validate(self, event):
        verdict = all([
            self.forgot_password_page.get_email_to_send_entry() != "",
            self.forgot_password_page.get_new_password_entry() != "",
            self.forgot_password_page.get_confirm_new_password_entry() != "",
            self.forgot_password_page.get_new_password_entry() == self.forgot_password_page.get_confirm_new_password_entry()
        ])
        
        if verdict:
            self.forgot_password_page.allow_password_change(True)
        else:
            self.forgot_password_page.allow_password_change(False)
    
    def go_to_signup(self, event):
        self.page.go("/signup")
    
    def change_password(self, event):
        code = self.model.confirm_email_ownership(self.forgot_password_page.get_email_to_send_entry())
        command = [
            "COMMAND_CHANGE_PASSWORD",
            self.model.change_password,
            code,
            self.forgot_password_page.get_email_to_send_entry(),
            self.forgot_password_page.get_new_password_entry(),
        ]
        self.forgot_password_page.basket.command = command
        self.page.go("/confirm_email")