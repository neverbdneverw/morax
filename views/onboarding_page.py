import flet as ft
from flet_route import Params, Basket

class OnboardingPage():
    def __init__(self):
        logo = ft.Image(
            src = "assets/logo_filled.png",
            width = 200,
            height = 200,
        )
        
        logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[logo]
        )
        
        help_button = SupportButton(ft.icons.HELP_OUTLINED, "Get Help...")
        contribute_button = SupportButton(ft.icons.SETTINGS_ACCESSIBILITY, "Contribute to the Project...")
        
        options_column = ft.Column(
            controls=[help_button, contribute_button],
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
        
        self.main_column = ft.Column(
            controls = [
                logo_row,
                ft.Text("Welcome to Morax", weight=ft.FontWeight.BOLD, size=44),
                ft.Text("A shared financial manager", weight=ft.FontWeight.W_400, size=20, color="#4d4d4d"),
                ft.Container(options_column, padding=ft.padding.only(30, 100, 30, 100))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0,
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(300)
        )
        
        gcash_logo = ft.Image(
            "assets/gcash.png",
            width = 200,
            height = 200,
        )
        
        gcash_logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[gcash_logo]
        )
        
        self.qr_image = ft.Image(
            "assets/sample_qr.png",
            width=100,
            height=100
        )
        
        self.qr_upload_button = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 200,
            height = 44,
            content=ft.Text(
                value="Upload QR Code",
                color = "#ae8948",
                size=12
            )
        )
        
        qr_column = ft.Column(
            controls=[self.qr_image, self.qr_upload_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
        number_label = ft.Text(
            "GCash Mobile Number",
            weight=ft.FontWeight.W_600
        )
        
        self.number_textfield = ft.TextField(
            label="Enter your number here",
            color = ft.colors.BLACK,
            border_radius = 25,
            border_color = "#d6d6d6",
            cursor_color="black",
            content_padding=10,
            bgcolor="#d6d6d6",
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        number_column = ft.Column(
            controls=[number_label, self.number_textfield],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
        options_row = ft.Row(
            controls=[qr_column, number_column],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        )
        
        self.gcash_column = ft.Column(
            controls = [
                gcash_logo_row,
                ft.Text("Update your Profile Picture", weight=ft.FontWeight.BOLD, size=44),
                ft.Text("Profile pictures allow you to be easily", weight=ft.FontWeight.W_400, size=20, color="#4d4d4d"),
                ft.Container(options_row, padding=ft.padding.only(30, 100, 30, 100))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0,
            offset=ft.transform.Offset(1, 0),
            animate_offset=ft.animation.Animation(300)
        )
        
        profile_logo = ft.Image(
            src = "assets/logo_filled.png",
            width = 200,
            height = 200,
        )
        
        profile_logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[profile_logo]
        )
        
        self.user_image = ft.Image(
            "assets/empty_user_image.svg",
            width=100,
            height=100
        )
        
        self.profile_upload_button = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            width = 150,
            height = 32,
            content=ft.Text(
                value="Upload Photo",
                color = "#ae8948",
                size=12
            )
        )
        
        profile_upload_column = ft.Column(
            controls=[self.user_image, self.profile_upload_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.profile_column = ft.Column(
            controls = [
                profile_logo_row,
                ft.Text("Update your Profile Picture", weight=ft.FontWeight.BOLD, size=44),
                ft.Text("Profile pictures allow you to be easily recognizable.", weight=ft.FontWeight.W_400, size=20, color="#4d4d4d"),
                ft.Container(profile_upload_column, padding=ft.padding.only(30, 100, 30, 100))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0,
            offset=ft.transform.Offset(2, 0),
            animate_offset=ft.animation.Animation(300)
        )
        
        switcher = ft.Stack(
            controls=[self.main_column, self.gcash_column, self.profile_column]
        )
        
        self.next_button = ft.ElevatedButton(
            "Next",
            width=150,
            bgcolor="#ae8948",
            color="white"
        )
        
        navigation_row = ft.Row(
            controls=[self.next_button],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
        
        self.view = ft.View(
            route = "/onboarding",
            bgcolor = "#fafafa",
            controls = [switcher, navigation_row],
            vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            padding=30
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view

class SupportButton(ft.Container):
    def __init__(self, icon_name: ft.icons, button_name: str):
        super().__init__()
        icon = ft.Icon(icon_name, color="#ae8948", size=32)
        text = ft.Text(button_name, color="#ae8948", weight=ft.FontWeight.W_400, size=16, width=200)
        
        self.content = ft.Row(
            controls = [icon, text],
            alignment=ft.MainAxisAlignment.CENTER
        )