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
        print("Confirm")