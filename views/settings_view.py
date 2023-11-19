import flet as ft
from views.group_button import GroupButton

class SettingsView(ft.Column):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(0, 1.5),
            animate_offset=ft.animation.Animation(300)
        )
        
        top_text = ft.Text(
            expand=True,
            value="Settings",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_600,
            size=54
        )
        
        top_text_row = ft.Row(
            expand=True,
            controls=[top_text]
        )
        
        self.top_text_container = ft.Container(
            padding=ft.padding.only(30, 30, 30, 0),
            content=top_text_row
        )
        
        setting_list = ft.Column(
            controls=[
                SettingButton("Appearance", "Customize the app's visual style and layout to suit your preferences", False),
                SettingButton("Currency", "Adjust the currency settings to specify your preferred currency for transactions and display.", False),
                SettingButton("Notification", "Notify me about updates within my groups.", True)
            ]
        )
        
        setting_container = ft.Container(
            setting_list,
            bgcolor="#ebebeb",
            border_radius=15,
            margin=30,
            padding=ft.padding.only(0, 40, 0, 40)
        )
        
        self.controls.append(self.top_text_container)
        self.controls.append(setting_container)
    
    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()

class SettingButton(ft.Container):
    def __init__(self, setting_name: str, setting_description: str, stateful: bool):
        super().__init__()
        
        self.setting_name = ft.Text(
            setting_name,
            size=24,
            weight=ft.FontWeight.W_700
        )
        
        self.setting_description = ft.Text(
            setting_description,
            size=14,
            color="#a6a6a6",
            expand=True
        )
        
        self.setting_icon = ft.Icon(
            ft.icons.MORE_HORIZ
        )
        
        self.setting_switch = ft.Switch(
            height=24,
            active_color="#ae8948"
        )
        
        bottom_row = ft.Row(
            controls=[self.setting_description]
        )
        
        bottom_row.controls.append(self.setting_switch if stateful else self.setting_icon)
        
        main_column = ft.Column(
            controls=[
                self.setting_name,
                bottom_row
            ],
            spacing=10
        )
        
        self.content = main_column
        self.bgcolor = "#fcffff"
        self.padding = 20
        self.margin = ft.margin.only(40, 0, 40, 0)
        self.border_radius = 15