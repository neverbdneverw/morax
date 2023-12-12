import flet as ft
from flet_route import Params, Basket

class SignupPage():
    def __init__(self):
        query_icon = ft.Image(
            src = "/logo_filled.png",
            width = 96,
            height = 96
        )
        
        image_container = ft.Container(
            content=query_icon,
            padding=ft.padding.only(20, 20, 20, 0)
        )
        
        self.signup_indicator_text = ft.Text(
            value="Sign up",
            weight=ft.FontWeight.W_700,
            size=54
        )
        
        signup_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        signup_indicator_row.controls.append(self.signup_indicator_text)
        
        self.welcome_back_text = ft.Text(
            "Fill your information below",
            size = 24
        )
        
        welcome_back_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        welcome_back_row.controls.append(self.welcome_back_text)
        
        self.email_textfield = ft.TextField(
            label = "Email",
            border_radius = 25,
            cursor_height=20,
            expand = True,
            height=44,
            label_style = ft.TextStyle()
        )
        
        email_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        email_textfield_row.controls.append(self.email_textfield)
        
        self.username_textfield = ft.TextField(
            label = "Username",
            border_radius = 25,
            cursor_height=20,
            expand = True,
            height=44,
            label_style = ft.TextStyle()
        )
        
        username_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        username_textfield_row.controls.append(self.username_textfield)
        
        self.password_textfield = ft.TextField(
            label = "Password",
            border_radius = 25,
            cursor_height=20,
            expand = True,
            height=44,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle()
        )
        
        password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        password_textfield_row.controls.append(self.password_textfield)
        
        self.confirm_password_textfield = ft.TextField(
            label = "Confirm Password",
            border_radius = 25,
            expand = True,
            height=44,
            cursor_height=20,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle()
        )
        
        confirm_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        confirm_password_textfield_row.controls.append(self.confirm_password_textfield)
        
        self.agree_eula_check = ft.Checkbox(
            value=False
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
            width = 200,
            height = 44,
            disabled=True,
            content=ft.Text(
                value="Register",
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
        
        self.login_indicator_text = ft.Text(
            value="Already have an account?",
            color = ft.colors.BLACK,
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
        
        sidebar_top_column = ft.Column(
            expand=True,
            spacing=10,
            controls = [
                signup_indicator_row,
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
            spacing=10,
            controls= [
                login_indicator_text_row,
                login_btn_container
            ]
        )
        
        sidebar_main_column = ft.Column(
            controls=[sidebar_top_column, sidebar_bottom_column],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.sidebar_container = ft.Container(
            expand = True,
            padding = 15,
            content = sidebar_main_column
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
        
        self.route_address = "/signup"
        self.view = ft.View(
            route=self.route_address,
            padding = 0,
            controls = [self.main_container]
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
        self.basket = basket
        self.page = page
        return self.view
    
    def allow_register(self, allow: bool):
        self.register_btn.disabled = (allow == False)
        self.page.update()
    
    def update_colors(self, colors):
        self.signup_indicator_text.color = colors["black"]
        
        self.welcome_back_text.color = colors["black"]
        
        self.email_textfield.border_color = colors["d6d6d6"]
        self.email_textfield.cursor_color = colors["black"]
        self.email_textfield.bgcolor = colors["d6d6d6"]
        self.email_textfield.color = colors["black"]
        self.email_textfield.label_style.color = colors["black"]
        
        self.username_textfield.border_color = colors["d6d6d6"]
        self.username_textfield.cursor_color = colors["black"]
        self.username_textfield.bgcolor = colors["d6d6d6"]
        self.username_textfield.color = colors["black"]
        self.username_textfield.label_style.color = colors["black"]
        
        self.password_textfield.border_color = colors["d6d6d6"]
        self.password_textfield.cursor_color = colors["black"]
        self.password_textfield.bgcolor = colors["d6d6d6"]
        self.password_textfield.color = colors["black"]
        self.password_textfield.label_style.color = colors["black"]
        
        self.confirm_password_textfield.border_color = colors["d6d6d6"]
        self.confirm_password_textfield.cursor_color = colors["black"]
        self.confirm_password_textfield.bgcolor = colors["d6d6d6"]
        self.confirm_password_textfield.color = colors["black"]
        self.confirm_password_textfield.label_style.color = colors["black"]
        
        self.agree_eula_check.fill_color = colors["d6d6d6"]
        self.agree_eula_check.check_color = colors["ae8948"]
        
        self.register_btn.bgcolor = colors["d6d6d6"]
        self.register_btn.content.color = colors["ae8948"]
        
        self.login_button.bgcolor = colors["d6d6d6"]
        self.login_button.content.color = colors["ae8948"]
        
        self.login_indicator_text.color = colors["black"]
        
        self.sidebar_container.bgcolor = colors["fafafa"]
        
        # self.main_container.gradient.colors = [
        #     colors["9a6e32"],
        #     colors["c7ac65"],
        #     colors["c7ac65"],
        #     colors["c7ac65"]
        # ]
        
        # self.view.bgcolor = colors["9a6e32"]