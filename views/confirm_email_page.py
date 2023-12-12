import flet as ft
from flet_route import Params, Basket

class ConfirmEmailPage():
    def __init__(self):
        lock_icon = ft.Image(
            src = "/logo_filled.png",
            width = 96,
            height = 96
        )
        
        image_container = ft.Container(
            content=lock_icon,
            padding=ft.padding.only(20, 20, 20, 0)
        )
        
        self.confirm_email_indicator_text = ft.Text(
            value="Confirm Email",
            weight=ft.FontWeight.W_700,
            size=44
        )
        
        confirm_email_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        confirm_email_indicator_row.controls.append(self.confirm_email_indicator_text)
        
        self.code_sent_indicator_text = ft.Text(
            value="A code was sent to your email.",
            size = 24
        )
        
        code_sent_indicator_text_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.code_sent_indicator_text]
        )
        
        self.code_sent_textfield = ft.TextField(
            label = "Code sent",
            border_radius = 25,
            expand=True,
            label_style = ft.TextStyle()
        )
        
        code_sent_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        code_sent_textfield_row.controls.append(self.code_sent_textfield)
        
        self.confirm_email_button = ft.ElevatedButton(
            width = 250,
            height = 44,
            disabled=True,
            content=ft.Text(
                value="Confirm Email",
                size=24
            )
        )
        
        confirm_email_btn_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        confirm_email_btn_row.controls.append(self.confirm_email_button)
        
        confirm_email_btn_container = ft.Container(
            content=confirm_email_btn_row
        )
        
        self.login_indicator_text = ft.Text(
            value="Already have an account?",
            weight=ft.FontWeight.W_200,
            size=16
        )
        
        login_indicator_text_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.login_indicator_text]
        )
        
        self.login_button = ft.ElevatedButton(
            width = 200,
            height = 44,
            content=ft.Text(
                value="Log in",
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
        
        sidebar_column_top = ft.Column(
            spacing=10,
            controls = [
                confirm_email_indicator_row,
                code_sent_indicator_text_row,
                code_sent_textfield_row,
                confirm_email_btn_container
            ]
        )
        
        sidebar_column_bottom = ft.Column(
            spacing=10,
            alignment=ft.alignment.bottom_center,
            controls = [
                login_indicator_text_row,
                login_btn_container
            ]
        )
        
        sidebar_main_column = ft.Column(
            controls=[sidebar_column_top,sidebar_column_bottom],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.sidebar_container = ft.Container(
            expand = True,
            content = sidebar_main_column,
            padding = 20,
        )
        
        main_row = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                image_container,
                self.sidebar_container
            ]
        )
        
        self.main_container = ft.Container(
            expand=True,
            content=main_row,
            # gradient=ft.LinearGradient(
            #     begin=ft.alignment.center_left,
            #     end=ft.alignment.center_right,
            #     colors=[
            #         "#9a6e32",
            #         "#c7ac65",
            #         "#c7ac65",
            #         "#c7ac65"
            #     ]
            # )
        )
        
        self.route_address = "/confirm_email"
        self.view = ft.View(
            route=self.route_address,
            padding = 0,
            controls = [self.main_container]
        )
        
        self.dialog_text = ft.Text(
            size=12
        )
        
        self.warning_dialog = ft.AlertDialog(
            title=ft.Text(
                value="Can't Register",
                size=20
            ),
            content=self.dialog_text
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view
    
    def get_code_input(self):
        return self.code_sent_textfield.value
    
    def allow_confirm(self, allow: bool):
        self.confirm_email_button.disabled = (allow == False)
        self.page.update()
    
    def display_on_dialog(self, title: str, message: str):
        self.warning_dialog.title.value = title
        self.dialog_text.value = message
        self.page.dialog = self.warning_dialog
        self.warning_dialog.open = True
        self.page.update()
    
    def update_colors(self, colors):
        self.confirm_email_indicator_text.color = colors["black"]
        self.code_sent_indicator_text.color = colors["black"]
        
        self.code_sent_textfield.border_color = colors["d6d6d6"]
        self.code_sent_textfield.cursor_color = colors["black"]
        self.code_sent_textfield.bgcolor = colors["d6d6d6"]
        self.code_sent_textfield.color = colors["black"]
        self.code_sent_textfield.label_style.color = colors["black"]
        
        self.confirm_email_button.bgcolor = colors["d6d6d6"]
        self.confirm_email_button.content.color = colors["ae8948"]
        
        self.login_indicator_text.color = colors["black"]
        
        self.login_button.bgcolor = colors["d6d6d6"]
        self.login_button.content.color = colors["ae8948"]
        
        self.sidebar_container.bgcolor = colors["fafafa"]
        
        # self.main_container.gradient.colors=[
        #     colors["9a6e32"],
        #     colors["c7ac65"],
        #     colors["c7ac65"],
        #     colors["c7ac65"]
        # ]
        
        # self.view.bgcolor = colors["9a6e32"]