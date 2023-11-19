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
    
    def show_who_paid(self, informations: dict):
        self.paid_list.controls = []
        paid_by = dict(informations['Paid by'])
        for user in paid_by.keys():
            image = ft.Image("resources/empty_user_image.svg", width=36, height=36)
            user_label = ft.Text(
                user
            )
            
            row = ft.Row(
                controls=[image, user_label]
            )
            
            container = ft.Container(
                row,
                bgcolor="white",
                padding=10,
                border_radius=15,
                tooltip= "Show proof of payment"
            )
            
            container.on_click = lambda e: self.show_proof(paid_by[user])
            
            self.paid_list.controls.append(container)

        if len(paid_by) == 0:
            self.content = self.no_paid_label
        else:
            self.content = self.paid_list
    
    def show_proof(self, id: str):
        pass