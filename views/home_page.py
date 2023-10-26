import flet as ft
from flet_route import Params, Basket

class HomePage():
    def __init__(self):
        self.view = ft.View(
            route = "/home",
            bgcolor = "#fafafa",
            controls = [ft.Text("HOMEPAGE!!!")]
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view
    