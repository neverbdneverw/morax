from controllers.Database import Database
from views.home_page import HomePage
import flet as ft
from flet_route import Basket

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

        self.home_page.add_dialog.group_code_textfield.on_change = self.validate_group_code
        self.home_page.add_dialog.create_new_button.on_click = self.create_new
        self.home_page.add_dialog.join_button.on_click = self.join_group
        self.home_page.add_dialog.close_button.on_click = self.home_page.add_dialog.close_dialog
        self.home_page.add_dialog.group_name_textfield.on_change = self.validate_creation_params
        self.home_page.add_dialog.group_desc_textfield.on_change = self.validate_creation_params
        self.home_page.add_dialog.check_if_exists_button.on_click = self.check_if_code_exists
    
    def validate_creation_params(self, event):
        if self.home_page.add_dialog.get_created_group_desc() != "" and self.home_page.add_dialog.get_created_group_name() != "":
            self.home_page.add_dialog.create_new_button.disabled = False
        else:
            self.home_page.add_dialog.create_new_button.disabled = True

        self.page.update()
    
    def check_if_code_exists(self, event):
        code = self.home_page.add_dialog.get_group_code_entry()
        if code != "":
            exists = self.database.is_group_existing(code)
            
            if exists:
                print("Code existsing. pede na magjoin yiee")
                self.code_validated = True
                self.home_page.add_dialog.join_button.disabled = False
            else:
                print("Nothing like that exists")
                self.code_validated = False
                self.home_page.add_dialog.join_button.disabled = True
            
            self.page.update()
    
    def create_new(self, event):
        if self.home_page.add_dialog.switcher.content == self.home_page.add_dialog.join_column:
            self.home_page.add_dialog.switch_to_creation()
            self.home_page.add_dialog.join_button.disabled = False
            
            if self.home_page.add_dialog.get_created_group_name() == "" and self.home_page.add_dialog.get_created_group_desc() == "":
                self.home_page.add_dialog.create_new_button.disabled = True
            
            self.page.update()
        else:
            if self.home_page.add_dialog.get_created_group_name() != "" and self.home_page.add_dialog.get_created_group_desc() != "":
                print("HAHAHAHAHAH")
    
    def join_group(self, event):
        if self.home_page.add_dialog.switcher.content == self.home_page.add_dialog.creation_row:
            self.home_page.add_dialog.switch_to_joining()
            self.home_page.add_dialog.create_new_button.disabled = False
            
            if self.code_validated:
                self.home_page.add_dialog.join_button.disabled = False
            else:
                self.home_page.add_dialog.join_button.disabled = True
            
            self.page.update()
        
        else:
            if self.code_validated:
                print("YES NAMAN PAPASA NA!")
    
    def fill_groups(self, email: str):
        self.database.update_refs()

        username = self.database.get_username_of_email(email)
        self.home_page.group_listview.top_text.value = f"Hi, {username}!"
        
        groups = self.database.get_groups_for_email(email)
        
        self.home_page.group_listview.setup_gui(groups)
        
        if self.page.client_storage.get("keep_signed_in") is True:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"You are automatically logged in."))
            self.page.snack_bar.open = True
            self.page.update()
        
        group_buttons = self.home_page.group_listview.grid.controls
        
        for button in group_buttons:
            button.activate = self.open_group
    
    def validate_group_code(self, event: ft.ControlEvent):
        if len(self.home_page.add_dialog.get_group_code_entry()) == 8:
            self.home_page.add_dialog.check_if_exists_button.disabled = False
        else:
            self.home_page.add_dialog.check_if_exists_button.disabled = True
        self.home_page.add_dialog.update()
    
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