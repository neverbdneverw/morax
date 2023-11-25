import flet as ft

class ShowReceivableInfoDialog(ft.AlertDialog):
    group_name = ""
    def __init__(self):
        super().__init__()
        self.completed_button = ft.TextButton("Mark as completed")
        self.cancel_button = ft.TextButton("Cancel")
        
        self.actions = [
            self.completed_button,
            self.cancel_button
        ]
        self.actions_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        
        self.paid_list = ft.ListView(spacing=5, width=400, height=200, padding=20)
        
        self.content = self.paid_list
        
        self.no_paid_label = ft.Text("No payment has yet been received.", width=400, height=200)
        
        self.title = ft.Text("HAHA", weight = ft.FontWeight.W_700)
    
    def show_proof(self, id: str):
        pass