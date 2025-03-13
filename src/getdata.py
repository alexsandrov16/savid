import flet as ft
import config,time
from database import DBManager
from datetime import datetime

def dataNotFound():
    return ft.Text('No hay datos para mostrar', size=25, text_align=ft.TextAlign.CENTER)
    # Texto de datos no encontrados

'''
DATOS DE DIETAS CONTABILIZADAS
'''
def contabilizadas(page):
    datos = DBManager().get_all_data('vw_dietasContabilizadas')
    rows = []

    if not datos:
        return dataNotFound()

    # Crear el DataTable
    data_table = ft.DataTable(
        width=page.width,
        columns=[
            ft.DataColumn(ft.Text("Dieta")),
            ft.DataColumn(ft.Text("Transferencia")),
            ft.DataColumn(ft.Text("Importe")),
            ft.DataColumn(ft.Text("Cuenta")),
            ft.DataColumn(ft.Text("Beneficiario")),
            ft.DataColumn(ft.Text("Realizado por")),
            ft.DataColumn(ft.Text("Contabilizado por")),
            ft.DataColumn(ft.Text("Usuario")),
            ft.DataColumn(ft.Text("Emitida")),
            ft.DataColumn(ft.Text("Pagada")),
        ],
        rows=[]  # Inicialmente vacío
    )

    for p in datos:
        fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
        fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
        importe=f"{p['importe']:.2f}"
        data_table.rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(p['dieta']))),
            ft.DataCell(ft.Text(str(p['br']))),
            ft.DataCell(ft.Text(importe)),
            ft.DataCell(ft.Text(str(p['destino']))),
            ft.DataCell(ft.Text(str(p['beneficiario']))),
            ft.DataCell(ft.Text(str(p['paga']))),  
            ft.DataCell(ft.Text(str(p['contabiliza']))),
            ft.DataCell(ft.Text(str(p['usuario']))),
            ft.DataCell(ft.Text(fecha_d)),
            ft.DataCell(ft.Text(fecha_p)),
        ],on_select_changed=True
        ))

    def searchNoDieta(e):
        search_diet=f"Dieta-{e.control.value.upper()}"
        filt=list(filter(lambda x: str(x['dieta']) == search_diet, datos))

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        page.update()

    def searchBR(e):
        search_br = e.control.value.upper()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_br in str(x['br']).upper(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        page.update()

    def searchCuenta(e):
        search_account = e.control.value
        filt = list(filter(lambda x: search_account in str(x['destino']), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        page.update()

    def searchbeneficia(e):
        search_beneficiary = e.control.value.lower()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_beneficiary in str(x['beneficiario']).lower(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_d = datetime.strptime(str(p['fecha_dieta']), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                fecha_p = datetime.strptime(str(p['fecha_transferencia']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),
                    ft.DataCell(ft.Text(str(p['br']))),
                    ft.DataCell(ft.Text(importe)),
                    ft.DataCell(ft.Text(str(p['destino']))),
                    ft.DataCell(ft.Text(str(p['beneficiario']))),
                    ft.DataCell(ft.Text(str(p['paga']))),  
                    ft.DataCell(ft.Text(str(p['contabiliza']))),
                    ft.DataCell(ft.Text(str(p['usuario']))),
                    ft.DataCell(ft.Text(fecha_d)),
                    ft.DataCell(ft.Text(fecha_p)),
                ],on_select_changed=True
                ))
        page.update()


    return ft.Column(
        expand=True,
        controls=[
            ft.ResponsiveRow(
                #expand=True,
                controls=[
                    ft.TextField(
                        col=2,
                        label='No. Dieta',
                        on_change=searchNoDieta
                    ),
                    ft.TextField(
                        col=2,
                        label='No. Transferencia',
                        on_change=searchBR
                    ),
                    ft.TextField(
                        col=2,
                        label='Cuenta',
                        on_change=searchCuenta
                    ),
                    ft.TextField(
                        col=2,
                        label='Beneficiario',
                        on_change=searchbeneficia
                    )
                ],vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                [
                    data_table
                ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
            )
        ]
    )

'''
DATOS DE DIETAS PAGADAS
'''
def pagadas(page):
    rows = []
    datos = DBManager().query("SELECT p.no_dieta as dieta, d.fecha AS pagado, p.fecha_modificada AS modificado, d.no_transferencia, d.importe, d.cuenta_destino, d.beneficiario, d.operador FROM dietas AS d INNER JOIN pagos AS p ON p.no_transferencia = d.no_transferencia WHERE d.estado = 'pagado' ORDER BY d.fecha DESC;")

    if not datos:
        return dataNotFound()


    # Crear el DataTable
    data_table = ft.DataTable(
        width=page.width,
        columns=[
            ft.DataColumn(ft.Text("No. Dieta")),
            ft.DataColumn(ft.Text("Transferencia")),
            ft.DataColumn(ft.Text("Importe")),
            ft.DataColumn(ft.Text("Cuenta")),
            ft.DataColumn(ft.Text("Beneficiario")),
            ft.DataColumn(ft.Text("Realizado por")),
            ft.DataColumn(ft.Text("Pagado")),
            ft.DataColumn(ft.Text("Modificado")),
        ],
        rows=[]  # Inicialmente vacío
    )

    for p in datos:
        fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

        #fecha_mod_db = str(p['modificado'])
        if p['modificado'] is None:
            fecha_m = "No"
        else:
            fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

        importe=f"{p['importe']:.2f}"


        data_table.rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
            ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
            ft.DataCell(ft.Text(importe)),  # Importe
            ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
            ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
            ft.DataCell(ft.Text(str(p['operador']))),  # Operador
            ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
            ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
        ],on_select_changed=True
        ))

    def searchNoDieta(e):
        search_diet=f"Dieta-{e.control.value.upper()}"
        filt=list(filter(lambda x: str(x['dieta']) == search_diet, datos))

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        page.update()

    def searchBR(e):
        search_br = e.control.value.upper()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_br in str(x['no_transferencia']).upper(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        page.update()

    def searchCuenta(e):
        search_account = e.control.value
        filt = list(filter(lambda x: search_account in str(x['cuenta_destino']), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        page.update()

    def searchbeneficia(e):
        search_beneficiary = e.control.value.lower()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_beneficiary in str(x['beneficiario']).lower(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha_p = datetime.strptime(str(p['pagado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                #fecha_mod_db = str(p['modificado'])
                if p['modificado'] is None:
                    fecha_m = "No"
                else:
                    fecha_m = datetime.strptime(str(p['modificado']), "%Y-%m-%d").strftime("%d-%m-%Y")

                importe=f"{p['importe']:.2f}"


                data_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p['dieta']))),  # No. Dieta
                    ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                    ft.DataCell(ft.Text(importe)),  # Importe
                    ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                    ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                    ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ft.DataCell(ft.Text(fecha_p)),  # Fecha transferencia
                    ft.DataCell(ft.Text(fecha_m)),  # Fecha transferencia
                ],on_select_changed=True
                ))
        page.update()


    return ft.Column(
        expand=True,
        controls=[
            ft.ResponsiveRow(
                #expand=True,
                controls=[
                    ft.TextField(
                        col=2,
                        label='No. Dieta',
                        on_change=searchNoDieta
                    ),
                    ft.TextField(
                        col=2,
                        label='No. Transferencia',
                        on_change=searchBR
                    ),
                    ft.TextField(
                        col=2,
                        label='Cuenta',
                        on_change=searchCuenta
                    ),
                    ft.TextField(
                        col=2,
                        label='Beneficiario',
                        on_change=searchbeneficia
                    )
                ],vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                [
                    data_table
                ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
            )
        ]
    )

'''
DATOS DE DIETAS PENDIENTES
'''
def pendientes(page):
    rows = []
    datos = DBManager().query("SELECT * FROM dietas WHERE estado='pendiente' ORDER BY fecha_correo DESC")

    if not datos:
        return dataNotFound()

    # Crear el DataTable
    data_table = ft.DataTable(
        width=page.width,
        columns=[
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Transferencia")),
            ft.DataColumn(ft.Text("Importe")),
            ft.DataColumn(ft.Text("Cuenta")),
            ft.DataColumn(ft.Text("Beneficiario")),
            ft.DataColumn(ft.Text("Realizado por")),
        ],
        rows=[]  # Inicialmente vacío
    )

    for p in datos:
        fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
        importe=f"{p['importe']:.2f}"
        data_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                ft.DataCell(ft.Text(importe)),  # Importe
                ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                ft.DataCell(ft.Text(str(p['operador']))),  # Operador
            ],on_select_changed=True
        ))

    def searchBR(e):
        search_br = e.control.value.upper()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_br in str(x['no_transferencia']).upper(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        page.update()

    def searchCuenta(e):
        search_account = e.control.value
        filt = list(filter(lambda x: search_account in str(x['cuenta_destino']), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        page.update()

    def searchbeneficia(e):
        search_beneficiary = e.control.value.lower()  # Convierte a minúsculas para comparación
        filt = list(filter(lambda x: search_beneficiary in str(x['beneficiario']).lower(), datos))  # Filtra por coincidencias

        data_table.rows = []  # Limpia las filas actuales

        if not e.control.value=='':
            # Actualiza el DataTable con los datos filtrados
            for p in filt:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        else:
            for p in datos:
                fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
                importe=f"{p['importe']:.2f}"
                data_table.rows.append(ft.DataRow(cells=[
                        ft.DataCell(ft.Text(fecha)),  # Fecha transferencia
                        ft.DataCell(ft.Text(str(p['no_transferencia']))),  # No Transferencia
                        ft.DataCell(ft.Text(importe)),  # Importe
                        ft.DataCell(ft.Text(str(p['cuenta_destino']))),  # Cuenta Destino
                        ft.DataCell(ft.Text(str(p['beneficiario']))),  # Beneficiario
                        ft.DataCell(ft.Text(str(p['operador']))),  # Operador
                    ],on_select_changed=True
                ))
        page.update()


    return ft.Column(
        expand=True,
        controls=[
            ft.ResponsiveRow(
                #expand=True,
                controls=[
                    
                    ft.TextField(
                        col=2,
                        label='No. Transferencia',
                        on_change=searchBR
                    ),
                    ft.TextField(
                        col=2,
                        label='Cuenta',
                        on_change=searchCuenta
                    ),
                    ft.TextField(
                        col=2,
                        label='Beneficiario',
                        on_change=searchbeneficia
                    )
                ],vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                [
                    data_table
                ],
            expand=True,
            scroll=ft.ScrollMode.AUTO
            )
        ]
    )

'''
DATOS DE DIETAS NO PAGADAS
'''
def noPagadas(page):
    rows = []
    datos = DBManager().get_all_data('vw_dietasNoPagadas')

    if not datos:
        return dataNotFound()

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
            ft.Text('Dietas sin constancia de pago',size=28, weight="bold"),
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

'''
DATOS DE DIETAS CON ERRORES
'''
def errores(page):
        rows = []
        datos = DBManager().query("SELECT * FROM dietas WHERE estado LIKE 'error%'")

        if not datos:
            return dataNotFound()

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

'''
DATOS DE DIETAS REPETIDAS
'''
def repetidas(page):
    rows = []
    datos = DBManager().get_all_data('vw_dietasDuplicadas')

    if not datos:
        return dataNotFound()

    for p in datos:
        # Convertir la cadena a un objeto datetime
        fecha = datetime.strptime(str(p['fecha']), "%Y-%m-%d").strftime("%d-%m-%Y")
        importe = f"{p['importe']:.2f}"
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(p['dieta']))),
            ft.DataCell(ft.Text(str(p['br']))),
            ft.DataCell(ft.Text(importe)),
            ft.DataCell(ft.Text(str(p['beneficiario']))),
            ft.DataCell(ft.Text(str(p['paga']))),
            ft.DataCell(ft.Text(str(p['estado']))),
            ft.DataCell(ft.Text(fecha)),
        ], on_select_changed=True))

    # Crear la tabla
    data_table = ft.DataTable(
        width=page.width,
        columns=[
                    ft.DataColumn(ft.Text("Dieta")),
                    ft.DataColumn(ft.Text("Transferencia")),
                    ft.DataColumn(ft.Text("Importe")),
                    ft.DataColumn(ft.Text("Destino")),
                    ft.DataColumn(ft.Text("Realizado por")),
                    ft.DataColumn(ft.Text("Estado")),
                    ft.DataColumn(ft.Text("Fecha")),
            ],
        rows=rows
    )

    # Contenedor con scroll
    return ft.Column(
        [
            data_table
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )
