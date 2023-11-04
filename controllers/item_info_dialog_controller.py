from controllers.Database import Database
from views.home_page import HomePage
import flet as ft
from PIL import Image
import io
import base64

class ItemInfoDialogController:
    image_path = ""
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        self.item_info_dialog = home_page.item_infos_dialog
        
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_proof_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
        
        self.item_info_dialog.upload_proof_button.on_click = self.open_chooser
        
        self.item_info_dialog.cancel_button.on_click = self.home_page.close_dialog
        self.item_info_dialog.pay_button.on_click = self.show_payment_details
    
    def open_chooser(self, event: ft.ControlEvent):
        self.file_picker.pick_files("Choose Image proof", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)
    
    def show_payment_details(self, event: ft.ControlEvent):
        if self.item_info_dialog.switcher.content == self.item_info_dialog.main_row:
            self.item_info_dialog.show_payment_details()
            self.item_info_dialog.pay_button.text = "Mark as paid"
            self.item_info_dialog.pay_button.update()
        elif self.item_info_dialog.switcher.content == self.item_info_dialog.payment_row:
            self.item_info_dialog.switcher.content = self.item_info_dialog.proof_column
            self.item_info_dialog.switcher.update()
        else:
            self.item_info_dialog.pay_button.disabled = True
            
            group_name = event.control.group_name
            current_email = self.page.client_storage.get("email")
            item_name = self.item_info_dialog.item_name.value
            
            verdict = self.database.mark_paid_with_proof(group_name, item_name, current_email, self.image_path)
            if verdict == "Successful":
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Your payable is marked as paid."), duration=1000)
                self.page.snack_bar.open = True
                self.home_page.group_listview.items_view.on_trigger_reload(event)
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Your payable cannot be marked as paid."), duration=1000)
                self.page.snack_bar.open = True

            self.item_info_dialog.open = False
            self.page.update()
    
    def set_proof_image(self, event: ft.FilePickerResultEvent):
        if event.files is not None:
            self.image_path = event.files[0].path
            image = Image.open(self.image_path).convert("RGBA")
            pil_img = image.resize((200, 200))
            buff = io.BytesIO()
            pil_img.save(buff, format="PNG")
            
            self.new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            self.item_info_dialog.payment_preview_image.src_base64 = self.new_image_string
            self.item_info_dialog.payment_preview_image.update()
            self.item_info_dialog.pay_button.disabled = False
            self.item_info_dialog.pay_button.update()
        else:
            self.image_path = ""