from model import Model
from views import HomePage, AddReceivableDialog

import flet as ft
from PIL import Image
import io
import base64

class AddReceivableDialogController:
    image_path = ""
    def __init__(self, page: ft.Page, model: Model, home_page: HomePage):
        self.page = page
        self.model = model
        self.home_page = home_page
        self.add_receivable_dialog: AddReceivableDialog = home_page.add_receivable_dialog
        
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_item_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
        
        self.add_receivable_dialog.choose_button.on_click = self.open_chooser
        
        self.add_receivable_dialog.cancel_button.on_click = self.home_page.close_dialog
        
        self.add_receivable_dialog.item_name_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_month_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_day_textfield.on_change = self.item_info_change
        self.add_receivable_dialog.item_year_textfield.on_change = self.item_info_change
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
        group_name = self.add_receivable_dialog.group
        item_name = self.add_receivable_dialog.get_item_name()
        item_month = self.add_receivable_dialog.get_item_creation_month()
        item_day = self.add_receivable_dialog.get_item_creation_day()
        item_year = self.add_receivable_dialog.get_item_creation_year()
        item_date = f"{item_month} {item_day}, {item_year}"
        item_amount = self.add_receivable_dialog.get_item_amount()
        item_description = self.add_receivable_dialog.get_item_description()
        
        verdict = self.model.create_receivable(email, group_name, item_name, item_date, item_amount, item_description)
        if verdict == "Successful":
            self.home_page.close_dialog(event)
            
        if self.image_path != "":
            self.model.upload_item_image(group_name, item_name, self.image_path)
        
        self.model.update_refs()
        self.home_page.group_listview.items_view.on_trigger_reload(event)
    
    def item_info_change(self, event: ft.ControlEvent):
        if all([self.add_receivable_dialog.get_item_name() != "",
                self.add_receivable_dialog.get_item_creation_month() != "",
                self.add_receivable_dialog.get_item_creation_day() != "",
                self.add_receivable_dialog.get_item_creation_year() != "",
                self.add_receivable_dialog.get_item_amount() != "",
                self.add_receivable_dialog.get_item_description() != ""]):
            
            self.add_receivable_dialog.add_item_button.disabled = False
        else:
            self.add_receivable_dialog.add_item_button.disabled = True
        self.add_receivable_dialog.update()