import flet as ft

class AddReceivableDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.add_item_button = ft.TextButton("Add Item", disabled=True)
        self.cancel_button = ft.TextButton("Cancel")
        
        self.actions = [
            self.add_item_button,
            self.cancel_button
        ]
        self.actions_alignment = ft.MainAxisAlignment.SPACE_BETWEEN 
        
        self.item_image = ft.Image(
            "resources/default_image.png",
            width = 250,
            height = 250
        )
        
        self.choose_button = ft.ElevatedButton(
            height=44,
            width=160,
            bgcolor = "#d6d6d6",
            content=ft.Text(
                value="Upload image",
                color="black"
            )
        )
        
        image_upload_column = ft.Column(
            controls=[self.item_image, self.choose_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.item_name_textfield = ft.TextField(
            label = "Item name",
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
        
        self.item_date_textfield = ft.TextField(
            label = "Date",
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
        
        self.item_amount_textfield = ft.TextField(
            label = "Amount",
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
        
        self.item_description_textfield = ft.TextField(
            label = "Description",
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
        
        info_column = ft.Column(
            controls=[self.item_name_textfield, self.item_date_textfield, self.item_amount_textfield, self.item_description_textfield]
        )
        
        main_row = ft.Row(
            controls=[image_upload_column, info_column],
            width = 500,
            height = 300,
        )
        
        self.content = main_row
        self.modal = False
    
    def get_item_name(self):
        return self.item_name_textfield.value
    
    def get_item_creation_date(self):
        return self.item_date_textfield.value
    
    def get_item_amount(self):
        return self.item_amount_textfield.value
    
    def get_item_description(self):
        return self.item_description_textfield.value