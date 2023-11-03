import flet as ft
from views.item_button import ItemButton
from views.group_button import AddGroupButton

class ItemsView(ft.Column):
    def __init__(self):
        super().__init__(
            expand=True,
            spacing=0
        )
        
        self.group_image = ft.Image(
            "resources/default_image.png",
            height=80,
            width=80
        )
        
        self.group_name = ft.Text(
            expand=True,
            value="School",
            color = ft.colors.WHITE,
            weight=ft.FontWeight.W_600,
            size=44
        )
        
        header_left = ft.Row(
            expand=True,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[self.group_image, self.group_name],
            spacing=20
        )
        
        self.reload_button = ft.Container(
            content=ft.Image("resources/refresh.svg", width=48, height=48),
            padding=ft.padding.only(15, 15, 0, 15)
        )
        
        self.return_button = ft.Container(
            content=ft.Image("resources/return.svg", width=48, height=48),
            padding=15
        )
        
        end_row = ft.Row(
            controls=[self.reload_button, self.return_button]
        )
        
        header_row = ft.Row(
            controls = [header_left, end_row],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.header_container = ft.Container(
            padding = ft.padding.only(10, 10, 10, 10),
            content=header_row,
            gradient=ft.LinearGradient(
                begin=ft.alignment.center_left,
                end=ft.alignment.center_right,
                colors=[
                    "#9a6e32",
                    "#c7ac65",
                    "#c7ac65",
                    "#c7ac65"
                ]
            )
        )
        
        self.payable_list = ft.ListView(
            expand = True,
            spacing = 20,
            padding = 20
        )
        
        empty_warning_text = ft.Text(
            expand=True,
            value="Your group has no payables yet.",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_400,
            size=20
        )
        
        empty_warning_text_row = ft.Row(
            controls=[empty_warning_text]
        )
        
        self.empty_warning_text_container = ft.Container(
            content = empty_warning_text_row,
            padding = ft.padding.only(30, 10, 30, 0)
        )
        
        self.cont = ft.AnimatedSwitcher(
            transition = ft.AnimatedSwitcherTransition.FADE,
            duration = 300,
            reverse_duration = 300,
            switch_in_curve = ft.AnimationCurve.EASE_OUT,
            switch_out_curve = ft.AnimationCurve.EASE_IN,
            expand=True,
            content = self.payable_list
        )
        
        self.receivable_list = ft.ListView(
            expand = True,
            spacing = 20,
            padding = 20
        )
        
        self.payable_column = ft.Column(
            expand=True,
            spacing=0,
            controls=[self.cont]
        )
        
        self.receivable_column =ft.Column(
            expand=True,
            spacing=0,
            controls=[self.receivable_list]
        )
        
        self.add_receivable_button = AddGroupButton()
        
        self.list_switcher = ft.AnimatedSwitcher(
            transition = ft.AnimatedSwitcherTransition.SCALE,
            duration = 300,
            reverse_duration = 300,
            switch_in_curve = ft.AnimationCurve.EASE_OUT,
            switch_out_curve = ft.AnimationCurve.EASE_IN,
            expand=True,
            content = self.payable_column
        )
        
        self.group_name_text = ft.Text(
            "School",
            color="#ae8948",
            weight=ft.FontWeight.W_600,
            size=24
        )
        
        self.group_description = ft.Text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            weight=ft.FontWeight.W_400,
            size = 12
        )
        
        self.created_by_text = ft.Text(
            value = "Created by: ",
            spans = [ft.TextSpan(
                "Owen David",
                style=ft.TextStyle(italic=True, weight=ft.FontWeight.W_300)
            )],
            color="#ae8948",
            weight=ft.FontWeight.W_500,
            italic=True,
        )
        
        self.user_image = ft.Image(
            "resources/empty_user_image.svg",
            width=75,
            height=75
        )
        
        self.username = ft.Text(
            "Owen David"
        )
        
        self.receivables_button = ft.ElevatedButton(
            "My Receivables",
            bgcolor="#ae8948",
            color="white"
        )
        
        financial_recap_text = ft.Text(
            "Financial Recap: ",
            italic=True,
            color="#ae8948",
            weight=ft.FontWeight.W_400
        )
        
        self.total_payable_text = ft.Text(
            "Total Payable: ",
            color="#ae8948",
            weight=ft.FontWeight.W_600
        )
        
        self.total_receivable_text = ft.Text(
            "Total Receivable: ",
            color="#ae8948",
            weight=ft.FontWeight.W_600
        )
        
        info_column = ft.Column(
            controls=[self.user_image, self.username, self.receivables_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        recap_column = ft.Column(
            controls=[financial_recap_text, self.total_payable_text, self.total_receivable_text],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )
        
        self.personal_info_column = ft.Column(
            controls=[info_column, recap_column],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True
        )
        
        self.personal_info_container = ft.Container(
            content=ft.Row([self.personal_info_column], expand=True),
            bgcolor="#fcffff",
            expand=True,
            padding = 20,
            border=ft.border.all(1, "#d6d6d6")
        )
        
        self.group_info_column = ft.Column(
            controls=[self.group_name_text, self.group_description, self.created_by_text]
        )
        
        self.info_sidebar_column = ft.Column(
            width=250,
            expand=True,
            controls=[self.group_info_column, self.personal_info_container]
        )
        
        self.info_sidebar = ft.Container(
            content = self.info_sidebar_column,
            bgcolor = "#f5f7f8",
            padding = 10
        )
        
        list_view_row = ft.Row(
            controls=[self.list_switcher, self.info_sidebar],
            expand=True
        )
        
        self.controls = [self.header_container, list_view_row]
    
    def display_transactions(self, email: str, group_name: str, image_string: str, transactions: dict, item_images: dict):
        email = email.replace(".", ".")
        self.group_name.value = group_name
        self.group_image.src_base64 = image_string
        
        if len(self.payable_list.controls) > 0:
            self.payable_list.controls = []
        
        if len(self.receivable_list.controls) > 0:
            self.receivable_list.controls = []

        payables = 0
        receivables = 0
        
        total_payable = 0
        total_receivable = 0
        
        transactions = dict(transactions)
        for transaction_name in transactions.keys():
            if transactions[transaction_name]['Posted by']['Username'] == self.username.value:
                receivables += 1
                total_receivable += float(transactions[transaction_name]['Price'])
                item  = ItemButton(group_name, transaction_name, transactions, item_images[transaction_name], True)
                self.receivable_list.controls.append(item)
            elif transactions[transaction_name]['Posted by']['Username'] == self.username.value and email in transactions[transaction_name]['Paid by']:
                continue
            else:
                payables += 1
                total_payable += float(transactions[transaction_name]['Price'])
                item  = ItemButton(group_name, transaction_name, transactions, item_images[transaction_name], False)
                self.payable_list.controls.append(item)
        
        self.total_payable_text.value = f"Total Payable: ₱ {total_payable}"
        self.total_receivable_text.value = f"Total Receivable: ₱ {total_receivable}"
        
        if payables == 0:
            self.cont.content = self.empty_warning_text_container
            return
        else:
            self.cont.content = self.payable_list
    
    def set_creator(self, creator):
        self.created_by_text.spans[0].text = creator
    
    def set_user_image(self, user_image: str):
        if user_image != "":
            self.user_image.src_base64 = user_image
    
    def on_trigger_reload(self, event: ft.ControlEvent):
        pass