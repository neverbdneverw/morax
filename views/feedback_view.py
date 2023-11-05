import flet as ft
from views.group_button import GroupButton

class FeedbackView(ft.Column):
    def __init__(self):
        super().__init__(
            offset=ft.transform.Offset(0, 3),
            animate_offset=ft.animation.Animation(300)
        )
        
        top_text = ft.Text(
            expand=True,
            value="Help and Support",
            color = ft.colors.BLACK,
            weight=ft.FontWeight.W_600,
            size=54
        )
        
        top_text_row = ft.Row(
            expand=True,
            controls=[top_text]
        )
        
        self.top_text_container = ft.Container(
            padding=ft.padding.only(30, 30, 30, 0),
            content=top_text_row
        )

        subtitle_text = ft.Text(
            expand=True,
            value="Having problems with the app? Please refer to the options below on how we can help you.",
            color=ft.colors.BLACK,
            weight=ft.FontWeight.W_400,
            size=20
        )

        subtitle_text_row = ft.Row(
            expand=True,
            controls=[subtitle_text]
        )

        self.subtitle_text_container = ft.Container(
            padding=ft.padding.only(30, 0, 30, 0),
            content=subtitle_text_row
        )

        contact_image = ft.Image(
            src="resources/contact_icon.svg",
            width = 200,
            height = 200
        )

        contact_image_container = ft.Container(
            content=contact_image,
            padding=30
        )

        contact_checkicon = ft.Image(
            src="resources/check_icon.svg",
            width=24,
            height=24
        )

        contact_describeissue_text = ft.Text(
            value="Describe Issue",
            size=15
        )

        contact_describeissue_row = ft.Row(
            controls=[contact_checkicon,contact_describeissue_text]
        )

        describe_issue_container = ft.Container(
            content=contact_describeissue_row,
            bgcolor="#F6F8F8",
            border = ft.border.all(width=1, color="#D6D6D6"),
            width=275,
            padding=8
        )

        contact_send_report_text = ft.Text(
            value="Send Report",
            size = 15
        )

        contact_send_report_row = ft.Row(
            controls=[contact_checkicon, contact_send_report_text]
        )

        send_report_container = ft.Container(
            content=contact_send_report_row,
            bgcolor="#F6F8F8",
            border=ft.border.all(width=1, color="#D6D6D6"),
            width = 275,
            padding=8
        )

        contact_get_help_text = ft.Text(
            value="Get Help",
            size=15
        )

        contact_get_help_row = ft.Row(
            controls=[contact_checkicon, contact_get_help_text]
        )

        get_help_container = ft.Container(
            content=contact_get_help_row,
            bgcolor="#F6F8F8",
            border=ft.border.all(width=1, color="#D6D6D6"),
            width=275,
            padding=8
        )

        button_contact_us = ft.ElevatedButton(
            text="Contact Us",
            color="#FFFFFF",
            bgcolor="#AE8948",
        )

        button_contact_us_container = ft.Container(
            content=button_contact_us,
            padding=20
        )

        contact_background_column = ft.Column(
            controls=[contact_image_container, describe_issue_container, send_report_container, get_help_container, button_contact_us_container],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )

        self.background_contact_container = ft.Container(
            content=contact_background_column,
            bgcolor="#F5F7F8",
            padding=ft.padding.only(30, 0, 30, 30),
            margin=40,
            border_radius=15,
            border=ft.border.all(width=1, color="#D6D6D6")
        )

        contribute_image = ft.Image(
            src="resources/contribute_icon.svg",
            width=200,
            height=200
        )

        contribute_image_container = ft.Container(
            content=contribute_image,
            padding=30
        )

        contribute_checkicon = ft.Image(
            src="resources/check_icon.svg",
            width=24,
            height=24
        )

        contribute_helpproject_text = ft.Text(
            value="Help  this project become better"
        )

        contribute_helpproject_row = ft.Row(
            controls=[contribute_checkicon,contribute_helpproject_text]
        )

        helpproject_container_container = ft.Container(
            content=contribute_helpproject_row,
            bgcolor="#F6F8F8",
            border = ft.border.all(width=1, color="#D6D6D6"),
            width=275,
            padding=8
        )

        contribute_contributecode_text = ft.Text(
            value="Contribute Code"
        )

        contribute_contributecode_row = ft.Row(
            controls=[contribute_checkicon, contribute_contributecode_text]
        )

        contributecode_container_container = ft.Container(
            content=contribute_contributecode_row,
            bgcolor="#F6F8F8",
            border=ft.border.all(width=1, color="#D6D6D6"),
            width=275,
            padding=8
        )

        contribute_involve_text = ft.Text(
            value="Get involved with the project"
        )

        contribute_involved_row = ft.Row(
            controls=[contribute_checkicon, contribute_involve_text]
        )

        involve_container_container = ft.Container(
            content=contribute_involved_row,
            bgcolor="#F6F8F8",
            border=ft.border.all(width=1, color="#D6D6D6"),
            width=275,
            padding=8
        )

        button_contribute = ft.ElevatedButton(
            text="Contribute Code",
            color="#FFFFFF",
            bgcolor="#AE8948",
        )

        button_contribute_container = ft.Container(
            content=button_contribute,
            padding=20
        )

        contribute_background_column = ft.Column(
            controls=[contribute_image_container, helpproject_container_container, contributecode_container_container, involve_container_container, button_contribute_container],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )

        self.background_contribute_container = ft.Container(
            content=contribute_background_column,
            bgcolor="#F5F7F8",
            padding=ft.padding.only(30, 0, 30, 30),
            margin=40,
            border_radius=15,
            border=ft.border.all(width=1, color="#D6D6D6")
        )

        contact_row = ft.Row(
            expand=True,
            controls=[self.background_contact_container, self.background_contribute_container],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls.append(self.top_text_container)
        self.controls.append(self.subtitle_text_container)
        self.controls.append(contact_row)

    def show(self, delta):
        self.offset = ft.transform.Offset(0, delta)
        self.update()
            