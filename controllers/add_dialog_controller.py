import flet as ft
from controllers.Database import Database
from PIL import Image
import io
import base64
from views.add_dialog import AddDialog
from views.home_page import HomePage

class AddDialogController:
    code_validated = False
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        self.add_dialog = home_page.add_dialog
        
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
    
        self.add_dialog.group_code_textfield.on_change = self.validate_group_code
        self.add_dialog.create_new_button.on_click = self.create_new
        self.add_dialog.join_button.on_click = self.join_group
        self.add_dialog.close_button.on_click = self.home_page.close_dialog
        self.add_dialog.group_name_textfield.on_change = self.validate_creation_params
        self.add_dialog.group_desc_textfield.on_change = self.validate_creation_params
        self.add_dialog.check_if_exists_button.on_click = self.check_if_code_exists
        self.add_dialog.image_upload_button.on_click = self.open_chooser
    
    def validate_group_code(self, event: ft.ControlEvent):
        if len(self.add_dialog.get_group_code_entry()) == 8:
            self.add_dialog.check_if_exists_button.disabled = False
        else:
            self.add_dialog.check_if_exists_button.disabled = True
        self.add_dialog.update()
    
    def create_new(self, event):
        if self.add_dialog.switcher.content == self.add_dialog.join_column:
            self.add_dialog.switch_to_creation()
            self.add_dialog.join_button.disabled = False
            
            if self.add_dialog.get_created_group_name() == "" and self.add_dialog.get_created_group_desc() == "":
                self.add_dialog.create_new_button.disabled = True
            
            self.page.update()
        else:
            if self.add_dialog.get_created_group_name() != "" and self.add_dialog.get_created_group_desc() != "":
                email = self.page.client_storage.get("email")
                self.database.create_group_with_email(self.add_dialog.get_created_group_name(), email)
                self.database.update_refs()
                self.home_page.group_listview.add_new_item(self.home_page.add_dialog.get_created_group_name(), self.new_image_string)
                self.database.upload_group_image(self.add_dialog.get_created_group_name(), self.image_path)
                self.home_page.close_dialog(None)
                self.new_image_string == ""
                
                self.page.update()
    
    def join_group(self, event):
        if self.add_dialog.switcher.content == self.add_dialog.creation_row:
            self.add_dialog.switch_to_joining()
            self.add_dialog.create_new_button.disabled = False
            
            if self.code_validated:
                self.add_dialog.join_button.disabled = False
            else:
                self.add_dialog.join_button.disabled = True
            
            self.page.update()
        
        else:
            if self.code_validated:
                email = self.page.client_storage.get("email")
                self.database.join_group_with_email(self.add_dialog.get_group_code_entry(), email)
                self.database.update_refs()
                group_name = self.database.get_group_by_code(self.add_dialog.get_group_code_entry())
                self.home_page.group_listview.add_new_item(group_name, self.database.get_group_image(group_name))
                self.home_page.close_dialog(None)
                self.page.update()
    
    def validate_creation_params(self, event):
        if self.add_dialog.get_created_group_desc() != "" and self.add_dialog.get_created_group_name() != "":
            self.add_dialog.create_new_button.disabled = False
        else:
            self.add_dialog.create_new_button.disabled = True

        self.page.update()
    
    def check_if_code_exists(self, event):
        code = self.add_dialog.get_group_code_entry()
        if code != "":
            exists = self.database.is_group_existing(code)
            
            if exists:
                print("Code existsing. pede na magjoin yiee")
                self.code_validated = True
                self.add_dialog.join_button.disabled = False
            else:
                print("Nothing like that exists")
                self.code_validated = False
                self.add_dialog.join_button.disabled = True
            
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
            self.home_page.add_dialog.image_preview.src_base64 = self.new_image_string
            self.home_page.add_dialog.image_preview.update()
        else:
            self.image_path = ""