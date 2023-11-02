import flet as ft

def main(page: ft.Page):

    c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=200)

    def animate_container(e):
        c1.left = page.width - c1.width - 20 # padding of left and right
        page.update()
    
    def follow_resize(e):
        print("RESIZING")
    
    page.on_resize = animate_container

    page.add(
        ft.Stack([c1], height=250, expand=True),
        ft.ElevatedButton("Animate!", on_click=animate_container),
    )

ft.app(target=main)