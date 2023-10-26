import flet as ft
from flet_route import Params, Basket

class SignupPage():
    def __init__(self):
        query_icon = ft.Image(
            src = "resources/question_mark.svg",
            width = 200,
            height = 200
        )
        
        image_container = ft.Container(
            expand=True,
            content=query_icon
        )
        
        login_indicator_text = ft.Text(
            value="Sign up",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=54
        )
        
        login_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        login_indicator_row.controls.append(login_indicator_text)
        
        welcome_back_text = ft.Text(
            "Fill your information below",
            color = ft.colors.BLACK,
            size = 24
        )
        
        welcome_back_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        welcome_back_row.controls.append(welcome_back_text)
        
        self.email_textfield = ft.TextField(
            label = "Email",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            bgcolor="#d6d6d6",
            cursor_color="black",
            cursor_height=20,
            expand = True,
            height=44,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        email_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        email_textfield_row.controls.append(self.email_textfield)
        
        self.username_textfield = ft.TextField(
            label = "Username",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            cursor_color="black",
            cursor_height=20,
            bgcolor="#d6d6d6",
            expand = True,
            height=44,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        username_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        username_textfield_row.controls.append(self.username_textfield)
        
        self.password_textfield = ft.TextField(
            label = "Password",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            bgcolor="#d6d6d6",
            cursor_color="black",
            cursor_height=20,
            expand = True,
            height=44,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        password_textfield_row.controls.append(self.password_textfield)
        
        self.confirm_password_textfield = ft.TextField(
            label = "Confirm Password",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            bgcolor="#d6d6d6",
            cursor_color="black",
            expand = True,
            height=44,
            cursor_height=20,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        confirm_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        confirm_password_textfield_row.controls.append(self.confirm_password_textfield)
        
        self.agree_eula_check = ft.Checkbox(
            value=False,
            fill_color="#d6d6d6",
            check_color="#ae8948"
        )
        
        agree_eula_indicator_text = ft.Text(
            value="I agree to the Terms and Conditions of using this service.",
            expand=True
        )
        
        agree_eula_check_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ self.agree_eula_check,  agree_eula_indicator_text]
        )
        
        self.register_btn = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 200,
            height = 44,
            disabled=True,
            content=ft.Text(
                value="Register",
                color = "#ae8948",
                size=24
            )
        )
        
        register_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        register_btn_row.controls.append(self.register_btn)
        
        register_btn_container = ft.Container(
            content=register_btn_row
        )
        
        login_indicator_text = ft.Text(
            value="Already have an account?",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_200,
            size=16
        )
        
        login_indicator_text_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[login_indicator_text]
        )
        
        self.login_button = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 200,
            height = 44,
            content=ft.Text(
                value="Log in",
                color = "#ae8948",
                size=24
            )
        )
        
        login_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        login_btn_row.controls.append(self.login_button)
        
        login_btn_container = ft.Container(
            content=login_btn_row
        )
        
        sidebar_top_column = ft.Column(
            expand=True,
            spacing=20,
            controls = [
                login_indicator_row,
                welcome_back_row,
                email_textfield_row,
                username_textfield_row,
                password_textfield_row,
                confirm_password_textfield_row,
                agree_eula_check_row,
                register_btn_container
            ]
        )
        
        sidebar_bottom_column = ft.Column(
            spacing=20,
            controls= [
                login_indicator_text_row,
                login_btn_container
            ]
        )
        
        sidebar_main_column = ft.Column(
            controls=[sidebar_top_column, sidebar_bottom_column],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        sidebar_container = ft.Container(
            expand = True,
            padding = 40,
            bgcolor = "#fafafa",
            content = sidebar_main_column,
        )
        
        main_row = ft.Row(
            expand=True,
            controls = [
                image_container,
                sidebar_container
            ]
        )
        
        main_container = ft.Container(
            expand=True,
            content=main_row,
            gradient=ft.LinearGradient(
                begin=ft.alignment.center_left,
                end=ft.alignment.center_right,
                colors=[
                    "#9a6e32",
                    "#c7ac65",
                    "#c7ac65",
                    "#c7ac65"
                ]
            )
        )
        
        self.view = ft.View(
            route="/signup",
            bgcolor = "#9a6e32",
            padding = 0,
            controls = [main_container]
        )
    
    def get_email_entry(self):
        return self.email_textfield.value
    
    def get_username_entry(self):
        return self.username_textfield.value
    
    def get_password_entry(self):
        return self.password_textfield.value
    
    def get_confirm_password_entry(self):
        return self.confirm_password_textfield.value
    
    def get_agree_eula_entry(self):
        return self.agree_eula_check.value
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view
    
    def allow_register(self, allow: bool):
        self.register_btn.disabled = (allow == False)
        self.page.update()