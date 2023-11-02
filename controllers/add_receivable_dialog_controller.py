import flet as ft
from controllers.Database import Database
from PIL import Image
import io
import base64
from views.add_dialog import AddDialog
from views.home_page import HomePage

class AddReceivableDialogController:
    image_path = ""
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        self.add_receivable_dialog = home_page.add_receivable_dialog
        
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_item_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
        
        self.add_receivable_dialog.choose_button.on_click = self.open_chooser
        
        self.add_receivable_dialog.cancel_button.on_click = self.home_page.close_dialog
        
        self.add_receivable_dialog.item_name_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_date_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_amount_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_description_textfield.on_change = self.item_info_change
        
        self.add_receivable_dialog.add_item_button.on_click = self.add_receivable
    
    def open_chooser(self, event: ft.ControlEvent):
        self.file_picker.pick_files("Choose Item Image", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)
    
    def set_item_image(self, event: ft.FilePickerResultEvent):
        if event.files is not None:
            self.image_path = event.files[0].path
            image = Image.open(self.image_path).convert("RGBA")
            pil_img = image.resize((200, 200))
            buff = io.BytesIO()
            pil_img.save(buff, format="PNG")
            
            self.new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            self.add_receivable_dialog.item_image.src_base64 = self.new_image_string
            self.add_receivable_dialog.item_image.update()
        else:
            self.image_path = ""

    def add_receivable(self, event: ft.ControlEvent):
        email = self.page.client_storage.get("email")
        group_name = self.home_page.add_receivable_dialog.group
        item_name = self.add_receivable_dialog.get_item_name()
        item_date = self.add_receivable_dialog.get_item_creation_date()
        item_amount = self.add_receivable_dialog.get_item_amount()
        item_description = self.add_receivable_dialog.get_item_description()
        
        verdict = self.database.create_receivable(email, group_name, item_name, item_date, item_amount, item_description)
        if verdict == "Successful":
            self.home_page.close_dialog(event)
            
        if self.image_path != "":
            self.database.upload_item_image(group_name, item_name, self.image_path)
        
        self.database.update_refs()
        self.home_page.group_listview.items_view.on_trigger_reload(event)
        # self.reload_listview(event)
    
    def item_info_change(self, event: ft.ControlEvent):
        if self.add_receivable_dialog.get_item_name() != "" and self.add_receivable_dialog.get_item_creation_date() != "" and self.add_receivable_dialog.get_item_amount() != "" and self.add_receivable_dialog.get_item_description() != "":
            self.add_receivable_dialog.add_item_button.disabled = False
        else:
            self.add_receivable_dialog.add_item_button.disabled = True
        self.add_receivable_dialog.update()