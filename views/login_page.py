import flet as ft
from flet_route import Params, Basket

class LoginPage():
    def __init__(self):
        lock_icon = ft.Image(
            src = "resources/lock.svg",
            width = 200,
            height = 200
        )
        
        image_container = ft.Container(
            expand=True,
            content=lock_icon
        )
        
        login_indicator_text = ft.Text(
            value="Log in",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=54
        )
        
        login_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        login_indicator_row.controls.append(login_indicator_text)
        
        welcome_back_text = ft.Text(
            "Welcome back user",
            color = ft.colors.BLACK,
            size = 24
        )
        
        welcome_back_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        welcome_back_row.controls.append(welcome_back_text)
        
        self.email_textfield = ft.TextField(
            label = "Email",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            cursor_color="black",
            bgcolor="#d6d6d6",
            expand=True,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        email_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        email_textfield_row.controls.append(self.email_textfield)
        
        self.password_textfield = ft.TextField(
            label = "Password",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            expand=True,
            cursor_color="black",
            password=True,
            can_reveal_password=True,
            bgcolor="#d6d6d6",
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        password_textfield_row.controls.append(self.password_textfield)
        
        keep_logged_check = ft.Checkbox(
            value=False,
            fill_color="#d6d6d6",
            check_color="#ae8948"
        )
        
        keep_logged_indicator_text = ft.Text(
            value="Keep me signed in",
            expand=True
        )
        
        forgot_password_text = ft.Text(
            "Forgot Password?",
            color="#9a6e32"
        )
        
        self.forgot_password_btn = ft.Container(
            content=forgot_password_text
        )
        
        keep_logged_check_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[keep_logged_check, keep_logged_indicator_text, self.forgot_password_btn]
        )
        
        self.login_btn = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 200,
            height = 44,
            disabled=True,
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
        login_btn_row.controls.append(self.login_btn)
        
        login_btn_container = ft.Container(
            content=login_btn_row,
            margin=20
        )
        
        signup_indicator_text = ft.Text(
            value="Don't have an account yet?",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_200,
            size=16
        )
        
        signup_indicator_text_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[signup_indicator_text]
        )
        
        self.signup_button = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 200,
            height = 44,
            content=ft.Text(
                value="Sign up",
                color = "#ae8948",
                size=24
            )
        )
        
        signup_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        signup_btn_row.controls.append(self.signup_button)
        
        signup_btn_container = ft.Container(
            content=signup_btn_row
        )
        
        sidebar_column_top = ft.Column(
            spacing=20,
            controls = [
                login_indicator_row,
                welcome_back_row,
                email_textfield_row,
                password_textfield_row,
                keep_logged_check_row,
                login_btn_container,
            ]
        )
        
        sidebar_column_bottom = ft.Column(
            spacing=20,
            alignment=ft.alignment.bottom_center,
            controls = [
                signup_indicator_text_row,
                signup_btn_container
            ]
        )
        
        sidebar_main_column = ft.Column(
            controls=[sidebar_column_top,sidebar_column_bottom],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        sidebar_container = ft.Container(
            expand = True,
            bgcolor = "#fafafa",
            content = sidebar_main_column,
            padding = 40,
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
            route="/login",
            bgcolor = "#9a6e32",
            padding = 0,
            controls = [main_container]
        )
        
        ###### DIALOGS ######
        self.dialog_text = ft.Text(
            size=12
        )
        
        self.warning_dialog = ft.AlertDialog(
            title=ft.Text(
                value="Can't Log in.",
                size=20
            ),
            content=self.dialog_text
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view
    
    def get_email_entry(self):
        return self.email_textfield.value
    
    def get_password_entry(self):
        return self.password_textfield.value
    
    def allow_login(self, allow: bool):
        self.login_btn.disabled = (allow == False)
        self.page.update()
    
    def display_on_dialog(self, message: str):
        self.dialog_text.value = message
        self.page.dialog = self.warning_dialog
        self.warning_dialog.open = True
        self.page.update()