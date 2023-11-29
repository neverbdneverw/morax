import flet as ft

from repository import Repository
from views import HomePage

class AppearanceDialogController:
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
        self.home_page = home_page
        self.appearance_dialog = home_page.appearance_dialog
        
        self.home_page.settings_view.appearance_setting.on_click = self.handle_dialog_open
        
        self.appearance_dialog.on_change = self.change_darkmode
    
    def change_darkmode(self, event: ft.ControlEvent):
        if event.data == "true":
            self.page.client_storage.set("dark_mode", True)
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.client_storage.set("dark_mode", False)
            self.page.theme_mode = ft.ThemeMode.LIGHT
        
        self.page.update()
    
    def handle_dialog_open(self, event):
        self.appearance_dialog.dark_mode_switch.value = bool(self.page.client_storage.get("dark_mode"))
        self.home_page.show_appearance_dialog()

class CurrencyDialogController:
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
        self.home_page = home_page
        self.currency_dialog = home_page.currency_dialog
        
        self.home_page.settings_view.currency_setting.on_click = self.handle_dialog_open
        self.currency_dialog.on_change = self.change_currency
    
    def change_currency(self, currency):
        self.page.client_storage.set("currency", currency)
        self.page.snack_bar = ft.SnackBar(ft.Text("A reload inside group view is required for the change to take effect..."))
        self.page.snack_bar.open = True
        self.page.update()
    
    def handle_dialog_open(self, event: ft.ControlEvent):
        self.currency_dialog.currency_choices.value = self.page.client_storage.get("currency")
        self.home_page.show_currency_dialog()