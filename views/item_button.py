import flet as ft

class ItemButton(ft.ElevatedButton):
    def __init__(self, group_name: str, username: str, image_string: str, transaction_name: str, transactions: dict, item_image_string: str, has_amount_received: bool):
        super().__init__(
            expand=True,
            style=ft.ButtonStyle(shape = ft.ContinuousRectangleBorder(radius = 0))
        )
        
        self.group_name = group_name
        self.gcash_infos = None

        self.account_image = ft.Image(
            "resources/empty_user_image.svg",
            width = 100,
            height = 100
        )
        
        if image_string != "":
            self.account_image.src_base64 = image_string
        
        user_name = ft.Text(
            username,
            color="#ae8948",
            weight=ft.FontWeight.W_600,
            size=16,
            width=100,
            text_align=ft.TextAlign.CENTER
        )
        
        account_column = ft.Column(
            controls=[ft.Container(self.account_image, border_radius=15), user_name],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        account_container = ft.Container(
            content=account_column,
            padding=ft.padding.only(10, 10, 10, 0)
        )
        
        self.account_container_row = ft.Row(
            controls=[account_container],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        item_name = ft.Text(
            transaction_name,
            color="#ae8948",
            weight=ft.FontWeight.W_700,
            size=20
        )
        
        item_description = ft.Text(
            max_lines=3,
            color=ft.colors.BLACK,
            size = 12,
            value = transactions[transaction_name]["Description"]
        )
        
        item_post_time = ft.Text(
            value = "Date Posted: ",
            spans = [ft.TextSpan(
                f"{transactions[transaction_name]['Time created']}",
                style=ft.TextStyle(italic=True, weight=ft.FontWeight.W_300)
            )],
            color="#ae8948",
            weight=ft.FontWeight.W_500,
            italic=True,
        )
        
        amount_received = ft.Text(
            value = "Amount Received: ",
            spans = [ft.TextSpan(
                f"₱ 100",
                style=ft.TextStyle(italic=True, weight=ft.FontWeight.W_300)
            )],
            color="#ae8948",
            weight=ft.FontWeight.W_500,
            italic=True,
        )
        
        item_info_column = ft.Column(
            controls=[item_name, item_description, item_post_time],
            expand=True
        )
        
        if has_amount_received:
            item_info_column.controls.append(amount_received)
        
        item_info_row = ft.Row(
            controls=[item_info_column],
            expand=True
        )
        
        self.item_image = ft.Image(
            "resources/default_image.png",
            width = 100,
            height = 100
        )
        
        if item_image_string != "":
            self.item_image.src_base64 = item_image_string
        
        amount = ft.Text(
            f"₱ {transactions[transaction_name]['Price']}",
            color="#ae8948",
            weight=ft.FontWeight.W_700,
            size=20
        )
        
        payment_column = ft.Column(
            controls=[amount, self.item_image],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        payment_container = ft.Container(
            content=payment_column,
            padding=ft.padding.only(20, 20, 20, 20)
        )
        
        payment_row = ft.Row(
            controls=[payment_container]
        )
        
        column = ft.Row(
            controls=[self.account_container_row, item_info_row, payment_row],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
            spacing=0
        )
        
        self.content = column
        self.on_click = lambda event: self.activate(event, self.group_name, transaction_name, transactions[transaction_name])
    
    def activate(self, event: ft.ControlEvent, group: str, item_name: str,  item_informations: dict):
        pass