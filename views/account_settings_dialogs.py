import flet as ft

##################################################
## Culmination of dialogs inside the Account View
##################################################

class ProfilePictureChangeDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        ####################################################
        ## Make the ui for the profile picture changing
        ####################################################

        self.save_changes_button = ft.TextButton(
            "Save Changes",
            disabled=True
        )
        
        self.cancel_button = ft.TextButton(
            "Cancel"
        )
        
        self.actions = [self.save_changes_button, self.cancel_button]
        
        self.user_image = ft.Image(
            src = "/empty_user_image.png",
            width=200,
            height = 200
        )
        
        self.upload_profile = ft.ElevatedButton(
            "Upload photo"
        )
        
        content_column = ft.Column(
            controls=[self.user_image, self.upload_profile],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=300,
            height=300
        )
        
        self.content = content_column

class EditUsernameDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        ######################################################
        ## Make ui for changing the username
        ######################################################

        self.save_changes_button = ft.TextButton(
            "Save Changes",
            disabled=True
        )
        
        self.cancel_button = ft.TextButton(
            "Cancel"
        )
        
        self.actions = [self.save_changes_button, self.cancel_button]
        self.title = ft.Text("Edit Profile")
        
        new_username = ft.Text(
            "Enter new username:",
            width=150
        )
        
        self.new_username_textfield = ft.TextField(
            hint_text="Username"
        )
        
        username_row = ft.Row(
            controls=[new_username, self.new_username_textfield]
        )
        
        content_column = ft.Column(
            controls=[username_row],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=500,
            height=200
        )
        
        self.content = content_column

class EditPasswordDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        ##########################################################
        ## Make the UI for editing the password
        ##########################################################

        self.save_changes_button = ft.TextButton(
            "Save Changes",
            disabled=True
        )
        
        self.cancel_button = ft.TextButton(
            "Cancel"
        )
        
        self.actions = [self.save_changes_button, self.cancel_button]
        self.title = ft.Text("Edit Profile")
        
        new_password = ft.Text(
            "Enter new password:",
            width=150
        )
        
        self.new_password_textfield = ft.TextField(
            hint_text="New Password",
            password=True,
            can_reveal_password=True
        )
        
        reenter_password = ft.Text(
            "Re-enter new password:",
            width=150       
        )
        
        self.reenter_password_textfield = ft.TextField(
            hint_text="Confirm Password",
            password=True,
            can_reveal_password=True
        )
        
        password_row = ft.Row(
            controls=[new_password, self.new_password_textfield]
        )
        
        reenter_password_row = ft.Row(
            controls=[reenter_password, self.reenter_password_textfield]
        )
        
        content_column = ft.Column(
            controls=[password_row, reenter_password_row],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=500,
            height=200
        )
        
        self.content = content_column

class EditGcashDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        ####################################################
        ## Make the UI for editing the GCash Credentials
        ####################################################

        self.save_changes_button = ft.TextButton(
            "Save Changes",
            disabled=True
        )
        
        self.cancel_button = ft.TextButton(
            "Cancel"
        )
        
        self.actions = [self.save_changes_button, self.cancel_button]
        self.title = ft.Text("GCash Settings")
        
        self.qr_image = ft.Image(
            src = "/sample_qr.png",
            width=100,
            height = 100
        )
        
        self.upload_qr_button = ft.ElevatedButton(
            "Upload QR Code"
        )
        
        qr_column = ft.Column(
            controls=[self.qr_image, self.upload_qr_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        enter_gcash = ft.Text(
            "Enter GCash number:"
        )
        
        self.number_textfield = ft.TextField(
            hint_text = "GCash number"
        )
        
        number_column = ft.Column(
            controls = [enter_gcash, self.number_textfield],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.content_container = ft.Container(
            content = ft.Row(
                controls = [qr_column, number_column]
            ),
            width=500,
            height=200,
            padding=20
        )
        
        self.content = self.content_container
    
    def update_colors(self, colors):
        self.content_container.bgcolor = colors["f6f7f8"]