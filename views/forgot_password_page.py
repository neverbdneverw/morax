import flet as ft
from flet_route import Params, Basket

class ForgotPasswordPage():
    def __init__(self):
        query_icon = ft.Image(
            src = "/question_mark.svg",
            width = 200,
            height = 200
        )
        
        image_container = ft.Container(
            expand=True,
            content=query_icon
        )
        
        fg_pass_indicator_text = ft.Text(
            value="Oh no!",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=54
        )
        
        fg_pass_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        fg_pass_indicator_row.controls.append(fg_pass_indicator_text)
        
        fg_pass_reminder_text = ft.Text(
            "Create a memorable password next time.",
            color = ft.colors.BLACK,
            size = 24
        )
        
        fg_pass_reminder_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        fg_pass_reminder_row.controls.append(fg_pass_reminder_text)
        
        self.email_textfield = ft.TextField(
            label = "Email",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            cursor_color="black",
            bgcolor="#d6d6d6",
            expand=True,
            height=44,
            cursor_height=20,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        email_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        email_textfield_row.controls.append(self.email_textfield)
        
        self.new_password_textfield = ft.TextField(
            label = "New Password",
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
        
        new_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        new_password_textfield_row.controls.append(self.new_password_textfield)
        
        self.confirm_new_password_textfield = ft.TextField(
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
        
        confirm_new_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        confirm_new_password_textfield_row.controls.append(self.confirm_new_password_textfield)
        
        self.change_password_btn = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 250,
            height = 44,
            disabled=True,
            content=ft.Text(
                value="Change your password",
                color = "#ae8948",
                size=18
            )
        )
        
        change_password_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        change_password_btn_row.controls.append(self.change_password_btn)
        
        change_password_btn_container = ft.Container(
            content=change_password_btn_row
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
        
        sidebar_top_column = ft.Column(
            expand=True,
            spacing=20,
            controls = [
                fg_pass_indicator_row,
                fg_pass_reminder_row,
                email_textfield_row,
                new_password_textfield_row,
                confirm_new_password_textfield_row,
                change_password_btn_container
            ]
        )
        
        sidebar_bottom_column = ft.Column(
            spacing=20,
            controls= [
                signup_indicator_text_row,
                signup_btn_container
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
            route="/forgot_password",
            bgcolor = "#9a6e32",
            padding = 0,
            controls = [main_container]
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view
    
    def get_email_to_send_entry(self):
        return self.email_textfield.value

    def get_new_password_entry(self):
        return self.new_password_textfield.value
    
    def get_confirm_new_password_entry(self):
        return self.confirm_new_password_textfield.value
    
    def allow_password_change(self, allow: bool):
        self.change_password_btn.disabled = (allow == False)
        self.page.update()