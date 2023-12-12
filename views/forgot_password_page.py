import flet as ft
from flet_route import Params, Basket

class ForgotPasswordPage():
    def __init__(self):
        #######################################
        ## MAke the forgot password UI
        #######################################

        query_icon = ft.Image(
            src = "/question_mark.svg",
            width = 200,
            height = 200
        )
        
        image_container = ft.Container(
            expand=True,
            content=query_icon
        )
        
        self.fg_pass_indicator_text = ft.Text(
            value="Oh no!",
            weight=ft.FontWeight.W_700,
            size=54
        )
        
        fg_pass_indicator_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        fg_pass_indicator_row.controls.append(self.fg_pass_indicator_text)
        
        self.fg_pass_reminder_text = ft.Text(
            "Create a memorable password next time.",
            size = 24
        )
        
        fg_pass_reminder_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        fg_pass_reminder_row.controls.append(self.fg_pass_reminder_text)
        
        self.email_textfield = ft.TextField(
            label = "Email",
            border_radius = 25,
            expand=True,
            height=44,
            cursor_height=20,
            label_style = ft.TextStyle()
        )
        
        email_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        email_textfield_row.controls.append(self.email_textfield)
        
        self.new_password_textfield = ft.TextField(
            label = "New Password",
            border_radius = 25,
            cursor_height=20,
            expand = True,
            height=44,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle()
        )
        
        new_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        new_password_textfield_row.controls.append(self.new_password_textfield)
        
        self.confirm_new_password_textfield = ft.TextField(
            label = "Confirm Password",
            border_radius = 25,
            expand = True,
            height=44,
            cursor_height=20,
            password=True,
            can_reveal_password=True,
            label_style = ft.TextStyle()
        )
        
        confirm_new_password_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        confirm_new_password_textfield_row.controls.append(self.confirm_new_password_textfield)
        
        self.change_password_btn = ft.ElevatedButton(
            width = 250,
            height = 44,
            disabled=True,
            content=ft.Text(
                value="Change your password",
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
        
        self.signup_indicator_text = ft.Text(
            value="Don't have an account yet?",
            weight=ft.FontWeight.W_200,
            size=16
        )
        
        signup_indicator_text_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.signup_indicator_text]
        )
        
        self.signup_button = ft.ElevatedButton(
            width = 200,
            height = 44,
            content=ft.Text(
                value="Sign up",
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
        
        self.sidebar_container = ft.Container(
            expand = True,
            padding = 40,
            content = sidebar_main_column,
        )
        
        main_row = ft.Row(
            expand=True,
            controls = [
                image_container,
                self.sidebar_container
            ]
        )
        
        self.main_container = ft.Container(
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
        
        self.route_address = "/forgot_password"
        self.view = ft.View(
            route=self.route_address,
            padding = 0,
            controls = [self.main_container]
        )
    
    # Make the view for the page
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.basket = basket
        self.page = page
        return self.view
    
    # get entered email
    def get_email_to_send_entry(self):
        return self.email_textfield.value

    # get entered password
    def get_new_password_entry(self):
        return self.new_password_textfield.value
    
    # get the entered password confirmation
    def get_confirm_new_password_entry(self):
        return self.confirm_new_password_textfield.value
    
    # allow changing of password
    def allow_password_change(self, allow: bool):
        self.change_password_btn.disabled = (allow == False)
        self.page.update()
    
    # update the app colors
    def update_colors(self, colors):
        self.fg_pass_indicator_text.color = colors["black"]
        self.fg_pass_reminder_text.color = colors["black"]
        
        self.email_textfield.border_color = colors["d6d6d6"]
        self.email_textfield.cursor_color = colors["black"]
        self.email_textfield.bgcolor = colors["d6d6d6"]
        self.email_textfield.color = colors["black"]
        self.email_textfield.label_style.color = colors["black"]
        
        self.new_password_textfield.border_color = colors["d6d6d6"]
        self.new_password_textfield.cursor_color = colors["black"]
        self.new_password_textfield.bgcolor = colors["d6d6d6"]
        self.new_password_textfield.color = colors["black"]
        self.new_password_textfield.label_style.color = colors["black"]
        
        self.confirm_new_password_textfield.border_color = colors["d6d6d6"]
        self.confirm_new_password_textfield.cursor_color = colors["black"]
        self.confirm_new_password_textfield.bgcolor = colors["d6d6d6"]
        self.confirm_new_password_textfield.color = colors["black"]
        self.confirm_new_password_textfield.label_style.color = colors["black"]
        
        self.change_password_btn.bgcolor = colors["d6d6d6"]
        self.change_password_btn.content.color = colors["ae8948"]
        
        self.signup_indicator_text.color = colors["black"]
        
        self.signup_button.bgcolor = colors["d6d6d6"]
        self.signup_button.content.color = colors["ae8948"]
        
        self.sidebar_container.bgcolor = colors["fafafa"]
        
        self.main_container.gradient.colors = [
            colors["9a6e32"],
            colors["c7ac65"],
            colors["c7ac65"],
            colors["c7ac65"]
        ]
        
        self.view.bgcolor = colors["9a6e32"]