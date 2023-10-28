import flet as ft

class AddDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Join a group")
        self.col
        
        self.group_code_textfield = ft.TextField(
            label = "Enter 8 digit group code",
            color = ft.colors.BLACK,
            border_color = "#d6d6d6",
            border_radius = 15,
            bgcolor="#d6d6d6",
            cursor_color="black",
            expand = True,
            height=44,
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
        )
        
        group_code_textfield_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        group_code_textfield_row.controls.append(self.group_code_textfield)
        
        self.check_if_exists_button = ft.ElevatedButton(
            bgcolor = "#d6d6d6",
            disabled=True,
            content=ft.Text(
                value="Verify group code",
                color = "#ae8948"
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
            "resources/default_image.png",
            width=160,
            height=160
        )
        
        image_preview_row = ft.Row(
            controls=[self.image_preview],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.image_upload_button = ft.ElevatedButton(
            height=30,
            width=160,
            bgcolor = "#d6d6d6",
            content=ft.Text(
                value="Upload image",
                color = "#ae8948"
            )
        )
        
        image_upload_button_row = ft.Row(
            controls=[self.image_upload_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        image_upload_column = ft.Column(
            controls=[image_preview_row, image_upload_button_row],
            spacing=20
        )
        
        self.group_name_textfield = ft.TextField(
            label = "Group Name",
            color = ft.colors.BLACK,
            border_radius = 15,
            width=220,
            height=44,
            border_color = "#d6d6d6",
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            ),
            cursor_color="black",
            bgcolor="#d6d6d6"
        )
        
        group_name_textfield_row = ft.Row(
            controls=[self.group_name_textfield],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.group_desc_textfield = ft.TextField(
            label = "Group Description",
            color = ft.colors.BLACK,
            border_radius = 15,
            width = 220,
            height = 300,
            multiline=True,
            border_color = "#d6d6d6",
            min_lines=5,
            max_lines=5,
            cursor_color="black",
            bgcolor="#d6d6d6",
            label_style = ft.TextStyle(
                color = ft.colors.BLACK
            )
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