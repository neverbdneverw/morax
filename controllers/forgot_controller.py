from controllers.Database import Database
from views.forgot_password_page import ForgotPasswordPage
import flet as ft

class ForgotController:
    def __init__(self, page: ft.Page, database: Database, forgot_password_page: ForgotPasswordPage):
        self.page = page
        self.database = database
        self.forgot_password_page = forgot_password_page
        
        self.forgot_password_page.new_password_textfield.on_change = self.validate
        self.forgot_password_page.confirm_new_password_textfield.on_change = self.validate
        self.forgot_password_page.signup_button.on_click = self.go_to_signup
        self.forgot_password_page.change_password_btn.on_click = self.change_password
    
    def validate(self, event):
        verdict = all([
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
    
    def forgot_password(self, event):
        self.page.go("/forgot_password")
    
    def change_password(self, event):
        self.page.go("/confirm_email")