import flet as ft
from views.item_button import ItemButton

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
        
        self.return_button = ft.Container(
            content=ft.Image("resources/return.svg", width=48, height=48),
            padding=15
        )
        
        header_row = ft.Row(
            controls = [header_left, self.return_button],
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
        
        self.grid = ft.ListView(
            expand = True,
            spacing = 20,
            padding = 20
        )
        
        cont = ft.Container(
            expand=True,
            content = self.grid
        )
        
        self.controls = [self.header_container, cont]
    
    def display_transactions(self, group_name: str, image_string: str, transactions: dict, item_images: dict):
        self.group_name.value = group_name
        self.group_image.src_base64 = image_string
        for transaction in dict(transactions).keys():
            item  = ItemButton(transaction, transactions, item_images[transaction])
            self.grid.controls.append(item)