from views import HomePage, ProfilePictureChangeDialog, EditGcashDialog, EditUsernameDialog, EditPasswordDialog, AccountView
from model import Repository, utils

from PIL import Image
from io import BytesIO
import flet as ft
import base64
import cv2
import qrcode

class AccountSettingsDialogsController:
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
        self.home_page = home_page
        
        self.change_dp_dialog: ProfilePictureChangeDialog = home_page.change_profile_picture_dialog
        self.change_gcash_dialog: EditGcashDialog = home_page.edit_gcash_dialog
        self.change_username_dialog: EditUsernameDialog = home_page.edit_username_dialog
        self.change_password_dialog: EditPasswordDialog = home_page.edit_password_dialog
        
        self.account_view: AccountView = home_page.account_view
        
        self.email: str = self.page.client_storage.get("email")
        
        self.qr_picker = ft.FilePicker()
        self.qr_picker.on_result = self.set_qr_image
        self.page.overlay.append(self.qr_picker)
        self.page.update()
        
        self.dp_picker = ft.FilePicker()
        self.dp_picker.on_result = self.set_dp_image
        self.page.overlay.append(self.dp_picker)
        self.page.update()
        
        self.gcash_changed = self.handle_save_changes_button
        
        self.account_view.change_user_picture_button.on_click = self.show_dp_change_dialog
        self.account_view.edit_profile_button.on_click = lambda e: self.home_page.show_edit_username_dialog()
        self.account_view.change_password_button.on_click = lambda e: self.home_page.show_edit_password_dialog()
        self.account_view.gcash_button.on_click = self.show_change_gcash_dialog
        
        self.change_dp_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        self.change_username_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        self.change_password_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        self.change_gcash_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        
        self.change_dp_dialog.upload_profile.on_click = self.open_profile_image_chooser
        self.change_dp_dialog.save_changes_button.on_click = self.save_changed_dp
        
        self.change_username_dialog.new_username_textfield.on_change = self.handle_username_change
        self.change_username_dialog.save_changes_button.on_click = self.save_changed_username
        
        self.change_password_dialog.new_password_textfield.on_change = self.handle_password_change
        self.change_password_dialog.reenter_password_textfield.on_change = self.handle_password_change
        self.change_password_dialog.save_changes_button.on_click = self.save_changed_password
        
        self.change_gcash_dialog.upload_qr_button.on_click = self.open_qr_chooser
        self.change_gcash_dialog.save_changes_button.on_click = self.save_changed_gcash_infos
    
    def show_change_gcash_dialog(self, event: ft.ControlEvent):
        for user in self.repository.users:
            if user.email == self.email.replace(".", ","):
                self.change_gcash_dialog.number_textfield.value = user.gcash_number
                image_bytes = self.repository.download_image(user.qr_image_id)
                self.change_gcash_dialog.qr_image.src_base64 = utils.convert_to_base64(image_bytes)       

        self.home_page.show_change_gcash_qr_dialog()
    
    def handle_username_change(self, event: ft.ControlEvent):
        if self.change_username_dialog.new_username_textfield.value != "":
            self.change_username_dialog.save_changes_button.disabled = False
            self.change_username_dialog.save_changes_button.update()
        else:
            self.change_username_dialog.save_changes_button.disabled = True
            self.change_username_dialog.save_changes_button.update()
    
    def handle_password_change(self, event: ft.ControlEvent):
        password = self.change_password_dialog.new_password_textfield.value
        confirm = self.change_password_dialog.reenter_password_textfield.value
        
        if password != "" and confirm != "" and password == confirm:
            self.change_password_dialog.save_changes_button.disabled = False
            self.change_password_dialog.save_changes_button.update()
        else:
            self.change_password_dialog.save_changes_button.disabled = True
            self.change_password_dialog.save_changes_button.update()
    
    def show_dp_change_dialog(self, event: ft.ControlEvent):
        image_string = self.account_view.user_picture.src_base64
        self.change_dp_dialog.user_image.src_base64 = image_string
        self.home_page.show_profile_picture_change_dialog()
    
    def open_profile_image_chooser(self, event):
        self.dp_picker.pick_files("Choose a User Image", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)
    
    def open_qr_chooser(self, event):
        self.qr_picker.pick_files("Choose GCash QR Code Image", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)

    def set_dp_image(self, event: ft.FilePickerResultEvent):
        if event.files is not None:
            self.dp_image_path = event.files[0].path
            image = Image.open(self.dp_image_path).convert("RGBA")
            pil_img = image.resize((200, 200))
            self.dp_image_buffer = BytesIO()
            pil_img.save(self.dp_image_buffer, format="PNG")
            
            self.dp_image_string = base64.b64encode(self.dp_image_buffer.getvalue()).decode("utf-8")
            self.change_dp_dialog.user_image.src_base64 = self.dp_image_string
            self.change_dp_dialog.user_image.update()
            self.change_dp_dialog.save_changes_button.disabled = False
            self.change_dp_dialog.save_changes_button.update()
        else:
            self.dp_image_path = ""
            self.change_dp_dialog.save_changes_button.disabled = True
            self.change_dp_dialog.save_changes_button.update()
    
    def save_changed_dp(self, event: ft.ControlEvent):
        if self.dp_image_path != "":
            for user in self.repository.users:
                if user.email == self.email.replace(".", ","):
                    id = self.repository.upload_image(f"{user.email}|DP.png", self.dp_image_buffer)
                    user.picture_link = id
                    
                    self.repository.update_user(user)
                    
                    self.home_page.trigger_reload_account_view()
                    self.account_view.user_picture.update()
                    self.account_view.username_text.update()
                    self.account_view.email_text.update()
                    
                    self.home_page.close_dialog(event)
                    
                    self.page.snack_bar = ft.SnackBar(ft.Text("Profile Picture has been changed. Please wait for changes to take effect..."))
                    self.page.snack_bar.open = True
                    self.page.update()
                    
                    return
    
    def save_changed_username(self, event: ft.ControlEvent):
        replacement = self.change_username_dialog.new_username_textfield.value
        for user in self.repository.users:
            if user.email == self.email.replace(".", ","):
                user.username = replacement
                self.repository.update_user(user)
                self.home_page.trigger_reload_account_view()
                self.home_page.group_listview.top_text.value = f"Hello, {replacement}!"
                self.home_page.group_listview.top_text.update()
                self.account_view.user_picture.update()
                self.account_view.username_text.update()
                self.account_view.email_text.update()
                
                self.home_page.close_dialog(event)
                
                return
    
    def save_changed_password(self, event: ft.ControlEvent):
        password = self.change_password_dialog.new_password_textfield.value
        
        for user in self.repository.users:
            if user.email == self.email.replace(".", ","):
                user.password = password
                self.repository.update_user(user)
                
                self.home_page.close_dialog(event)
                
                text = ft.Text("Your password has been successfully changed.")
                self.page.snack_bar = ft.SnackBar(text, duration=3000)
                self.page.snack_bar.open = True
                self.page.update()
                
                return
    
    def set_qr_image(self, event: ft.FilePickerResultEvent):
        if event.files is not None:
            self.qr_image_path = event.files[0].path
            image = cv2.imread(self.qr_image_path)
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecode(image)
            
            if data == "" or data == None:
                self.gcash_qr_base64 = ""
                self.page.snack_bar = ft.SnackBar(ft.Text("The QR Code image is invalid"), duration=3000)
                self.page.snack_bar.open = True
                self.page.update()
                return
            
            qr = qrcode.QRCode(
                version = 1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size = 10,
                border = 4
            )
            
            qr.add_data(data)
            qr.make(fit=True)
            image = qr.make_image()
            self.qr_buffer = BytesIO()
            image.save(self.qr_buffer, format="JPEG")
            self.gcash_qr_base64 = base64.b64encode(self.qr_buffer.getvalue()).decode("utf-8")
            self.change_gcash_dialog.qr_image.src_base64 = self.gcash_qr_base64
            self.change_gcash_dialog.qr_image.update()
            self.gcash_changed()
        else:
            self.qr_image_path = ""
    
    def gcash_changed(self):
        pass

    def handle_save_changes_button(self):
        if self.gcash_qr_base64 != "" and len(self.change_gcash_dialog.number_textfield.value) == 11 and (self.change_gcash_dialog.number_textfield.value[:2] == "09" or self.change_gcash_dialog.number_textfield.value[:3] == "639"):
            self.change_gcash_dialog.save_changes_button.disabled = False
            self.change_gcash_dialog.save_changes_button.update()
        else:
            self.change_gcash_dialog.save_changes_button.disabled = True
            self.change_gcash_dialog.save_changes_button.update()
    
    def save_changed_gcash_infos(self, event: ft.ControlEvent):
        for user in self.repository.users:
            if user.email == self.email.replace(".", ","):
                id = self.repository.upload_image(f"{user.email}|QRCode.png", self.qr_buffer)
                user.qr_image_id = id
                user.gcash_number = self.change_gcash_dialog.number_textfield.value
                self.repository.update_user(user)
                self.home_page.close_dialog(event)
                
                return
        