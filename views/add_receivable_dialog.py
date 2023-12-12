import flet as ft

class AddReceivableDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        ####################################################
        ## Make the Add receivable dialog
        ####################################################
        self.group = ""
        
        self.add_item_button = ft.TextButton("Add Item", disabled=True)
        self.cancel_button = ft.TextButton("Cancel")
        
        self.actions = [
            self.add_item_button,
            self.cancel_button
        ]
        self.actions_alignment = ft.MainAxisAlignment.SPACE_BETWEEN 
        
        self.item_image = ft.Image(
            "/default_image.png",
            width = 250,
            height = 250
        )
        
        self.choose_button = ft.ElevatedButton(
            height=44,
            width=160,
            content=ft.Text(
                value="Upload image",
            )
        )
        
        image_upload_column = ft.Column(
            controls=[self.item_image, self.choose_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.item_name_textfield = ft.TextField(
            label = "Item name",
            border_radius = 15,
            width=230,
            height=44,
            label_style = ft.TextStyle()
        )
        
        self.item_month_textfield = ft.TextField(
            label = "Month",
            border_radius = 15,
            width=85,
            height=44,
            label_style = ft.TextStyle()
        )
        
        self.item_day_textfield = ft.TextField(
            label = "Day",
            border_radius = 15,
            width=60,
            height=44,
            label_style = ft.TextStyle(),
            input_filter=ft.NumbersOnlyInputFilter()
        )
        
        self.item_year_textfield = ft.TextField(
            label = "Year",
            border_radius = 15,
            width=65,
            height=44,
            label_style = ft.TextStyle(),
            input_filter=ft.NumbersOnlyInputFilter()
        )
        
        item_date_row = ft.Row(
            controls=[self.item_month_textfield, self.item_day_textfield, self.item_year_textfield],
            spacing=10
        )
        
        self.item_amount_textfield = ft.TextField(
            label = "Amount",
            border_radius = 15,
            width=230,
            height=44,
            label_style = ft.TextStyle(),
            input_filter=ft.NumbersOnlyInputFilter()
        )
        
        self.item_description_textfield = ft.TextField(
            label = "Description",
            border_radius = 15,
            width = 230,
            height = 300,
            multiline=True,
            min_lines=5,
            max_lines=5,
            label_style = ft.TextStyle()
        )
        
        info_column = ft.Column(
            controls=[self.item_name_textfield, item_date_row, self.item_amount_textfield, self.item_description_textfield]
        )
        
        main_row = ft.Row(
            controls=[image_upload_column, info_column],
            width = 500,
            height = 300,
        )
        
        self.content = main_row
        self.modal = False
    
    # get entered item name
    def get_item_name(self):
        return self.item_name_textfield.value
    
    # get entered creation month
    def get_item_creation_month(self):
        return self.item_month_textfield.value
    
    # get entered creation day
    def get_item_creation_day(self):
        return self.item_day_textfield.value
    
    # get entered creation year
    def get_item_creation_year(self):
        return self.item_year_textfield.value
    
    # get the entered item amount
    def get_item_amount(self):
        return self.item_amount_textfield.value
    
    # get the item description
    def get_item_description(self):
        return self.item_description_textfield.value
    
    # update the colors with scheme
    def update_colors(self, colors):
        self.choose_button.bgcolor = colors["d6d6d6"]
        self.choose_button.content.color = colors["black"]
        
        self.item_name_textfield.border_color = colors["d6d6d6"]
        self.item_name_textfield.cursor_color = colors["black"]
        self.item_name_textfield.bgcolor = colors["d6d6d6"]
        self.item_name_textfield.color = colors["black"]
        self.item_name_textfield.label_style.color = colors["black"]
        
        self.item_month_textfield.border_color = colors["d6d6d6"]
        self.item_month_textfield.cursor_color = colors["black"]
        self.item_month_textfield.bgcolor = colors["d6d6d6"]
        self.item_month_textfield.color = colors["black"]
        self.item_month_textfield.label_style.color = colors["black"]
        
        self.item_day_textfield.border_color = colors["d6d6d6"]
        self.item_day_textfield.cursor_color = colors["black"]
        self.item_day_textfield.bgcolor = colors["d6d6d6"]
        self.item_day_textfield.color = colors["black"]
        self.item_day_textfield.label_style.color = colors["black"]
        
        self.item_year_textfield.border_color = colors["d6d6d6"]
        self.item_year_textfield.cursor_color = colors["black"]
        self.item_year_textfield.bgcolor = colors["d6d6d6"]
        self.item_year_textfield.color = colors["black"]
        self.item_year_textfield.label_style.color = colors["black"]
        
        self.item_amount_textfield.border_color = colors["d6d6d6"]
        self.item_amount_textfield.cursor_color = colors["black"]
        self.item_amount_textfield.bgcolor = colors["d6d6d6"]
        self.item_amount_textfield.color = colors["black"]
        self.item_amount_textfield.label_style.color = colors["black"]
        
        self.item_description_textfield.border_color = colors["d6d6d6"]
        self.item_description_textfield.cursor_color = colors["black"]
        self.item_description_textfield.bgcolor = colors["d6d6d6"]
        self.item_description_textfield.color = colors["black"]
        self.item_description_textfield.label_style.color = colors["black"]