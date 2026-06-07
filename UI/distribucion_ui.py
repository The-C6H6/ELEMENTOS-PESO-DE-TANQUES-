import flet as ft


def distribucion_pagina(page, elementos_UI):
    page.padding = 30
    page.bgcolor = "#EEF2FF"

    # Header superior
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.PROPANE_TANK_OUTLINED, color="white", size=28),
                ft.Text(
                    "Calculadora de Peso de Tanques",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
            ],
            spacing=12,
        ),
        gradient=ft.LinearGradient(
            begin=ft.Alignment.CENTER_LEFT,
            end=ft.Alignment.CENTER_RIGHT,
            colors=["#2563EB", "#7C3AED"],
        ),
        border_radius=14,
        padding=18,
        margin=ft.Margin.only(bottom=20),
    )

    # Columna izquierda - Controles
    panel_controles = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Parámetros del tanque",
                    size=15,
                    weight=ft.FontWeight.BOLD,
                    color="#2563EB",
                ),
                ft.Divider(height=1, color="#BFDBFE"),
                ft.Text("Tipo de tanque", size=12, color="#6B7280"),
                elementos_UI["dropdown_Tipo_de_tanque"],
                ft.Text("Orientación de la placa", size=12, color="#6B7280"),
                elementos_UI["dropdown_Placa horizontal o vertical"],
                ft.Text("Diámetro del tanque", size=12, color="#6B7280"),
                elementos_UI["diametro_tanque"],
                ft.Text("Altura del tanque", size=12, color="#6B7280"),
                elementos_UI["altura_tanque"],
                ft.Text("Presión de operación", size=12, color="#6B7280"),
                elementos_UI["Presion_operacion"],
                ft.Container(height=10),
                elementos_UI["boton_calcular"],
            ],
            spacing=8,
        ),
        bgcolor="white",
        border_radius=14,
        padding=24,
        shadow=ft.BoxShadow(
            blur_radius=16,
            color="#2563EB22",
            offset=ft.Offset(0, 4),
        ),
        expand=1,
    )

    # Columna derecha - Imágenes
    panel_imagenes = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Vista previa",
                    size=15,
                    weight=ft.FontWeight.BOLD,
                    color="#2563EB",
                ),
                ft.Divider(height=1, color="#BFDBFE"),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            elementos_UI["imagen_tanque"],
                            elementos_UI["imagen_placa"],
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=16,
                    ),
                    bgcolor="#EFF6FF",
                    border_radius=10,
                    padding=20,
                    expand=True,
                ),
            ],
            spacing=12,
            expand=True,
        ),
        bgcolor="white",
        border_radius=14,
        padding=24,
        shadow=ft.BoxShadow(
            blur_radius=16,
            color="#2563EB22",
            offset=ft.Offset(0, 4),
        ),
        expand=1,
    )

    page.add(
        ft.Column(
            controls=[
                header,
                ft.Row(
                    controls=[panel_controles, panel_imagenes],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
            spacing=0,
        )
    )