from models import Member, Group, User, Transaction
from repository import Repository, utils
from views import HomePage, GroupListView, FeedbackView, AccountView, ItemsView, GroupButton, ItemButton, AddGroupButton

import flet as ft
import webbrowser

class HomeController:
    code_validated = False
    image_path = ""
    def __init__(self, page: ft.Page, repository: Repository, home_page: HomePage):
        self.page = page
        self.repository = repository
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
        
        self.account_view.logout_button.on_click = self.logout_account
    
    def logout_account(self, event: ft.ControlEvent):
        self.page.client_storage.set("keep_signed_in", False)
        self.page.client_storage.set("recent_set_keep_signed_in", False)
        self.group_listview.grid.controls = []
        self.page.go("/login")
    
    def reload_groups(self, email: str):
        self.group_listview.grid.controls = []
        self.group_listview.update()
        self.fill_groups(email)

    def fill_groups(self, email: str):
        email = email.replace(".", ",")
        self.repository.update_refs()
        
        if self.page.client_storage.get("keep_signed_in") is True and self.page.client_storage.get("recent_set_keep_signed_in") is False and self.page.client_storage.get("just_opened") is True:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"You are automatically logged in."))
            self.page.snack_bar.open = True
            self.page.update()
        elif self.page.client_storage.get("recent_set_keep_signed_in") is True:
            self.page.client_storage.set("recent_set_keep_signed_in", False)
            self.page.client_storage.set("just_opened", True)

        username = ""
        for user in self.repository.users:
            if user.email == email:
                username = user.username
                break
        
        self.group_listview.top_text.value = f"Hi, {username}!"
        
        joined_groups = []
        for group in self.repository.groups:
            member: Member = None
            for member in group.members:
                if member.email == email:
                    image_string = utils.convert_to_base64(self.repository.download_image(group.picture_id))
                    joined_groups.append((group, image_string))
        
        if len(joined_groups) == 0:
            self.group_listview.empty_warning_text_container.visible = True
            self.group_listview.empty_warning_text_container.offset = ft.transform.Offset(0, 0)
        else:
            self.group_listview.empty_warning_text_container.offset = ft.transform.Offset(-1, 0)
            self.group_listview.empty_warning_text_container.visible = False

        group_object: Group = None
        group_image: str = ""
        for group_object, group_image in joined_groups:
            group_button = GroupButton(group_object.group_name, group_image)
            group_button.group = group_object
            group_button.activate = lambda button, group_name, image_string: self.open_group(group_name, image_string, button.group, False)
            self.group_listview.grid.controls.append(group_button)
        
        add_button = AddGroupButton()
        add_button.on_click = lambda event: self.home_page.show_add_group_dialog()
        self.group_listview.grid.controls.append(add_button)
    
    def open_group(self, group_name: str, image_string: str, group: Group, from_reload: bool):
        self.repository.update_refs()
        
        button: GroupButton = None
        for button in self.group_listview.grid.controls:
            button.disabled = True
            
            if not from_reload:
                button.update()
            
        if not from_reload:
            self.page.snack_bar = ft.SnackBar(ft.Text("Loading group... Please wait."), duration=3000)
            self.page.snack_bar.open = True
            self.page.update()
        
        usernames = dict()
        user_images = dict()
        gcash_infos = dict()
        
        email = str(self.page.client_storage.get("email")).replace(".", ",")

        current_user = ""
        current_user_image = ""
        for user in self.repository.users:
            user_image = utils.convert_to_base64(self.repository.download_image(user.picture_link))
            user_images.update({user.email: user_image})
            usernames.update({user.email : user.username})
            
            qr_image = utils.convert_to_base64(self.repository.download_image(user.qr_image_id))
            gcash_number = user.gcash_number
            
            gcash_infos.update({user.email : {"QR Image" : qr_image, "GCash number": gcash_number}})
            
            if user.email == email:
                current_user = user.username
                current_user_image = user_image
        
        self.items_view.group_name.value = self.items_view.group_name_text.value = group_name
        self.items_view.group_image.src_base64 = image_string
        self.items_view.group_description.value = group.description
        self.items_view.username.value = current_user
        self.items_view.group_code_text.spans[0].text = group.unique_code
        self.items_view.group: Group = group
        self.items_view.set_creator(group.created_by)
        self.items_view.set_user_image(current_user_image)
        
        self.items_view.payable_list.controls = []
        self.items_view.receivable_list.controls = []

        payables, receivables, total_payable, total_receivable = 0, 0, 0.0, 0.0
        
        transaction: Transaction = None
        for transaction in group.transactions:
            paid_users = [user[0] for user in transaction.paid_by]
            item_image = utils.convert_to_base64(self.repository.download_image(transaction.image_id))
            
            if email in paid_users:
                continue
            elif transaction.posted_by == email:
                receivables += 1
                total_receivable += float(transaction.price)
                item  = ItemButton(group, self.items_view.username.value, user_images[transaction.posted_by], transaction.name, transaction.description, transaction.time_created, transaction.price, item_image, True)
                item.transaction: Transaction = transaction
                self.items_view.receivable_list.controls.append(item)
            else:
                payables += 1
                total_payable += float(transaction.price)
                
                item  = ItemButton(group, usernames[transaction.posted_by], user_images[transaction.posted_by], transaction.name, transaction.description, transaction.time_created, transaction.price, item_image, False)
                item.transaction: Transaction = transaction
                self.items_view.payable_list.controls.append(item)
        
        self.items_view.total_payable_text.value = f"Total Payable: ₱ {total_payable}"
        self.items_view.total_receivable_text.value = f"Total Receivable: ₱ {total_receivable}"
        
        if payables == 0:
            self.items_view.cont.content = self.items_view.empty_warning_text_container
        else:
            self.items_view.cont.content = self.items_view.payable_list
        
        if self.items_view.add_receivable_button not in self.items_view.receivable_list.controls:
            self.items_view.receivable_list.controls.append(self.items_view.add_receivable_button)

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
        self.open_group(group_name, image_string, self.items_view.group, True)
    
    def return_to_grid(self, event: ft.ControlEvent):
        self.items_view.payable_list.controls = []
        self.items_view.receivable_list.controls = []
        
        for button in self.group_listview.grid.controls:
            button.disabled = False
    
        self.group_listview.content = self.group_listview.grid_view
        self.group_listview.update()
    
    def show_item_informations(self, event: ft.ControlEvent, group_name: str, item_name: str):
        usernames = dict()
        
        button: ItemButton = event.control
        
        user: User = None
        for user in self.repository.users:
            usernames.update({user.username : user.email})
        
        self.home_page.item_infos_dialog.switcher.content = self.home_page.item_infos_dialog.main_row
        self.home_page.item_infos_dialog.title.visible = True
        self.home_page.item_infos_dialog.pay_button.text = "Pay now"
        self.home_page.item_infos_dialog.group_name = button.group_name
        gcash_infos = button.gcash_infos
        
        user = ""
        qr_image_string = ""
        gcash_number = ""
        for username in usernames:
            if usernames[username] == button.transaction.posted_by:
                qr_image_string = gcash_infos[usernames[username]]["QR Image"]
                gcash_number = gcash_infos[usernames[username]]["GCash number"]
                user = username

        self.home_page.item_infos_dialog.item_name.value = self.home_page.item_infos_dialog.payment_item_name.spans[0].text = item_name
        self.home_page.item_infos_dialog.price.value = self.home_page.item_infos_dialog.item_price.spans[0].text = f"₱ {button.transaction.price}"
        self.home_page.item_infos_dialog.item_image.src_base64 = button.item_image.src_base64
        self.home_page.item_infos_dialog.item_post_time.spans[0].text = button.transaction.time_created
        self.home_page.item_infos_dialog.account_name_info.value = self.home_page.item_infos_dialog.account_name_payment.value = user
        self.home_page.item_infos_dialog.description.value = button.transaction.description
        self.home_page.item_infos_dialog.qr_code.src_base64 = qr_image_string
        self.home_page.item_infos_dialog.gcash_number.spans[0].text = gcash_number
        
        if button.account_image.src_base64 != "":
            self.home_page.item_infos_dialog.account_image.src_base64 = button.account_image.src_base64
        
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
    
    def show_receivable_info(self, event: ft.ControlEvent, group: str, item_name: str):
        self.home_page.receivable_info_dialog.title.value = item_name
        self.home_page.receivable_info_dialog.group_name = group

        button: ItemButton = event.control
        transaction: Transaction = button.transaction

        self.home_page.receivable_info_dialog.paid_list.controls = []
        if transaction.paid_by != "None":
            for user in transaction.paid_by:
                image = ft.Image("/empty_user_image.svg", width=36, height=36)
                user_label = ft.Text(
                    user[0]
                )
                
                row = ft.Row(
                    controls=[image, user_label]
                )
                
                container = ft.Container(
                    row,
                    bgcolor="white",
                    padding=10,
                    border_radius=15,
                    tooltip= "Show proof of payment"
                )
                
                container.on_click = lambda e: self.home_page.receivable_info_dialog.show_proof(user[1])
                
                self.home_page.receivable_info_dialog.paid_list.controls.append(container)

        if len(transaction.paid_by) == 0 or transaction.paid_by == "None":
            self.home_page.receivable_info_dialog.content = self.home_page.receivable_info_dialog.no_paid_label
        else:
            self.home_page.receivable_info_dialog.content = self.home_page.receivable_info_dialog.paid_list
        
        self.home_page.show_receivable_info_dialog()
    
    def update_account_view(self):
        email = str(self.page.client_storage.get("email")).replace(".", ",")
        
        user_image = ""
        username = ""
        for user in self.repository.users:
            if user.email == email:
                user_image = utils.convert_to_base64(self.repository.download_image(user.picture_link))
                username = user.username
                break

        self.account_view.user_picture.src_base64 = user_image
        self.account_view.username_text.value = username
        self.account_view.email_text.value = email.replace(",", ".")