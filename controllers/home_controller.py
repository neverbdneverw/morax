from controllers.Database import Database
from views.home_page import HomePage
import flet as ft
from flet_route import Basket

class HomeController:
    def __init__(self, page: ft.Page, database: Database, home_page: HomePage):
        self.page = page
        self.database = database
        self.home_page = home_page
        
        self.home_page.home_button.on_click = self.buttons_change
        self.home_page.settings_button.on_click = self.buttons_change
        self.home_page.feedback_button.on_click = self.buttons_change
        self.home_page.on_basket_set = self.fill_groups
        
        self.sidebar_buttons = [self.home_page.home_button, self.home_page.settings_button, self.home_page.feedback_button]
    
    def fill_groups(self, basket: Basket):
        email = basket.email
        self.database.update_refs()
        groups = self.database.get_groups(email)
        
        self.home_page.group_listview.setup_gui(groups)
    
    def buttons_change(self, event: ft.ControlEvent):
        new_button = event.control
        old_index = 0
        new_index = 0
        for index, button_ in enumerate(self.sidebar_buttons):
            if button_.selected is True:
                old_index = index
            
            if new_button == button_:
                new_index = index
            
        for button_ in self.sidebar_buttons:
            if button_ == new_button:
                button_.selected = True
            else:
                button_.selected = False
        
        if old_index == 0 and new_index == 1:
            self.home_page.group_listview.show(-1)
            self.home_page.settings_view.show(0)
            self.home_page.feedback_view.show(1)
        elif (old_index == 1 or old_index == 0) and new_index == 2:
            self.home_page.group_listview.show(-2)
            self.home_page.settings_view.show(-1)
            self.home_page.feedback_view.show(0)
        elif old_index == 2 and new_index == 1:
            self.home_page.group_listview.show(-1)
            self.home_page.settings_view.show(0)
            self.home_page.feedback_view.show(1)
        elif (old_index == 1 or old_index ==2) and new_index == 0:
            self.home_page.group_listview.show(0)
            self.home_page.settings_view.show(1)
            self.home_page.feedback_view.show(2)
        
        self.page.update()