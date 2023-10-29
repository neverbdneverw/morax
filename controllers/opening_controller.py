from controllers.Database import Database
from views.opening_page import OpeningPage
import flet as ft

class OpeningController:
    def __init__(self, page: ft.Page, database: Database, opening_page: OpeningPage):
        self.page = page
        self.database = database
        self.opening_page = opening_page
        
        self.handle_automatic_login()
        
        self.opening_page.login_button.on_click = self.login_clicked
        self.opening_page.signup_button.on_click = self.signup_clicked
        
    def login_clicked(self, event):
        self.page.go("/login")
    
    def signup_clicked(self, event):
        self.page.go("/signup")
    
    def handle_automatic_login(self):
        automatic_login = self.page.client_storage.get("keep_signed_in")
        email = self.page.client_storage.get("email")
        
        if automatic_login is True and email is not None and email != "":
            # self.opening_page.basket.email = email
            self.page.go("/home")