import flet as ft
from views.group_button import GroupButton, AddGroupButton
from views.items_view import ItemsView

class GroupListView(ft.AnimatedSwitcher):
    def __init__(self, homepage):
        super().__init__(
            offset=ft.transform.Offset(0, 0),
            animate_offset = ft.animation.Animation(300),
            transition = ft.AnimatedSwitcherTransition.SCALE,
            duration = 300,
            reverse_duration = 300,
            switch_in_curve = ft.AnimationCurve.EASE_OUT,
            switch_out_curve = ft.AnimationCurve.EASE_IN
        )

        self.homepage = homepage
        
        self.top_text = ft.Text(
            expand=True,
            value="Hello User",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_600,
            size=54
        )
        
        top_text_row = ft.Row(
            expand=True,
            controls=[self.top_text]
        )
        
        self.top_text_container = ft.Container(
            padding = ft.padding.only(30, 30, 30, 0),
            content=top_text_row
        )
        
        empty_warning_text = ft.Text(
            expand=True,
            value="You have not joined a group as of yet. Click the box to create one.",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_400,
            size=20
        )
        
        empty_warning_text_row = ft.Row(
            controls=[empty_warning_text]
        )
        
        self.empty_warning_text_container = ft.Container(
            content = empty_warning_text_row,
            padding = ft.padding.only(30, 10, 30, 0),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(250)
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
        
        self.items_view = ItemsView()
        
        self.grid_view = ft.Column(
            controls=[self.top_text_container, self.empty_warning_text_container, self.grid]
        )
        
        self.content = self.grid_view
    
    def setup_gui(self, groups: dict, images: dict):
        if len(groups.keys()) == 0:
            self.empty_warning_text_container.visible = True
            self.empty_warning_text_container.offset = ft.transform.Offset(0, 0)
        else:
            self.empty_warning_text_container.offset = ft.transform.Offset(-1, 0)
            self.empty_warning_text_container.visible = False

        for group_name in groups.keys():
            group_button = GroupButton(group_name, images[group_name])
            self.grid.controls.append(group_button)
        
        add_button = AddGroupButton()
        self.grid.controls.append(add_button)

    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()
    
    def trigger_reload(self, email: str):
        pass
            