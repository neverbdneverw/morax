import flet as ft

class PaidUserButton(ft.Container):
    def __init__(self, email: str):
        super().__init__()
        image = ft.Image("/empty_user_image.svg", width=36, height=36)
        user_label = ft.Text(
            email
        )

        self.reject_button = ft.IconButton(
            ft.icons.REMOVE_CIRCLE_OUTLINE,
            icon_color="#ae8948"
        )

        self.show_proof_button = ft.Container(
            ft.Row(
                [image, user_label]
            )
        )

        row = ft.Row(
            controls=[self.show_proof_button, self.reject_button],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.content = row
        self.bgcolor = "white"
        self.padding = 10
        self.border_radius = 15,
        self.tooltip = "Show proof of payment"
        