import flet as ft

class AppearanceDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        title = ft.Text("Appearance", weight=ft.FontWeight.BOLD)
        subtitle = ft.Text("Customize the app's visual style and layout to suit your preferences.", color="#a6a6a6", size=12)
        
        title_column = ft.Column(
            controls = [title, subtitle]
        )
        
        self.title = title_column
        
        dark_mode_text = ft.Text("Dark Mode", weight=ft.FontWeight.W_700)
        dark_mode_switch = ft.Switch()
        
        dark_mode_row = ft.Row(
            controls=[dark_mode_text, dark_mode_switch],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        self.content = dark_mode_row
        
        def close(event: ft.ControlEvent):
            self.open = False
            self.page.update()
        
        close_button = ft.TextButton("Close")
        close_button.on_click = close
        
        self.actions = [close_button]
        self.actions_alignment = ft.MainAxisAlignment.END
        
class CurrencyDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        title = ft.Text("Currency", weight=ft.FontWeight.BOLD)
        subtitle = ft.Text("Please be cautious when changing the app's currency, as this action may result in potential pricing and conversion issues for your transactions.", width=400, color="#a6a6a6", size=12)
        
        title_column = ft.Column(
            controls = [title, subtitle]
        )
        
        self.title = title_column
        
        self.currency_choices = ft.RadioGroup(
            content=ft.Row([
                ChoiceButton("PHP", "ph.png"),
                ChoiceButton("USD", "usa.png"),
                ChoiceButton("EU", "eu.png")
            ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START, height=100, spacing=50),
        )
        
        self.content = self.currency_choices
        
        def close(event: ft.ControlEvent):
            self.open = False
            self.page.update()
        
        close_button = ft.TextButton("Close")
        close_button.on_click = close
        
        self.actions = [close_button]
        self.actions_alignment = ft.MainAxisAlignment.END

class ChoiceButton(ft.Column):
    def __init__(self, label: str, source: str):
        super().__init__()
        
        supporting_image = ft.Container(
            ft.Image(
                "assets/" + source,
                width=50,
                height=50,
                fit=ft.ImageFit.FILL
            ),
            border_radius=5
        )
        
        button_name = ft.Text(
            label,
            weight=ft.FontWeight.W_400
        )
        
        self.controls = [
            ft.Radio(value=label),
            supporting_image,
            button_name
        ]
        
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 10