import flet as ft
from flet_route import Params, Basket

class OnboardingPage():
    def __init__(self):
        ###########################################
        ## MAke the onboarding UI
        ###########################################

        logo = ft.Image(
            src = "/logo_filled.png",
            width = 200,
            height = 200,
        )
        
        logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[logo]
        )
        
        self.help_button = SupportButton(ft.icons.HELP_OUTLINED, "Get Help...")
        self.contribute_button = SupportButton(ft.icons.SETTINGS_ACCESSIBILITY, "Contribute to the Project...")
        
        options_column = ft.Column(
            controls=[self.help_button, self.contribute_button],
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
            "/gcash.png",
            width = 200,
            height = 200,
        )
        
        gcash_logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[gcash_logo]
        )
        
        self.qr_image = ft.Image(
            "/sample_qr.png",
            width=100,
            height=100
        )
        
        self.qr_upload_button = ft.ElevatedButton(
            width = 200,
            height = 44,
            content=ft.Text(
                value="Upload QR Code",
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
            border_radius = 25,
            content_padding=10,
            label_style = ft.TextStyle()
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
            src = "/logo_filled.png",
            width = 200,
            height = 200,
        )
        
        profile_logo_row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[profile_logo]
        )
        
        self.user_image = ft.Image(
            "/empty_user_image.png",
            width=100,
            height=100
        )
        
        self.profile_upload_button = ft.ElevatedButton(
            width = 150,
            height = 32,
            content=ft.Text(
                value="Upload Photo",
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
            width=150
        )
        
        navigation_row = ft.Row(
            controls=[self.next_button],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
        
        self.route_address = "/onboarding"
        self.view = ft.View(
            route = self.route_address,
            controls = [switcher, navigation_row],
            vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            padding=30
        )
    
    # get view for the page
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view
    
    # update the colors with the scheme
    def update_colors(self, colors):
        self.main_column.controls[1].color = colors["4d4d4d"]
        self.profile_column.controls[1].color = colors["4d4d4d"]
        self.profile_upload_button.bgcolor = colors["d6d6d6"]
        self.profile_upload_button.content.color = colors["ae8948"]
        self.qr_upload_button.bgcolor = colors["d6d6d6"]
        self.qr_upload_button.content.color = colors["ae8948"]
        self.next_button.bgcolor = colors["d6d6d6"]
        self.next_button.color = colors["ae8948"]
        self.view.bgcolor = colors["fafafa"]
        
        self.number_textfield.border_color = colors["d6d6d6"]
        self.number_textfield.cursor_color = colors["black"]
        self.number_textfield.bgcolor = colors["d6d6d6"]
        self.number_textfield.color = colors["black"]
        self.number_textfield.label_style.color = colors["black"]
        
        self.help_button.update_colors(colors)
        self.contribute_button.update_colors(colors)

class SupportButton(ft.Container):
    def __init__(self, icon_name: ft.icons, button_name: str):
        super().__init__()
        self.icon = ft.Icon(icon_name, color="#ae8948", size=32)
        self.text = ft.Text(button_name, color="#ae8948", weight=ft.FontWeight.W_400, size=16, width=200)
        
        self.content = ft.Row(
            controls = [self.icon, self.text],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def update_colors(self, colors):
        self.icon.color = colors["ae8948"]
        self.text.color = colors["ae8948"]