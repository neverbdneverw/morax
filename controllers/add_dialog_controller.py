from models import Group, Member
from repository import Repository, utils
from views import AddDialog, HomePage

from PIL import Image

import flet as ft
import io
import base64

class AddDialogController:
    code_validated = False
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
        self.home_page = home_page
        self.add_group_dialog: AddDialog = home_page.add_group_dialog
        
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
    
        self.add_group_dialog.group_code_textfield.on_change = self.validate_group_code
        self.add_group_dialog.create_new_button.on_click = self.create_new
        self.add_group_dialog.join_button.on_click = self.join_group
        self.add_group_dialog.close_button.on_click = self.home_page.close_dialog
        self.add_group_dialog.group_name_textfield.on_change = self.validate_creation_params
        self.add_group_dialog.group_desc_textfield.on_change = self.validate_creation_params
        self.add_group_dialog.check_if_exists_button.on_click = self.check_if_code_exists
        self.add_group_dialog.image_upload_button.on_click = self.open_chooser
    
    def validate_group_code(self, event: ft.ControlEvent):
        if len(self.add_group_dialog.get_group_code_entry()) == 8:
            self.add_group_dialog.check_if_exists_button.disabled = False
        else:
            self.add_group_dialog.check_if_exists_button.disabled = True
        self.add_group_dialog.update()
    
    def create_new(self, event):
        if self.add_group_dialog.switcher.content == self.add_group_dialog.join_column:
            self.add_group_dialog.switch_to_creation()
            self.add_group_dialog.join_button.disabled = False
            
            if self.add_group_dialog.get_created_group_name() == "" and self.add_group_dialog.get_created_group_desc() == "":
                self.add_group_dialog.create_new_button.disabled = True
            
            self.page.update()
        else:
            if self.add_group_dialog.get_created_group_name() != "" and self.add_group_dialog.get_created_group_desc() != "":
                email: str = self.page.client_storage.get("email")
                
                creator = ""
                for user in self.repository.users:
                    if user.email == email.replace(".", "."):
                        creator = user.username
                        break
                    
                image_bytes = io.BytesIO()
                image = Image.open(self.image_path).convert("RGBA")
                image = image.resize((200, 200))
                image.save(image_bytes, format="PNG")
                
                empty_list = list()
                unique_code = utils.generate_unique_code()
                
                group_image_id = self.repository.upload_image(f"{self.add_group_dialog.get_created_group_name()}.png", image_bytes)
                
                new_group = Group(
                    group_name=self.add_group_dialog.get_created_group_name(),
                    created_by=creator,
                    description=self.add_group_dialog.get_created_group_desc(),
                    members=[Member(creator, email)],
                    picture_id=group_image_id,
                    unique_code=unique_code,
                    transactions=empty_list
                )
                
                self.repository.update_group(new_group)
                self.page.client_storage.set("just_opened", False)
                self.home_page.group_listview.trigger_reload(email)
                self.home_page.close_dialog(None)
                self.new_image_string == ""
                
                self.page.update()
    
    def join_group(self, event):
        if self.add_group_dialog.switcher.content == self.add_group_dialog.creation_row:
            self.add_group_dialog.switch_to_joining()
            self.add_group_dialog.create_new_button.disabled = False
            
            if self.code_validated:
                self.add_group_dialog.join_button.disabled = False
            else:
                self.add_group_dialog.join_button.disabled = True
            
            self.page.update()
        
        else:
            if self.code_validated:
                email = str(self.page.client_storage.get("email")).replace(".", ",")
                
                username = ""
                for user in self.repository.users:
                    if user.email == email:
                        username = user.username
                
                for group in self.repository.groups:
                    if group.unique_code == self.add_group_dialog.get_group_code_entry():
                        group.members.append(Member(username, email))

                        self.repository.update_group(group)
                
                        self.page.client_storage.set("just_opened", False)
                        self.home_page.group_listview.trigger_reload(email)
                        self.home_page.close_dialog(None)
                        self.page.update()
    
    def validate_creation_params(self, event):
        if self.add_group_dialog.get_created_group_desc() != "" and self.add_group_dialog.get_created_group_name() != "":
            self.add_group_dialog.create_new_button.disabled = False
        else:
            self.add_group_dialog.create_new_button.disabled = True

        self.page.update()
    
    def check_if_code_exists(self, event):
        code = self.add_group_dialog.get_group_code_entry()
        if code != "":
            exists = False
            for group in self.repository.groups:
                if code == group.unique_code:
                    exists = True
                    break
            
            if exists:
                self.page.snack_bar = ft.SnackBar(ft.Text("The group code is valid. You may now join..."), duration=3000)
                self.page.snack_bar.open = True
                self.page.update()
                self.code_validated = True
                self.add_group_dialog.join_button.disabled = False
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("The group code is invalid. Please try again..."), duration=3000)
                self.page.snack_bar.open = True
                self.page.update()
                self.code_validated = False
                self.add_group_dialog.join_button.disabled = True
            
            self.page.update()
    
    def open_chooser(self, event):
        self.file_picker.pick_files("Choose Group Image", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)
    
    def set_image(self, event: ft.FilePickerResultEvent):
        if event.files is not None:
            self.image_path = event.files[0].path
            image = Image.open(self.image_path).convert("RGBA")
            pil_img = image.resize((200, 200))
            buff = io.BytesIO()
            pil_img.save(buff, format="PNG")
            
            self.new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            self.add_group_dialog.image_preview.src_base64 = self.new_image_string
            self.add_group_dialog.image_preview.update()
        else:
            self.image_path = ""