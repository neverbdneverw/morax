from model import Model
from views import HomePage, ShowReceivableInfoDialog
from PIL import Image, ImageTk

import flet as ft
import tkinter as tk

class ReceivableInfoDialogController:
    def __init__(self, page: ft.Page, model: Model, home_page: HomePage):
        self.page = page
        self.model = model
        self.home_page = home_page
        self.receivable_info_dialog: ShowReceivableInfoDialog = home_page.receivable_info_dialog
        
        self.receivable_info_dialog.completed_button.on_click = self.mark_receivable_completed
        self.receivable_info_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        self.receivable_info_dialog.show_proof = self.show_proof
    
    def mark_receivable_completed(self, event: ft.ControlEvent):
        item_name = self.receivable_info_dialog.title.value
        group_name = self.receivable_info_dialog.group_name
        
        self.model.complete_transaction(group_name, item_name)
        
        self.home_page.close_dialog(event)
        
        self.home_page.group_listview.items_view.on_trigger_reload(event)
    
    def show_proof(self, picture_id: str):
        image = self.model.get_image_proof(picture_id)
        
        root = tk.Tk()
        root.title("PROOF OF PAYMENT")
        photo = ImageTk.PhotoImage(Image.open(image))
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack(ipadx= 20, pady=20)
        root.mainloop()