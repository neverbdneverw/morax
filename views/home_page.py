import flet as ft
from flet_route import Params, Basket

from views.group_listview import GroupListView
from views.settings_view import SettingsView
from views.feedback_view import FeedbackView
from views.account_view import AccountView

from views.add_dialog import AddDialog
from views.item_info_dialog import ItemInfoDialog
from views.add_receivable_dialog import AddReceivableDialog
from views.show_receivable_info_dialog import ShowReceivableInfoDialog
from views.account_settings_dialogs import *
from views.settings_view_dialogs import *

class HomePage():
    def __init__(self):
        self.group_listview = GroupListView(self)
        self.settings_view = SettingsView()
        self.feedback_view = FeedbackView()
        self.account_view = AccountView()
        
        self.slider_stack = ft.Stack(
            expand=True,
            controls=[self.group_listview, self.settings_view, self.feedback_view, self.account_view]
        )
        
        content_area_row = ft.Row(
            expand = True,
            controls=[self.slider_stack]
        )
        
        content_area = ft.Column(
            expand=True,
            spacing=0,
            controls=[content_area_row]
        )
        
        logo = ft.Image(
            src = "/logo_filled.png",
            width=50,
            height=50
        )
        
        logo_row = ft.Row(
            controls=[logo],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.home_button = ft.IconButton(
            selected=True,
            icon=ft.icons.HOME_OUTLINED,
            selected_icon=ft.icons.HOME_FILLED,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle()
        )
        
        home_button_row = ft.Row(
            controls=[self.home_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.settings_button = ft.IconButton(
            selected=False,
            icon=ft.icons.SETTINGS_OUTLINED,
            selected_icon=ft.icons.SETTINGS,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle()
        )
        
        settings_button_row = ft.Row(
            controls=[self.settings_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.feedback_button = ft.IconButton(
            selected=False,
            icon=ft.icons.FEEDBACK_OUTLINED,
            selected_icon=ft.icons.FEEDBACK,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle(),
        )
        
        feedback_button_row = ft.Row(
            controls=[self.feedback_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.profile_button = ft.IconButton(
            selected=False,
            icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
            selected_icon=ft.icons.ACCOUNT_CIRCLE,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle()
        )
        
        profile_button_row = ft.Row(
            controls=[self.profile_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        profile_button_container = ft.Container(
            content=profile_button_row,
            padding=12.5
        )
        
        sidebar_top_column = ft.Column(
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            controls=[logo_row, home_button_row, settings_button_row, feedback_button_row]
        )
    
        sidebar = ft.Column(
            expand = True,
            width = 75,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            controls=[sidebar_top_column, profile_button_container]
        )
        
        self.sidebar_container = ft.Container(
            content=sidebar,
            padding=0
        )
        
        main_row = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                self.sidebar_container,
                ft.VerticalDivider(width=1),
                content_area]
        )

        self.route_address = "/home"
        self.view = ft.View(
            route = self.route_address,
            padding=0,
            controls = [main_row]
        )
        
        self.add_group_dialog = AddDialog()
        self.item_infos_dialog = ItemInfoDialog()
        self.add_receivable_dialog = AddReceivableDialog()
        self.receivable_info_dialog = ShowReceivableInfoDialog()
        
        self.change_profile_picture_dialog = ProfilePictureChangeDialog()
        self.edit_username_dialog = EditUsernameDialog()
        self.edit_password_dialog = EditPasswordDialog()
        self.edit_gcash_dialog = EditGcashDialog()
        
        self.appearance_dialog = AppearanceDialog()
        self.currency_dialog = CurrencyDialog()
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        self.email = self.page.client_storage.get("email")
        self.on_email_retrieved(self.email)
        return self.view
    
    def on_email_retrieved(self, email: str):
        pass
    
    def check_if_autologin(self):
        pass
    
    def trigger_reload_account_view(self):
        pass
    
    def show_add_group_dialog(self):
        self.page.dialog = self.add_group_dialog
        self.add_group_dialog.open = True
        self.page.update()
    
    def close_dialog(self, event: ft.ControlEvent):
        self.page.dialog.open = False
        self.page.update()
    
    def show_info_dialog(self):
        self.page.dialog = self.item_infos_dialog
        self.item_infos_dialog.open = True
        self.page.update()
        
    def show_add_receivable_dialog(self):
        self.page.dialog = self.add_receivable_dialog
        self.add_receivable_dialog.open = True
        self.page.update()
    
    def show_receivable_info_dialog(self):
        self.page.dialog = self.receivable_info_dialog
        self.receivable_info_dialog.open = True
        self.page.update()
    
    def show_profile_picture_change_dialog(self):
        self.page.dialog = self.change_profile_picture_dialog
        self.change_profile_picture_dialog.open = True
        self.page.update()
    
    def show_edit_username_dialog(self):
        self.page.dialog = self.edit_username_dialog
        self.edit_username_dialog.open = True
        self.page.update()
    
    def show_edit_password_dialog(self):
        self.page.dialog = self.edit_password_dialog
        self.edit_password_dialog.open = True
        self.page.update()
    
    def show_change_gcash_qr_dialog(self):
        self.page.dialog = self.edit_gcash_dialog
        self.edit_gcash_dialog.open = True
        self.page.update()
    
    def show_appearance_dialog(self):
        self.page.dialog = self.appearance_dialog
        self.appearance_dialog.open = True
        self.page.update()
    
    def show_currency_dialog(self):
        self.page.dialog = self.currency_dialog
        self.currency_dialog.open = True
        self.page.update()
    
    def update_colors(self, colors):
        self.home_button.style.color={"selected": colors["black"], "": colors["d6d6d6"]}
        self.settings_button.style.color={"selected": colors["black"], "": colors["d6d6d6"]}
        self.feedback_button.style.color={"selected": colors["black"], "": colors["d6d6d6"]}
        self.profile_button.style.color={"selected": colors["black"], "": colors["d6d6d6"]}
        
        self.sidebar_container.bgcolor = colors["white"]
        
        self.view.bgcolor = colors["f8fafc"]
        self.update_subviews(colors)
    
    def update_subviews(self, colors):
        pass
    
    def reapply_theme(self):
        pass