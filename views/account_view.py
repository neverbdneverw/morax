import flet as ft

class AccountView(ft.Container):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(0, 4.5),
            animate_offset=ft.animation.Animation(300)
        )
        
        self.user_picture = ft.Image(
            src = "resources/empty_user_image.svg",
            width=100,
            height=100
        )
        
        self.change_user_picture_button = ft.ElevatedButton(
            text="Change",
            bgcolor="#f8fafc",
            color="#c09451"
        )
        
        self.username_text = ft.Text(
            "Owen David",
            size="36",
            weight=ft.FontWeight.BOLD,
            color="#fcffff"
        )
        
        self.email_text = ft.Text(
            "22-04905@g.batstate-u.edu.ph",
            size="16",
            color="#fcffff"
        )
        
        user_info_column = ft.Column(
            controls=[self.username_text, self.email_text],
            expand=True
        )
        
        picture_row = ft.Row(
            controls=[
                self.user_picture,
                user_info_column
            ]
        )
        
        profile_info_column = ft.Column(
            controls = [picture_row, self.change_user_picture_button],
            expand=True
        )
        
        profile_info_container = ft.Container(
            profile_info_column,
            padding=ft.padding.all(20),
            margin=ft.margin.only(150, 0, 150, 0),
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
        
        button_label_contents = ft.Row(
            controls=[
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.EDIT, color="#c09451"),
                        ft.Text("Edit Profile", color="black", weight=ft.FontWeight.W_400)
                    ]
                ),
                ft.Icon(ft.icons.NAVIGATE_NEXT, color="#c09451")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.edit_profile_button = ft.ElevatedButton(
            content=button_label_contents,
            bgcolor="#d6d6d6"
        )
        
        security_labeler = ft.Text(
            "Security",
            size=18,
            weight=ft.FontWeight.BOLD
        )
        
        change_password_button = ft.Container(
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
        
        gcash_button = ft.Container(
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
                change_password_button,
                gcash_button
            ],
            spacing=10,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )
        
        account_settings_container = ft.Container(
            account_settings_column,
            bgcolor="white",
            padding=ft.padding.all(50),
            margin=ft.margin.only(150, 0, 150, 0),
            expand=True
        )
        
        self.logout_button = ft.ElevatedButton(
            "Log Out",
            bgcolor="#ae8948",
            color="#fcffff",
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
        
        logout_button_container = ft.Container(
            logout_column,
            bgcolor="white",
            padding=ft.padding.all(20),
            margin=ft.margin.only(150, 0, 150, 0),
            expand=True
        )
        
        self.content = ft.Column(
            [profile_info_container, account_settings_container, logout_button_container],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
        
        self.bgcolor = "#f5f7f8"
    
    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()