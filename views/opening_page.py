import flet as ft
from flet_route import Params, Basket

class OpeningPage():
    def __init__(self):
        logo = ft.Image(
            src = "/logo.png",
            width = 400,
            height = 400
        )
        
        logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[logo]
        )
        
        self.login_button = ft.ElevatedButton(
            # bgcolor = "#d6d6d6",
            width = 250,
            height = 48,
            content = ft.Text(
                value = "Log in",
                # color = "#ae8948",
                size = 20
            ),
        )
        
        login_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [self.login_button]
        )
        
        self.account_none_indicator = ft.Text(
            value = "Don't have an account?",
            # color = "#ae8948",
            size = 16
        )
        
        account_none_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [self.account_none_indicator]
        )
        
        self.signup_button = ft.ElevatedButton(
            # bgcolor = "#d6d6d6",
            width = 250,
            height = 48,
            content = ft.Text(
                value = "Sign up",
                # color = "#ae8948",
                size = 20
            ),
        )
        
        signup_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [self.signup_button]
        )
        
        main_column = ft.Column(
            controls = [logo_row, login_btn_row, account_none_indicator_row, signup_btn_row]
        )
        
        self.route_address = "/"
        self.view = ft.View(
            route = self.route_address,
            # bgcolor = "#fafafa",
            controls = [main_column]
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view
    
    def update_colors(self, colors):
        self.login_button.bgcolor = colors["d6d6d6"]
        self.login_button.update()
        
        self.login_button.content.color = colors["ae8948"]
        self.login_button.content.update()
        
        self.account_none_indicator.color = colors["ae8948"]
        self.account_none_indicator.update()
        
        self.signup_button.bgcolor = colors["d6d6d6"]
        self.signup_button.update()
        
        self.signup_button.content.color = colors["ae8948"]
        self.signup_button.content.update()
        
        self.view.bgcolor = colors["fafafa"]
        self.view.update()