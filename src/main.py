import flet as ft
import config,time,widget
from outlook import sendMailData
from database import DBManager
import getdata
import datepiker

def main(page:ft.Page):
    page.title = f"{config.app('name')} v{config.app('version')}"
    page.window.min_height=640
    page.window.min_width=1024
    page.window.center()
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.theme_mode=ft.ThemeMode.SYSTEM

    def alertInitial():
        modif = DBManager().query("SELECT COUNT(*) AS count FROM dietas AS d INNER JOIN pagos AS p ON p.no_transferencia = d.no_transferencia WHERE d.estado = 'pagado' AND p.fecha_modificada IS NOT NULL AND p.fecha_modificada < DATEADD(DAY, -7, GETDATE());")

        if modif and modif[0]['count'] > 0:
            # Asegúrate de que el contenido sea un objeto de control, no una cadena
            load = widget.Modal(
                title='⚠️ Error',
                content=ft.Text(f"Tiene {modif[0]['count']} dieta(s) modifica(s) en transito por más de 7 días",size=16),
                action=[ft.TextButton('Cerrar', on_click=lambda e: page.close(load.dialog))]
                )
            page.open(load.dialog)

    # Cards informativas
    def cards():
        pagadTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado='pagado'")
        pendtTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado='pendiente'")
        noPayTotal=DBManager().query("SELECT COUNT(*) FROM vw_dietasNoPagadas")
        repeatTotal=DBManager().query("SELECT COUNT(p.no_dieta) FROM dietas d INNER JOIN pagos p ON p.no_transferencia=d.no_transferencia AND p.anno=YEAR(GETDATE()) INNER JOIN PNT_MEDIASERVER.UNE_2316A_INT.dbo.dietas_finanza df ON df.Id_Doc=p.no_dieta AND df.Ano_Doc=p.anno AND df.Anulado!='S' GROUP BY p.no_dieta HAVING COUNT(*) > 1")
        errorTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado LIKE 'error%'")

        if not repeatTotal:
            repeatTotal = 0
        else:
            repeatTotal = repeatTotal[0]['']

        return ft.ResponsiveRow(
            [
                # total Contabilizados
                ft.Card(
                    col=3,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    selected=True,
                                    selected_tile_color=ft.Colors.GREEN_50,
                                    leading=ft.Icon(ft.Icons.PAYMENTS),
                                    title=ft.Text(f"Pagadas: {pagadTotal[0]['']}",size=20, weight="bold"),
                                )
                            ]
                        ),
                        width=400,
                        padding=3,
                    ),
                    color=ft.Colors.GREEN_50
                ),

                # Pendientes
                ft.Card(
                    col=3,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    selected=True,
                                    selected_tile_color=ft.Colors.GREEN_50,
                                    leading=ft.Icon(ft.Icons.ACCESS_TIME_FILLED_OUTLINED),
                                    title=ft.Text(f"Pendientes: {pendtTotal[0]['']}",size=20, weight="bold"),
                                )
                            ]
                        ),
                        width=400,
                        padding=3
                    ),
                    color=ft.Colors.GREEN_50
                ),

                # Repetidas
                ft.Card(
                    col=3,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    selected=True,
                                    selected_tile_color=ft.Colors.GREEN_50,
                                    leading=ft.Icon(ft.Icons.DIFFERENCE),
                                    title=ft.Text(f"Duplicadas: {repeatTotal}",size=20, weight="bold"),
                                )
                            ]
                        ),
                        width=400,
                        padding=3,
                    ),
                    color=ft.Colors.GREEN_50
                ),

                # Errores
                ft.Card(
                    col=3,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    selected=True,
                                    selected_tile_color=ft.Colors.GREEN_50,
                                    leading=ft.Icon(ft.Icons.WARNING_ROUNDED),
                                    title=ft.Text(f"Errores: {errorTotal[0]['']}",size=20, weight="bold"),
                                )
                            ]
                        ),
                        width=400,
                        padding=3,
                    ),
                    color=ft.Colors.GREEN_50
                ),
            ]
        )


    # Carga las vistas
    def view(index):
        
        contents = {
            0: ft.Column(
                expand=True,
                controls=[
                    #top.build(),
                    ft.Text(config.app('fullname'), size=40, weight="bold"),
                    cards(),
                    getdata.noPagadas(page)
                ]
            ),
            1: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Dietas Contabilizadas", size=30, weight="bold"),
                    getdata.contabilizadas(page)
                ]
            ),
            2: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Dietas Pagadas", size=30, weight="bold"),
                    getdata.pagadas(page)
                ]
            ),
            3: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Dietas Pendientes", size=30, weight="bold"),
                    getdata.pendientes(page),
                ]
            ),
            4: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Dietas Duplicadas", size=30, weight="bold"),
                    getdata.repetidas(page)
                ]
            ),
            5: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Dietas con Errores", size=30, weight="bold"),
                    getdata.errores(page)
                ]
            ),
            #6: ft.Column(
            #    expand=True,
            #    controls=[
            #        ft.Text("Reportes", size=30, weight="bold"),
            #        ft.Row(
            #            [
            #                datepiker.datePiker(page)
            #            ]
            #        )
            #    ]
            #)
        }
        return contents[index]


    container=ft.Container(
        content=view(0),
        padding=20,
        expand=True
    )

    # Update data
    def update(e):
        load=widget.Modal('⌛ Espere un momento...')
        page.open(load.dialog)
        try:
            sendMailData()
            time.sleep(2)
            page.close(load.dialog)
            #actualiza la vista
            container.content = view(view_index)  # Actualiza el contenido del contenedor
            page.update()
        except Exception as th:
            page.close(load.dialog)

            if th==0:
                modal=widget.Modal(
                    title="⚠️ Error",
                    content=ft.Text(f"{str(th)}"),
                    action=[ft.TextButton('Cerrar', on_click=lambda e: page.close(modal.dialog))]
                )
                page.open(modal.dialog)

    def navigation(e):
        global view_index
        view_index=e.control.selected_index
        container.content = view(e.control.selected_index)
        page.update()

    #page.floating_action_button = ft.FloatingActionButton(
    #    icon=ft.Icons.SEARCH,
    #    bgcolor=ft.Colors.GREEN_100,
    #    data=0,
    #)

    alertInitial()
    page.add(
        ft.Row(
            [
                widget.sidebar(navigation,update),
                ft.VerticalDivider(width=1),
                container
            ],
            expand=True
        )
    )


if __name__ == '__main__':
    # Busca e inserta los datos al inicializarce
    sendMailData()

    ft.app(main)