import flet as ft

class AccountView(ft.Container):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(4.5, 0),
            animate_offset=ft.animation.Animation(300)
        )
        
        self.user_picture = ft.Image(
            src = "/empty_user_image.svg",
            width=100,
            height=100
        )
        
        user_picture_container = ft.Container(
            self.user_picture,
            border_radius=15
        )
        
        self.change_user_picture_button = ft.ElevatedButton(
            text="Change",
        )
        
        self.username_text = ft.Text(
            "Owen David",
            size="36",
            weight=ft.FontWeight.BOLD,
        )
        
        self.email_text = ft.Text(
            "22-04905@g.batstate-u.edu.ph",
            size="16",
        )
        
        user_info_column = ft.Column(
            controls=[self.username_text, self.email_text],
            expand=True
        )
        
        picture_row = ft.Row(
            controls=[
                user_picture_container,
                user_info_column
            ]
        )
        
        profile_info_column = ft.Column(
            controls = [picture_row, self.change_user_picture_button],
            expand=True
        )
        
        self.profile_info_container = ft.Container(
            profile_info_column,
            padding=ft.padding.all(10),
            # margin=ft.margin.only(150, 0, 150, 0),
            gradient=ft.LinearGradient(
                colors=[
                    "#9a6e32",
                    "#c7ac65"
                ]
            )
        )
        
        account_labeler = ft.Text(
            "Account",
            size=18,
            weight=ft.FontWeight.BOLD
        )
        
        self.edit_profile_button = ft.Container(
            content = ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOCK, color="#c09451"),
                            ft.Text("Edit Username", color="black", weight=ft.FontWeight.W_400)
                        ]
                    ),
                    ft.Icon(ft.icons.NAVIGATE_NEXT, color="#c09451")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(22, 0, 22, 0)
        )
        
        security_labeler = ft.Text(
            "Security",
            size=18,
            weight=ft.FontWeight.BOLD
        )
        
        self.change_password_button = ft.Container(
            content = ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOCK, color="#c09451"),
                            ft.Text("Change Password", color="black", weight=ft.FontWeight.W_400)
                        ]
                    ),
                    ft.Icon(ft.icons.NAVIGATE_NEXT, color="#c09451")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(22, 0, 22, 0)
        )
        
        self.gcash_button = ft.Container(
            content = ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("G", weight=ft.FontWeight.W_900, size = 32, color="#c09451"),
                            ft.Text("GCash", color="black", weight=ft.FontWeight.W_400)
                        ]
                    ),
                    ft.Icon(ft.icons.NAVIGATE_NEXT, color="#c09451")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(22, 0, 22, 0)
        )
        
        account_settings_column = ft.Column(
            controls=[
                account_labeler,
                self.edit_profile_button,
                security_labeler,
                self.change_password_button,
                self.gcash_button
            ],
            spacing=10,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )
        
        self.account_settings_container = ft.Container(
            account_settings_column,
            padding=ft.padding.all(10),
            # margin=ft.margin.only(150, 0, 150, 0),
            expand=True
        )
        
        self.logout_button = ft.ElevatedButton(
            "Log Out",
            width=200,
            height=36
        )
        
        logout_column = ft.Column(
            controls=[
                ft.Row(
                    [self.logout_button],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )
        
        self.logout_button_container = ft.Container(
            logout_column,
            padding=ft.padding.all(10),
            # margin=ft.margin.only(150, 0, 150, 0),
            expand=True
        )
        
        self.content = ft.Column(
            [self.profile_info_container, self.account_settings_container, self.logout_button_container],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    
    def show(self, delta):
        self.offset = ft.transform.Offset(delta, 0)
        self.update()
    
    def update_colors(self, colors):
        self.change_user_picture_button.bgcolor = colors["f8fafc"]
        self.change_user_picture_button.color = colors["c09451"]
        self.username_text.color = colors["fcffff"]
        self.email_text.color = colors["fcffff"]
        
        self.profile_info_container.gradient.colors = [
            colors["9a6e32"],
            colors["c7ac65"]
        ]
        
        self.bgcolor = colors["f6f7f8"]
        self.account_settings_container.bgcolor = colors["white"]
        self.logout_button_container.bgcolor = colors["white"]
        
        self.logout_button.bgcolor = colors["ae8948"]
        self.logout_button.color = colors["fcffff"]
        
        self.edit_profile_button.content.controls[0].controls[0].color = colors["c09451"]
        self.edit_profile_button.content.controls[0].controls[1].color = colors["black"]
        self.edit_profile_button.content.controls[1].color = colors["c09451"]
        
        self.change_password_button.content.controls[0].controls[0].color = colors["c09451"]
        self.change_password_button.content.controls[0].controls[1].color = colors["black"]
        self.change_password_button.content.controls[1].color = colors["c09451"]
        
        self.gcash_button.content.controls[0].controls[0].color = colors["c09451"]
        self.gcash_button.content.controls[0].controls[1].color = colors["black"]
        self.gcash_button.content.controls[1].color = colors["c09451"]