import datetime
import flet as ft


def datePiker(page):
    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    now = datetime.datetime.now()
    # Extraer año, mes y día
    year = now.year
    month = now.month
    day = now.day

    return ft.ElevatedButton(
        "Pick date",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2025, month=1, day=1),
                last_date=datetime.datetime(year=year, month=month, day=day),
                on_change=lambda e: handle_change(e),
                #on_dismiss=lambda e: handle_dismissal(e),
            )
        ),
    )
