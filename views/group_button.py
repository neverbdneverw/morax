import flet as ft

class GroupButton(ft.ElevatedButton):
    def __init__(self, group_name):
        super().__init__()
        self.group_name = group_name
        
        text = ft.Container(
            content=ft.Text(
                f"{group_name}",
                color="#ae8948",
                weight=ft.FontWeight.W_700,
                size=20
            ),
            padding=ft.padding.only(10, 10, 10, 0)
        )
        
        self.text_row = ft.Row(
            controls=[text],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.image = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ft.Image("resources/default_image.png", width=150, height=150)]
        )
        
        column = ft.Column(
            controls=[self.text_row, ft.Container(content=self.image)],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )
        
        self.content = column
        self.on_click = lambda event: self.activate(event)
        self.style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        )
        
    def activate(self, event):
        pass

class AddGroupButton(GroupButton):
    def __init__(self):
        super().__init__("Add")
        self.image.controls[0].src = "resources/add_icon.svg"
        self.text_row.visible = False
        