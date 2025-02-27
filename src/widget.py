import flet as ft

class Modal:
    def __init__(self,content,title=None,action=[],modal=True):
        if title==None:
            self.dialog = ft.AlertDialog(
                modal=modal,
                title=ft.Text(content),
                actions=action,
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda e: page.add(
                #    ft.Text("Modal dialog dismissed"),
                #),
                inset_padding=ft.padding.symmetric(horizontal=40)
            )
        else:
            self.dialog = ft.AlertDialog(
                modal=modal,
                title=ft.Text(title),
                content=ft.Text(content),
                actions=action,
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda e: page.add(
                #    ft.Text("Modal dialog dismissed"),
                #),
                inset_padding=ft.padding.symmetric(horizontal=40)
            )