from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Función para exportar a PDF
def exportar_a_pdf(header,data, nombre_archivo):
    pdf = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    elements = []

    # Crear la tabla
    table_data = [header]# [["Nombre", "Edad"]]  Encabezados
    for row in data:
        table_data.append([row["Nombre"], row["Edad"]])

    table = Table(table_data)

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    elements.append(table)
    pdf.build(elements)

# Función principal de Flet
def main(page):
    data = [
        {"Nombre": "Alice", "Edad": 24},
        {"Nombre": "Bob", "Edad": 30},
        {"Nombre": "Charlie", "Edad": 22},
    ]

    # Crear el DataTable en Flet
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Edad")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(row["Nombre"])),
                ft.DataCell(ft.Text(row["Edad"])),
            ]) for row in data
        ]
    )

    # Botón para exportar a PDF
    export_button = ft.ElevatedButton("Exportar a PDF", on_click=lambda e: exportar_a_pdf(data, "datattable.pdf"))

    page.add(table, export_button)

# Ejecutar la aplicación Flet
ft.app(target=main)