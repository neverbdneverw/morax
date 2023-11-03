import flet as ft
from views.item_button import ItemButton

class ItemInfoDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.item_name = ft.Text(
            "Gatas",
            color="#ae8948",
            weight=ft.FontWeight.W_700,
        )
        
        self.price = ft.Text(
            "₱ 450",
            color="#ae8948",
            weight=ft.FontWeight.W_700,
        )
        
        self.title = ft.Row(
            controls = [self.item_name, self.price],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.item_image = ft.Image(
            "resources/default_image.png",
            width=120,
            height=120
        )
        
        self.account_image = ft.Image(
            "resources/empty_user_image.svg",
            width = 36,
            height = 36
        )
        
        self.account_name = ft.Text(
            "Owen David",
            color="#ae8948",
        )
        
        account_row = ft.Row(
            controls=[self.account_image, self.account_name],
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.description = ft.Text(
            "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available.",
            weight=ft.FontWeight.W_400
        )
        
        description_column = ft.Column(
            controls=[self.description],
            height=100,
            scroll=ft.ScrollMode.ALWAYS
        )
        
        self.item_post_time = ft.Text(
            value = "Date Posted: ",
            spans = [ft.TextSpan(
                f"October 30, 2023 - 12:00 am",
                style=ft.TextStyle(italic=True, weight=ft.FontWeight.W_300)
            )],
            color="#ae8948",
            weight=ft.FontWeight.W_500,
            italic=True,
        )
        
        info_column = ft.Column(
            controls=[account_row, description_column, self.item_post_time],
            width = 350,
            height = 150
        )
        
        self.main_row = ft.Row(
            controls = [self.item_image, info_column]
        )
        
        qr_indicator = ft.Text(
            "Pay with QR Code"
        )
        
        self.qr_code = ft.Image(
            "resources/sample_qr.png",
            width = 120,
            height = 120
        )
        
        qr_column = ft.Column(
            controls=[qr_indicator, self.qr_code],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.account_image = ft.Image(
            "resources/empty_user_image.svg",
            width = 24,
            height = 24
        )
        
        self.account_name = ft.Text(
            "Owen David",
            size=8
        )
        
        gcash_acct_user = ft.Column(
            controls=[self.account_image, self.account_name],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
        
        self.gcash_number = ft.Text(
            value = "Gcash number: ",
            size=14,
            spans = [ft.TextSpan(
                f"09999999999",
            )],
        )
        
        gcash_info_row = ft.Row(
            controls=[gcash_acct_user, self.gcash_number],
            spacing=0
        )
        
        self.payment_item_name = ft.Text(
            value = "Item: ",
            spans = [ft.TextSpan(
                f"Gatas",
            )],
        )
        
        self.item_price = ft.Text(
            value = "Amount to be paid: ",
            spans = [ft.TextSpan(
                "₱ 450",
            )],
        )
        
        gcash_info_column = ft.Column(
            controls=[gcash_info_row, self.payment_item_name, self.item_price],
            spacing=30
        )
        
        gcash_container = ft.Container(
            content=gcash_info_column,
            padding=5,
            bgcolor="#f6f8f8"
        )
        
        self.payment_row = ft.Row(
            controls=[qr_column, gcash_container],
            width = 480,
            height = 150
        )

        self.switcher = ft.AnimatedSwitcher(
            content = self.main_row,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=300,
            reverse_duration=300,
            switch_in_curve=ft.AnimationCurve.LINEAR,
            switch_out_curve=ft.AnimationCurve.LINEAR,
        )
        
        self.pay_button = ft.TextButton("Pay now")
        self.cancel_button = ft.TextButton("Cancel")
        
        self.content=self.switcher
        self.actions=[
            self.pay_button,
            self.cancel_button,
        ]
        self.actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    
    def show_payment_details(self):
        self.switcher.content = self.payment_row
        self.switcher.update()
    
    def load_infos(self, control: ItemButton, item_name: str, item_informations: dict):
        self.switcher.content = self.main_row
        self.title.visible = True
        self.pay_button.text = "Pay now"

        informations = dict(item_informations)
        self.item_name.value = self.payment_item_name.spans[0].text = item_name
        self.price.value = self.item_price.spans[0].text = f"₱ {informations['Price']}"
        self.item_image.src_base64 = control.item_image.src_base64
        self.item_post_time.spans[0].text = informations['Time created']
        self.account_name.value = informations["Posted by"]['Username']
        self.description.value = informations['Description']