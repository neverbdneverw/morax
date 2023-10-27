import flet as ft

class FeedbackView(ft.Column):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(0, 3),
            animate_offset=ft.animation.Animation(300)
        )
        
        top_text = ft.Text(
            expand=True,
            value="FEEDBACK",
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
            text = ft.Container(
                content=ft.Text(
                    f"Column {i}",
                    color="green",
                    weight=ft.FontWeight.W_500,
                ),
                padding=10
            )
            
            text_row = ft.Row(
                controls=[text],
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            image = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Image("resources/logo_filled.png", width=150, height=150)]
            )
            
            column = ft.Column(
                controls=[text_row, ft.Container(content=image)],
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            aim = ft.Card(
                content=column,
                color="white"
            )
            
            self.grid.controls.append(aim)
    
    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()
            