import flet as ft
from views.group_button import GroupButton

class AccountView(ft.Column):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(0, 4.5),
            animate_offset=ft.animation.Animation(300)
        )
        
        top_text = ft.Text(
            expand=True,
            value="ACCOUNT",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_600,
            size=54
        )
        
        top_text_row = ft.Row(
            expand=True,
            controls=[top_text]
        )
        
        self.top_text_container = ft.Container(
            padding=30,
            content=top_text_row
        )
        
        self.grid = ft.GridView(
            expand = True,
            runs_count=5,
            max_extent=200,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=20,
            padding = 30
        )
        
        self.controls.append(self.top_text_container)
        self.controls.append(self.grid)
        
        for i in range(25):
            group_button = GroupButton(str(i))
            self.grid.controls.append(group_button)
    
    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()
            