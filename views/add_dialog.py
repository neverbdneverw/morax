import flet as ft

class AddDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Join a group")
        
        self.group_code_textfield = ft.TextField(
            label = "Enter 8 digit group code",
            border_radius = 15,
            expand = True,
            height=44,
            label_style = ft.TextStyle()
        )
        
        group_code_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        group_code_textfield_row.controls.append(self.group_code_textfield)
        
        self.check_if_exists_button = ft.ElevatedButton(
            disabled=True,
            content=ft.Text(
                value="Verify group code",
            )
        )
        
        check_if_exists_btn_container = ft.Container(
            content=self.check_if_exists_button,
            padding=10
        )
        
        check_if_exists_row = ft.Row(
            controls=[check_if_exists_btn_container],
            alignment=ft.MainAxisAlignment.END
        )
        
        self.join_column = ft.Column(
            controls=[group_code_textfield_row, check_if_exists_row],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.image_preview = ft.Image(
            "/default_image.png",
            width=80,
            height=80
        )
        
        image_preview_row = ft.Row(
            controls=[self.image_preview],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.image_upload_button = ft.ElevatedButton(
            height=30,
            width=80,
            content=ft.Text(
                value="Upload image",
                size=10
            )
        )
        
        image_upload_button_row = ft.Row(
            controls=[self.image_upload_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        image_upload_column = ft.Column(
            controls=[image_preview_row, image_upload_button_row],
            spacing=10
        )
        
        self.group_name_textfield = ft.TextField(
            label = "Group Name",
            border_radius = 15,
            # width=220,
            height=32,
            text_size=12,
            label_style = ft.TextStyle()
        )
        
        group_name_textfield_row = ft.Row(
            controls=[self.group_name_textfield],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.group_desc_textfield = ft.TextField(
            label = "Group Description",
            border_radius = 15,
            width = 50,
            # height = 100,
            text_style=10,
            multiline=True,
            min_lines=5,
            max_lines=5,
            label_style = ft.TextStyle()
        )
        
        group_desc_textfield_row = ft.Row(
            controls=[self.group_desc_textfield],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        group_information_column = ft.Column(
            controls=[group_name_textfield_row, group_desc_textfield_row],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
        
        self.creation_row = ft.Row(
            expand=True,
            controls=[image_upload_column, group_information_column],
            spacing=18
        )
        
        self.switcher = ft.AnimatedSwitcher(
            content = self.join_column,
            width = 400,
            height = 200,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=300,
            reverse_duration=300,
            switch_in_curve=ft.AnimationCurve.LINEAR,
            switch_out_curve=ft.AnimationCurve.LINEAR,
        )
        
        self.join_button = ft.TextButton("Join", disabled = True)
        self.create_new_button = ft.TextButton("Create New")
        self.close_button = ft.TextButton("Cancel")
        
        self.content = self.switcher
        self.actions = [
            self.join_button,
            self.create_new_button,
            self.close_button
        ]
        self.actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        self.on_dismiss=lambda e: print("Modal dialog dismissed!")
    
    def get_group_code_entry(self):
        return self.group_code_textfield.value
    
    def get_created_group_name(self):
        return self.group_name_textfield.value
    
    def get_created_group_desc(self):
        return self.group_desc_textfield.value

    def switch_to_creation(self):
        self.switcher.content = self.creation_row
        self.title.value = "Create new group"
             
    def switch_to_joining(self):
        self.switcher.content = self.join_column
        self.title.value = "Join a group"
    
    def update_colors(self, colors):
        self.group_code_textfield.border_color = colors["d6d6d6"]
        self.group_code_textfield.cursor_color = colors["black"]
        self.group_code_textfield.bgcolor = colors["d6d6d6"]
        self.group_code_textfield.color = colors["black"]
        self.group_code_textfield.label_style.color = colors["black"]
        
        self.check_if_exists_button.bgcolor = colors["d6d6d6"]
        self.check_if_exists_button.content.color = colors["ae8948"]
        
        self.image_upload_button.bgcolor = colors["d6d6d6"]
        self.image_upload_button.content.color = colors["black"]
        
        self.group_name_textfield.border_color = colors["d6d6d6"]
        self.group_name_textfield.cursor_color = colors["black"]
        self.group_name_textfield.bgcolor = colors["d6d6d6"]
        self.group_name_textfield.color = colors["black"]
        self.group_name_textfield.label_style.color = colors["black"]
        
        self.group_desc_textfield.border_color = colors["d6d6d6"]
        self.group_desc_textfield.cursor_color = colors["black"]
        self.group_desc_textfield.bgcolor = colors["d6d6d6"]
        self.group_desc_textfield.color = colors["black"]
        self.group_desc_textfield.label_style.color = colors["black"]