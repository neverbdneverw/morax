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
        self.home_page.item_infos_dialog.show_payment_details()
        self.home_page.item_infos_dialog.title.visible = False
        self.home_page.item_infos_dialog.pay_button.text = "Mark as paid"
        self.home_page.item_infos_dialog.title.update()
        self.home_page.item_infos_dialog.pay_button.update()