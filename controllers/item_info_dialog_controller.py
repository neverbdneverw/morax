from models import Transaction
from repository import Repository
from views import HomePage

from PIL import Image

import flet as ft
import io
import base64

# Initialize the Payable Info Dialog
class ItemInfoDialogController:
    image_path = ""
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
        self.home_page = home_page
        self.item_info_dialog = home_page.item_infos_dialog
        
        # Initialize the file picker
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.set_proof_image
        self.page.overlay.append(self.file_picker)
        self.page.update()
        
        # handle events
        self.item_info_dialog.upload_proof_button.on_click = self.open_chooser
        
        self.item_info_dialog.cancel_button.on_click = self.reset_button_states
        self.item_info_dialog.pay_button.on_click = self.show_payment_details
    
    # reset the buttons after reopening
    def reset_button_states(self, event: ft.ControlEvent):
        self.item_info_dialog.pay_button.disabled = False
        self.item_info_dialog.pay_button.update()
        self.home_page.close_dialog(event)
    
    # opent the file chooser
    def open_chooser(self, event: ft.ControlEvent):
        self.file_picker.pick_files("Choose Image proof", allowed_extensions = ["png", "jpg", "jpeg", "PNG", "JPG"], file_type = ft.FilePickerFileType.CUSTOM)
    
    # show the payment details 
    def show_payment_details(self, event: ft.ControlEvent):
        if self.item_info_dialog.switcher.content == self.item_info_dialog.main_row:
            # show the infos of the payable
            self.item_info_dialog.show_payment_details()
            self.item_info_dialog.pay_button.text = "Mark as paid"
            self.item_info_dialog.pay_button.update()
        elif self.item_info_dialog.switcher.content == self.item_info_dialog.payment_row:
            # show the infos of the payment details
            self.item_info_dialog.switcher.content = self.item_info_dialog.proof_column
            self.item_info_dialog.switcher.update()
            self.item_info_dialog.pay_button.disabled = True
            self.item_info_dialog.pay_button.update()
        else:
            # show the payment request page
            group_name = self.item_info_dialog.group_name
            current_email = self.page.client_storage.get("email")
            item_name = self.item_info_dialog.item_name.value
            
            self.item_info_dialog.open = False
            self.page.update()
            
            image_bytes = io.BytesIO()
            image = Image.open(self.image_path).convert("RGBA")
            image = image.resize((200, 200))
            image.save(image_bytes, format="PNG")
            
            paid_proof_id = self.repository.upload_image(f"PROOF|{group_name}|{item_name}.png", image_bytes)
            
            for group in self.repository.groups:
                if group.group_name == group_name:
                    transaction: Transaction = None
                    for transaction in group.transactions:
                        if transaction.name == item_name:
                            list(transaction.paid_by).append((current_email, paid_proof_id))
                            
                            if type(transaction.paid_by) is list:
                                transaction.paid_by.append(set(current_email, paid_proof_id))
                            else:
                                transaction.paid_by = [(current_email, paid_proof_id)]
                            
                            self.repository.update_group(group)
                            self.page.snack_bar = ft.SnackBar(ft.Text(f"Your payable is marked as paid."), duration=1000)
                            self.page.snack_bar.open = True

                            self.home_page.group_listview.items_view.on_trigger_reload(event)
                            
                            return
    
    # upload the proof
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