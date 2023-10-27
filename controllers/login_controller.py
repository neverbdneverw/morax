from controllers.Database import Database
from views.login_page import LoginPage
import flet as ft

class LoginController:
    def __init__(self, page: ft.Page, database: Database, login_page: LoginPage):
        self.page = page
        self.database = database
        self.login_page = login_page
        
        self.login_page.email_textfield.on_change = self.validate
        self.login_page.password_textfield.on_change = self.validate
        self.login_page.login_btn.on_click = self.login
        self.login_page.forgot_password_btn.on_click = self.forgot_password
        self.login_page.signup_button.on_click = self.go_to_signup
        self.login_page.keep_logged_check.on_change = self.handle_automatic_login
    
    def validate(self, event):
        if self.login_page.get_email_entry() != "" and self.login_page.get_password_entry() != "":
            self.login_page.allow_login(True)
        else:
            self.login_page.allow_login(False)
    
    def login(self, event):
        verdict = self.database.query_login(self.login_page.get_email_entry(), self.login_page.get_password_entry())
        if verdict == "Found":
            email = self.login_page.get_email_entry()
            self.login_page.basket.email = email
            self.page.client_storage.set("email", email)
            self.page.go("/home")
        elif verdict == "Not found":
            self.login_page.display_on_dialog("Username or Password might be wrong. Please Try Again.")
        else:
            self.login_page.display_on_dialog("Password is wrong. Please Try Again.")
    
    def handle_automatic_login(self, event):
        setting = self.login_page.get_keep_signed_in()
        self.page.client_storage.set("keep_signed_in", setting)
    
    def go_to_signup(self, event):
        self.page.go("/signup")
    
    def forgot_password(self, event):
        self.page.go("/forgot_password")