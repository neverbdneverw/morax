from model import Model
from views import HomePage, GroupListView, FeedbackView, AccountView, ItemsView, GroupButton, ItemButton

import flet as ft
import webbrowser

class HomeController:
    code_validated = False
    image_path = ""
    def __init__(self, page: ft.Page, model: Model, home_page: HomePage):
        self.page = page
        self.model = model
        self.home_page = home_page
        
        self.group_listview: GroupListView = self.home_page.group_listview
        self.feedback_view: FeedbackView = self.home_page.feedback_view
        self.account_view: AccountView = self.home_page.account_view
        
        self.items_view: ItemsView = self.group_listview.items_view
        
        self.home_page.home_button.on_click = self.location_change
        self.home_page.settings_button.on_click = self.location_change
        self.home_page.feedback_button.on_click = self.location_change
        self.home_page.profile_button.on_click = self.location_change
        
        self.items_view.return_button.on_click = self.return_to_grid
        self.items_view.reload_button.on_click = self.reload_listview
        self.items_view.receivables_button.on_click = self.show_receivables
        self.items_view.add_receivable_button.on_click = self.open_receivable_adding_dialog
        
        self.items_view.on_trigger_reload = self.reload_listview
        self.group_listview.trigger_reload = self.reload_groups
        
        self.home_page.on_email_retrieved = self.fill_groups
        self.home_page.trigger_reload_account_view = self.update_account_view
        
        self.sidebar_buttons = [
            self.home_page.home_button,
            self.home_page.settings_button,
            self.home_page.feedback_button,
            self.home_page.profile_button
        ]
        
        self.feedback_view.button_contact_us.on_click = lambda e: webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcRzCMtQddshVRjPCKJRGfFwDxvWqJcNftmXFMFqqpdvrXXBpGsrfGGNTnSswPqHpChKdBRJG")
        self.feedback_view.button_contribute.on_click = lambda e: webbrowser.open_new("https://github.com/neverbdneverw/morax/issues/new")
        
        self.account_view.logout_button.on_click = lambda e: self.page.go("/login")
    
    def reload_groups(self, email: str):
        self.group_listview.grid.controls = []
        self.group_listview.update()
        self.fill_groups(email)

    def fill_groups(self, email: str):
        self.model.update_refs()

        username = self.model.get_username_of_email(email)
        self.group_listview.top_text.value = f"Hi, {username}!"
        
        groups = self.model.get_groups_for_email(email)
        images = self.model.get_group_images_for_email(email)
        
        self.group_listview.setup_gui(groups, images)
        
        if self.page.client_storage.get("keep_signed_in") is True and self.page.client_storage.get("recent_set_keep_signed_in") is False and self.page.client_storage.get("just_opened") is True:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"You are automatically logged in."))
            self.page.snack_bar.open = True
            self.page.update()
        elif self.page.client_storage.get("recent_set_keep_signed_in") is True:
            self.page.client_storage.set("recent_set_keep_signed_in", False)
            self.page.client_storage.set("just_opened", True)
        
        for button in self.group_listview.grid.controls:
            button: GroupButton  = button
            button.activate = self.open_group
    
    def open_group(self, group: str, image_string: str):
        if group == "Add":
            self.home_page.show_add_group_dialog()
        else:
            self.model.update_refs()
            transactions = self.model.get_transactions(group)
            item_images = self.model.get_item_images_for_group(group)
            usernames = self.model.get_usernames()
            user_images = self.model.get_user_images()
            gcash_infos = self.model.get_gcash_credentials()
            
            email = self.page.client_storage.get("email")
            current_user = self.model.get_username_of_email(email)
            user_image = self.model.get_user_image(email)
            
            self.items_view.group_name.value = self.items_view.group_name_text.value = group
            self.items_view.group_description.value = self.model.get_group_description(group)
            self.items_view.username.value = current_user
            self.items_view.set_creator(self.model.get_group_creator(group))
            self.items_view.set_user_image(user_image)
            self.items_view.display_transactions(email, group, image_string, transactions, item_images, usernames, user_images)

            self.group_listview.content = self.items_view
            self.group_listview.update()
            
            for payable_button in self.items_view.payable_list.controls:
                payable_button: ItemButton = payable_button
                payable_button.gcash_infos = gcash_infos
                payable_button.activate = self.show_item_informations
            
            for receivable_button in self.items_view.receivable_list.controls:
                receivable_button: ItemButton = receivable_button
                receivable_button.gcash_infos = gcash_infos
                receivable_button.activate = self.show_receivable_info
    
    def reload_listview(self, event: ft.ControlEvent):
        group_name = self.items_view.group_name.value
        image_string = self.items_view.group_image.src_base64
        
        self.items_view.payable_list.controls = []
        self.items_view.receivable_list.controls = []
        self.page.snack_bar = ft.SnackBar(ft.Text(f"Reloading items..."), duration=3000)
        self.page.snack_bar.open = True
        self.page.update()
        self.open_group(group_name, image_string)
    
    def return_to_grid(self, event: ft.ControlEvent):
        self.items_view.payable_list.controls = []
        self.items_view.receivable_list.controls = []
    
        self.group_listview.content = self.group_listview.grid_view
        self.group_listview.update()
    
    def show_item_informations(self, event: ft.ControlEvent, group: str, item_name: str, item_informations: dict):
        usernames = self.model.get_usernames()
        self.home_page.item_infos_dialog.load_infos(event.control, item_name, item_informations, usernames)
        self.home_page.show_info_dialog()
    
    def location_change(self, event: ft.ControlEvent):
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
            
        if new_button == self.home_page.profile_button:
            self.update_account_view()
        
        self.page.update()
    
    def show_receivables(self, event: ft.ControlEvent):
        if self.items_view.list_switcher.content == self.items_view.payable_column:
            self.items_view.receivables_button.text = "My Payables"
            self.items_view.list_switcher.content = self.items_view.receivable_column
        else:
            self.items_view.receivables_button.text = "My Receivables"
            self.items_view.list_switcher.content = self.items_view.payable_column
        
        if self.items_view.add_receivable_button not in self.items_view.receivable_list.controls:
            self.items_view.receivable_list.controls.append(self.items_view.add_receivable_button)
        
        self.items_view.receivables_button.update()
        self.items_view.list_switcher.update()
    
    def open_receivable_adding_dialog(self, event: ft.ControlEvent):
        self.home_page.add_receivable_dialog.group = self.items_view.group_name.value
        self.home_page.show_add_receivable_dialog()
    
    def show_receivable_info(self, event: ft.ControlEvent, group: str, item_name: str, item_informations: dict):
        self.home_page.receivable_info_dialog.title.value = item_name
        self.home_page.receivable_info_dialog.group_name = group
        self.home_page.receivable_info_dialog.show_who_paid(item_informations)
        self.home_page.show_receivable_info_dialog()
    
    def update_account_view(self):
        email = self.page.client_storage.get("email")
        user_image = self.model.get_user_image(email)
        self.account_view.user_picture.src_base64 = user_image
        self.account_view.username_text.value = self.model.get_username_of_email(email)
        self.account_view.email_text.value = email