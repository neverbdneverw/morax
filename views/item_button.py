import flet as ft

class ItemButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__(
            expand=True,
            style=ft.ButtonStyle(shape = ft.ContinuousRectangleBorder(radius = 0))
        )
        account_image = ft.Image(
            "resources/default_image.png",
            width = 100,
            height = 100
        )
        
        user_name = ft.Text(
            f"Saito",
            color="#ae8948",
            weight=ft.FontWeight.W_400,
            size=16,
        )
        
        account_column = ft.Column(
            controls=[account_image, user_name],
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
            "Item 1",
            color="#ae8948",
            weight=ft.FontWeight.W_700,
            size=20
        )
        
        item_description = ft.Text(
            max_lines=3,
            color=ft.colors.BLACK,
            size = 12,
            value = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        )
        
        item_post_time = ft.Text(
            "Date Posted: ",
            color="#ae8948",
            weight=ft.FontWeight.W_200,
            italic=True
        )
        
        item_info_column = ft.Column(
            controls=[item_name, item_description, item_post_time],
            expand=True
        )
        
        item_info_row = ft.Row(
            controls=[item_info_column],
            expand=True
        )
        
        item_image = ft.Image(
            "resources/default_image.png",
            width = 100,
            height = 100
        )
        
        amount = ft.Text(
            f"Amount",
            color="#ae8948",
            weight=ft.FontWeight.W_700,
            size=20
        )
        
        payment_column = ft.Column(
            controls=[amount, item_image,],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        payment_container = ft.Container(
            content=payment_column,
            padding=ft.padding.only(10, 10, 10, 0)
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