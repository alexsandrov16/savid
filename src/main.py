import flet as ft
import config,time,widget
from outlook import sendMailData
from database import DBManager
from datetime import datetime



def main(page:ft.Page):
    page.title = f"{config.app('name')} v{config.app('version')}"
    page.window.min_height=640
    page.window.min_width=1024
    page.window.center()
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.theme_mode=ft.ThemeMode.SYSTEM


    def contabilizadas():
        datos = DBManager().get_all_data('vw_dietasContabilizadas')
        rows = []

        if not datos:
            return ft.Text('No hay datos para mostrar', size=25, text_align=ft.TextAlign.CENTER)
        #for p in DBManager().get_all_data('vw_dietasNoPagadas'):
        #    rows.append(ft.DataRow(cells=[
        #        ft.DataCell(ft.Text(str(p[0]))),  # Primera columna
        #       ft.DataCell(ft.Text(str(p[1]))),  # Segunda columna
        #    ]))

        #return rows


    def pagadas():
        datos = DBManager().query("SELECT * FROM dietas WHERE estado='pagado' ORDER BY fecha_correo DESC")
        rows = []
        
        if not datos:
            return ft.Text('No hay datos para mostrar', size=25, text_align=ft.TextAlign.CENTER)

        for p in datos:
            fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
            importe=f"{p['importe']:.2f}"
            rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                ft.DataCell(ft.Text(importe)),  # Importe
                ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                ft.DataCell(ft.Text(str(p['operador']))),  # Operador
            ],on_select_changed=lambda e: show_details(p,'pendiente')
            ))

        return ft.Column(
            [
                ft.DataTable(
                    width=page.width,
                    columns=[
                        ft.DataColumn(ft.Text("Fecha")),
                        ft.DataColumn(ft.Text("Transferencia")),
                        ft.DataColumn(ft.Text("Importe")),
                        ft.DataColumn(ft.Text("Cuenta")),
                        ft.DataColumn(ft.Text("Beneficiario")),
                        ft.DataColumn(ft.Text("Realizado por")),
                    ],
                    rows=rows
                )
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

    def pendientes():
        rows = []
        datos = DBManager().query("SELECT * FROM dietas WHERE estado='pendiente' ORDER BY fecha_correo DESC")

        if not datos:
            return ft.Text('No hay datos para mostrar', size=25, text_align=ft.TextAlign.CENTER)

        for p in datos:
            fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
            importe=f"{p['importe']:.2f}"
            rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                ft.DataCell(ft.Text(importe)),  # Importe
                ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                ft.DataCell(ft.Text(str(p['operador']))),  # Operador
            ],on_select_changed=True
            #],on_select_changed=lambda e: show_details(p,'pendiente')
            ))

        return ft.Column(
            [
                ft.DataTable(
                    
                    width=page.width,
                    columns=[
                        ft.DataColumn(ft.Text("Fecha")),
                        ft.DataColumn(ft.Text("Transferencia")),
                        ft.DataColumn(ft.Text("Importe")),
                        ft.DataColumn(ft.Text("Cuenta")),
                        ft.DataColumn(ft.Text("Beneficiario")),
                        ft.DataColumn(ft.Text("Realizado por")),
                    ],
                    rows=rows
                )
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

    def noPagadas():
        rows = []
        datos = DBManager().get_all_data('vw_dietasNoPagadas')

        if not datos:
            return ft.Text()

        for p in datos:
            # Convertir la cadena a un objeto datetime
            fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
            importe = f"{p['importe']:.2f}"
            rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(p['dieta']))),
                ft.DataCell(ft.Text(importe)),
                ft.DataCell(ft.Text(str(p['destino']))),
                ft.DataCell(ft.Text(str(p['contabiliza']))),
                ft.DataCell(ft.Text(str(p['usuario']))),
                ft.DataCell(ft.Text(fecha)),
            ], on_select_changed=True))

        # Crear la tabla
        data_table = ft.DataTable(
            width=page.width,
            columns=[
                        ft.DataColumn(ft.Text("Dieta")),
                        ft.DataColumn(ft.Text("Importe")),
                        ft.DataColumn(ft.Text("Destino")),
                        ft.DataColumn(ft.Text("Contabilizado")),
                        ft.DataColumn(ft.Text("Usuario")),
                        ft.DataColumn(ft.Text("Fecha")),
                ],
            rows=rows
        )

        # Contenedor con scroll
        return ft.Column(
            [
                ft.Text('Dietas no pagadas',size=28, weight="bold"),
                ft.Column(
                    [
                        data_table,
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                )
            ],
            expand=True
        )

    def errores():
        rows = []
        datos = DBManager().query("SELECT * FROM dietas WHERE estado LIKE 'error%'")

        if not datos:
            return ft.Text('No hay datos para mostrar', size=25, text_align=ft.TextAlign.CENTER)

        for p in datos:
            fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
            importe=f"{p['importe']:.2f}"
            rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                ft.DataCell(ft.Text(importe)),  # Importe
                ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                ft.DataCell(ft.Text(str(p['estado']))),  # Estado
                ft.DataCell(ft.Text(str(p['operador']))),  # Operador
            ],on_select_changed=True
            #],on_select_changed=lambda e: show_details(p,'pendiente')
            ))

        return ft.Column(
            [
                ft.DataTable(
                    
                    width=page.width,
                    columns=[
                        ft.DataColumn(ft.Text("Fecha")),
                        ft.DataColumn(ft.Text("Transferencia")),
                        ft.DataColumn(ft.Text("Importe")),
                        ft.DataColumn(ft.Text("Cuenta")),
                        ft.DataColumn(ft.Text("Beneficiario")),
                        ft.DataColumn(ft.Text("Estado")),
                        ft.DataColumn(ft.Text("Realizado por")),
                    ],
                    rows=rows
                )
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

    # Cards informativas
    def cards():
        pagadTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado='pagado'")
        pendtTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado='pendiente'")
        noPayTotal=DBManager().query("SELECT COUNT(*) FROM vw_dietasNoPagadas")
        errorTotal=DBManager().query("SELECT COUNT(*) FROM dietas WHERE estado LIKE 'error%'")

        return ft.ResponsiveRow(
            [
                # total Contabilizados
                ft.Card(
                    col=4,
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
                        padding=10,
                    ),
                    color=ft.Colors.GREEN_50
                ),

                ft.Card(
                    col=4,
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
                        padding=10,
                    ),
                    color=ft.Colors.GREEN_50
                ),

                # Errores
                ft.Card(
                    col=4,
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
                        padding=10,
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
                    noPagadas()
                ]
            ),
            1: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Contabilizados", size=30, weight="bold"),
                    contabilizadas()
                ]
            ),
            2: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Pagados", size=30, weight="bold"),
                    pagadas()
                ]
            ),
            3: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Pendientes", size=30, weight="bold"),
                    pendientes(),
                ]
            ),
            4: ft.Column(
                expand=True,
                controls=[
                    ft.Text("Errores", size=30, weight="bold"),
                    errores()
                ]
            )
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


ft.app(main)