from controllers.Database import Database
from views.home_page import HomePage
import flet as ft

class ItemInfoDialogController:
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        self.item_info_dialog = home_page.item_infos_dialog
        
        self.item_info_dialog.cancel_button.on_click = self.home_page.close_dialog
        self.item_info_dialog.pay_button.on_click = self.show_payment_details
    
    def show_payment_details(self, event: ft.ControlEvent):
        if self.item_info_dialog.switcher.content == self.item_info_dialog.main_row:
            self.item_info_dialog.show_payment_details()
            self.item_info_dialog.title.visible = False
            self.item_info_dialog.pay_button.text = "Mark as paid"
            self.item_info_dialog.title.update()
            self.item_info_dialog.pay_button.update()
        else:
            self.start_payment()
    
    def start_payment(self):
        print("MAGBABAYAD!")