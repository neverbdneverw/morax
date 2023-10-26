from controllers.Database import Database
from views.signup_page import SignupPage
import flet as ft

class SignupController:
    def __init__(self, page: ft.Page, database: Database, signup_page: SignupPage):
        self.page = page
        self.database = database
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
        self.page.go("/confirm_email")
    
    def go_to_login(self, event):
        self.page.go("/login")
    
    def forgot_password(self, event):
        self.page.go("/forgot_password")