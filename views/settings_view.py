import flet as ft
from views.settings_view_dialogs import *

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
        
        self.appearance_setting = SettingButton("Appearance", "Customize the app's visual style and layout to suit your preferences", "")
        self.currency_setting = SettingButton("Currency", "Adjust the currency settings to specify your preferred currency for transactions and display.", "Currently set to: P")
        
        setting_list = ft.Column(
            controls=[
                self.appearance_setting,
                self.currency_setting,
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
    def __init__(self, setting_name: str, setting_description: str, additonal_state: str):
        super().__init__()
        
        self.setting_name = ft.Text(
            setting_name,
            size=24,
            weight=ft.FontWeight.W_700
        )
        
        self.setting_with_current = ft.Text(
            additonal_state,
            italic=True,
            color="#a6a6a6"
        )
        
        setting_title_row = ft.Row(
            [self.setting_name]
        )
        
        if additonal_state:
            setting_title_row.controls.append(self.setting_with_current)
        
        self.setting_description = ft.Text(
            setting_description,
            size=14,
            color="#a6a6a6",
            expand=True
        )
        
        self.setting_icon = ft.Icon(
            ft.icons.MORE_HORIZ
        )
        
        bottom_row = ft.Row(
            controls=[self.setting_description]
        )
        
        bottom_row.controls.append(self.setting_icon)
        
        main_column = ft.Column(
            controls=[
                setting_title_row,
                bottom_row
            ],
            spacing=10
        )
        
        self.content = main_column
        self.bgcolor = "#fcffff"
        self.padding = 20
        self.margin = ft.margin.only(40, 0, 40, 0)
        self.border_radius = 15
        
        def change_color(event: ft.ControlEvent):
            self.bgcolor = "#d6d6d6" if event.data == "true" else "#fcffff"
            self.update()

        self.on_hover = change_color