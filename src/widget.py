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
                content=content,
                actions=action,
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda e: page.add(
                #    ft.Text("Modal dialog dismissed"),
                #),
                inset_padding=ft.padding.symmetric(horizontal=40)
            )

# Navegación
def sidebar(navigation,update):
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        group_alignment=-0.8,
        leading=ft.FloatingActionButton(icon=ft.Icons.UPDATE, text="Actualizar",on_click=update),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.DASHBOARD
            ),ft.NavigationRailDestination(
                icon=ft.Icons.ACCOUNT_BALANCE_OUTLINED,
                selected_icon=ft.Icons.ACCOUNT_BALANCE
            ),ft.NavigationRailDestination(
                icon=ft.Icons.PAYMENTS_OUTLINED,
                selected_icon=ft.Icons.PAYMENTS
            ),ft.NavigationRailDestination(
                icon=ft.Icons.ACCESS_TIME,
                selected_icon=ft.Icons.ACCESS_TIME_FILLED_OUTLINED
            ),ft.NavigationRailDestination(
                icon=ft.Icons.DIFFERENCE_OUTLINED,
                selected_icon=ft.Icons.DIFFERENCE
            ),ft.NavigationRailDestination(
                icon=ft.Icons.WARNING_AMBER_ROUNDED,
                selected_icon=ft.Icons.WARNING_ROUNDED
            )
        ],
        on_change=lambda e: navigation(e)
    )