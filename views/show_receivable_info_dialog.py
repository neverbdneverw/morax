import flet as ft

class ShowReceivableInfoDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.completed_button = ft.TextButton("Mark as completed")
        self.cancel_button = ft.TextButton("Cancel")
        
        self.actions = [
            self.completed_button,
            self.cancel_button
        ]
        self.actions_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        
        self.title = ft.Text("HAHA")