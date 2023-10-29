from controllers.Database import Database
from views.home_page import HomePage
import flet as ft

class HomeController:
    code_validated = False
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        
        self.home_page.home_button.on_click = self.buttons_change
        self.home_page.settings_button.on_click = self.buttons_change
        self.home_page.feedback_button.on_click = self.buttons_change
        self.home_page.profile_button.on_click = self.buttons_change
        self.home_page.on_email_retrieved = self.fill_groups
        
        self.sidebar_buttons = [
            self.home_page.home_button,
            self.home_page.settings_button,
            self.home_page.feedback_button,
            self.home_page.profile_button
        ]

    def fill_groups(self, email: str):
        self.database.update_refs()

        username = self.database.get_username_of_email(email)
        self.home_page.group_listview.top_text.value = f"Hi, {username}!"
        
        groups = self.database.get_groups_for_email(email)
        images = self.database.get_group_images_for_email(email)
        
        self.home_page.group_listview.setup_gui(groups, images)
        
        if self.page.client_storage.get("keep_signed_in") is True:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"You are automatically logged in."))
            self.page.snack_bar.open = True
            self.page.update()
        
        group_buttons = self.home_page.group_listview.grid.controls
        
        for button in group_buttons:
            button.activate = self.open_group
    
    def open_group(self, event: ft.ControlEvent):
        group = event.control.group_name
        
        if group == "Add":
            self.home_page.show_add_dialog()
        else:
            transactions = self.database.get_transactions(group)
            print(transactions)
    
    def buttons_change(self, event: ft.ControlEvent):
        new_button = event.control
        new_index = 0
        for index, button in enumerate(self.sidebar_buttons):
            if new_button == button:
                new_index = index
                button.selected = True
            else:
                button.selected = False
        
        for iter, view in enumerate(self.home_page.slider_stack.controls):
            view.show(iter - new_index)
        
        self.page.update()