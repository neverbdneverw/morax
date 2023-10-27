import flet as ft
from flet_route import Params, Basket

from views.group_listview import GroupListView
from views.settings_view import SettingsView
from views.feedback_view import FeedbackView

class HomePage():
    def __init__(self):
        self.group_listview = GroupListView(self)
        self.settings_view = SettingsView()
        self.feedback_view = FeedbackView()
        
        self.slider_stack = ft.Stack(
            expand=True,
            controls=[self.group_listview, self.settings_view, self.feedback_view]
        )
        
        content_area_row = ft.Row(
            expand = True,
            controls=[self.slider_stack]
        )
        
        content_area = ft.Column(
            expand=True,
            spacing=0,
            controls=[content_area_row]
        )
        
        logo = ft.Image(
            src = "resources/logo_filled.png",
            width=50,
            height=50
        )
        
        logo_row = ft.Row(
            controls=[logo],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.home_button = ft.IconButton(
            selected=True,
            icon=ft.icons.HOME_OUTLINED,
            selected_icon=ft.icons.HOME_FILLED,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle(color={"selected": "black", "": "#d6d6d6"}),
        )
        
        home_button_row = ft.Row(
            controls=[self.home_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.settings_button = ft.IconButton(
            selected=False,
            icon=ft.icons.SETTINGS_OUTLINED,
            selected_icon=ft.icons.SETTINGS,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle(color={"selected": "black", "": "#d6d6d6"}),
        )
        
        settings_button_row = ft.Row(
            controls=[self.settings_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.feedback_button = ft.IconButton(
            selected=False,
            icon=ft.icons.FEEDBACK_OUTLINED,
            selected_icon=ft.icons.FEEDBACK,
            width = 50,
            height = 50,
            icon_size=36,
            style=ft.ButtonStyle(color={"selected": "black", "": "#d6d6d6"}),
        )
        
        feedback_button_row = ft.Row(
            controls=[self.feedback_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        logod = ft.Image(
            src = "resources/logo_filled.png",
            width=50,
            height=50,
            expand=True
        )
        
        logod_row = ft.Row(
            controls=[logod],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        logod_container = ft.Container(
            content=logod_row,
            padding=12.5
        )
        
        sidebar_top_column = ft.Column(
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            controls=[logo_row, home_button_row, settings_button_row, feedback_button_row]
        )
    
        sidebar = ft.Column(
            expand = True,
            width = 75,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            controls=[sidebar_top_column, logod_container]
        )
        
        sidebar_container = ft.Container(
            content=sidebar,
            padding=0,
            bgcolor="#ffffff"
        )
        
        main_row = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                sidebar_container,
                ft.VerticalDivider(width=1),
                content_area]
        )

        self.view = ft.View(
            route = "/home",
            bgcolor = "#f8fafc",
            padding=0,
            controls = [main_row]
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        self.basket = basket
        self.on_basket_set(basket)
        
        return self.view
    
    def on_basket_set(self, basket: Basket):
        pass