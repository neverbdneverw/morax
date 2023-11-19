from controllers.Database import Database
from views.home_page import HomePage
import flet as ft
import webbrowser

import tkinter as tk
from PIL import Image, ImageTk

class HomeController:
    code_validated = False
    image_path = ""
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        self.group_listview = self.home_page.group_listview
        
        self.home_page.home_button.on_click = self.buttons_change
        self.home_page.settings_button.on_click = self.buttons_change
        self.home_page.feedback_button.on_click = self.buttons_change
        self.home_page.profile_button.on_click = self.buttons_change
        self.home_page.group_listview.items_view.return_button.on_click = self.return_to_grid
        self.home_page.group_listview.items_view.reload_button.on_click = self.reload_listview
        self.home_page.group_listview.items_view.receivables_button.on_click = self.show_receivables
        self.home_page.group_listview.items_view.add_receivable_button.on_click = self.open_receivable_adding_dialog
        self.home_page.group_listview.items_view.on_trigger_reload = lambda event: self.reload_listview(event)
        self.home_page.group_listview.trigger_reload = self.reload_groups
        self.home_page.on_email_retrieved = self.fill_groups
        
        self.home_page.receivable_info_dialog.completed_button.on_click = self.mark_receivable_completed
        self.home_page.receivable_info_dialog.cancel_button.on_click = lambda e: self.home_page.close_dialog(e)
        self.home_page.receivable_info_dialog.show_proof = self.show_proof
        
        self.sidebar_buttons = [
            self.home_page.home_button,
            self.home_page.settings_button,
            self.home_page.feedback_button,
            self.home_page.profile_button
        ]
        
        self.home_page.feedback_view.button_contact_us.on_click = lambda e: webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcRzCMtQddshVRjPCKJRGfFwDxvWqJcNftmXFMFqqpdvrXXBpGsrfGGNTnSswPqHpChKdBRJG")
        self.home_page.feedback_view.button_contribute.on_click = lambda e: webbrowser.open_new("https://github.com/neverbdneverw/morax/issues/new")
    
    def reload_groups(self, email: str):
        self.home_page.group_listview.grid.controls = []
        self.home_page.group_listview.update()
        self.fill_groups(email)

    def fill_groups(self, email: str):
        self.database.update_refs()

        username = self.database.get_username_of_email(email)
        self.home_page.group_listview.top_text.value = f"Hi, {username}!"
        
        groups = self.database.get_groups_for_email(email)
        images = self.database.get_group_images_for_email(email)
        
        self.home_page.group_listview.setup_gui(groups, images)
        
        if self.page.client_storage.get("keep_signed_in") is True and self.page.client_storage.get("recent_set_keep_signed_in") is False and self.page.client_storage.get("just_opened") is True:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"You are automatically logged in."))
            self.page.snack_bar.open = True
            self.page.update()
        elif self.page.client_storage.get("recent_set_keep_signed_in") is True:
            self.page.client_storage.set("recent_set_keep_signed_in", False)
            self.page.client_storage.set("just_opened", True)
        
        group_buttons = self.home_page.group_listview.grid.controls
        
        for button in group_buttons:
            button.activate = self.open_group
    
    def open_group(self, group: str, image_string: str):
        if group == "Add":
            self.home_page.show_add_group_dialog()
        else:
            self.database.update_refs()
            transactions = self.database.get_transactions(group)
            item_images = self.database.get_item_images_for_group(group)
            
            email = self.page.client_storage.get("email")
            current_user = self.database.get_username_of_email(email)
            user_image = self.database.get_user_image(email)
            
            self.home_page.group_listview.items_view.group_name.value = self.home_page.group_listview.items_view.group_name_text.value = group
            self.home_page.group_listview.items_view.group_description.value = self.database.get_group_description(group)
            self.home_page.group_listview.items_view.username.value = current_user
            self.home_page.group_listview.items_view.set_creator(self.database.get_group_creator(group))
            self.home_page.group_listview.items_view.set_user_image(user_image)
            self.home_page.group_listview.content = self.home_page.group_listview.items_view
            self.home_page.group_listview.items_view.display_transactions(email, group, image_string, transactions, item_images)
            self.home_page.group_listview.update()
            
            for payable_button in self.home_page.group_listview.items_view.payable_list.controls:
                payable_button.activate = self.show_item_informations
            
            for receivable_button in self.home_page.group_listview.items_view.receivable_list.controls:
                receivable_button.activate = self.show_receivable_info
    
    def reload_listview(self, event: ft.ControlEvent):
        self.database.update_refs()
        group_name = self.group_listview.items_view.group_name.value
        image_string = self.group_listview.items_view.group_image.src_base64
        
        self.group_listview.items_view.payable_list.controls = []
        self.group_listview.items_view.receivable_list.controls = []
        self.page.snack_bar = ft.SnackBar(ft.Text(f"Reloading items..."), duration=3000)
        self.page.snack_bar.open = True
        self.page.update()
        self.open_group(group_name, image_string)
    
    def return_to_grid(self, event: ft.ControlEvent):
        self.home_page.group_listview.items_view.payable_list.controls = []
        self.home_page.group_listview.items_view.receivable_list.controls = []
    
        self.home_page.group_listview.content = self.home_page.group_listview.grid_view
        self.home_page.group_listview.update()
    
    def show_item_informations(self, event: ft.ControlEvent, group: str, item_name: str, item_informations: dict):
        self.home_page.item_infos_dialog.load_infos(event.control, item_name, item_informations)
        self.home_page.show_info_dialog()
    
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
    
    def show_receivables(self, event: ft.ControlEvent):
        if self.home_page.group_listview.items_view.list_switcher.content == self.home_page.group_listview.items_view.payable_column:
            self.home_page.group_listview.items_view.receivables_button.text = "My Payables"
            self.home_page.group_listview.items_view.list_switcher.content = self.home_page.group_listview.items_view.receivable_column
        else:
            self.home_page.group_listview.items_view.receivables_button.text = "My Receivables"
            self.home_page.group_listview.items_view.list_switcher.content = self.home_page.group_listview.items_view.payable_column
        
        if self.home_page.group_listview.items_view.add_receivable_button not in self.home_page.group_listview.items_view.receivable_list.controls:
            self.home_page.group_listview.items_view.receivable_list.controls.append(self.home_page.group_listview.items_view.add_receivable_button)
        
        self.home_page.group_listview.items_view.receivables_button.update()
        self.home_page.group_listview.items_view.list_switcher.update()
    
    def open_receivable_adding_dialog(self, event: ft.ControlEvent):
        self.home_page.add_receivable_dialog.group = self.home_page.group_listview.items_view.group_name.value
        self.home_page.show_add_receivable_dialog()
    
    def show_receivable_info(self, event: ft.ControlEvent, group: str, item_name: str, item_informations: dict):
        self.home_page.receivable_info_dialog.title.value = item_name
        self.home_page.receivable_info_dialog.group_name = group
        self.home_page.receivable_info_dialog.show_who_paid(item_informations)
        self.home_page.show_receivable_info_dialog()
    
    def mark_receivable_completed(self, event: ft.ControlEvent):
        item_name = self.home_page.receivable_info_dialog.title.value
        group_name = self.home_page.receivable_info_dialog.group_name
        
        self.database.complete_transaction(group_name, item_name)
        
        self.home_page.close_dialog(event)
        
        self.home_page.group_listview.items_view.on_trigger_reload(event)
    
    def show_proof(self, picture_id: str):
        image = self.database.get_image_proof(picture_id)
        
        root = tk.Tk()
        root.title("PROOF OF PAYMENT")
        photo = ImageTk.PhotoImage(Image.open(image))
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack(ipadx= 20, pady=20)
        root.mainloop()
        