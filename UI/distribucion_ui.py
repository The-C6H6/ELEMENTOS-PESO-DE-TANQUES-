import flet as ft


def distribucion_pagina(page, elementos_UI):
    page.padding = 30
   

    page.add(
        ft.Row(
            controls=[
                # Columna izquierda - Controles
                ft.Container(
                    height=400,
                    width=400,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Calculadora de Peso de Tanques",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color='white',
                            ),
                            ft.Divider(height=1, color="#E0E0E0"),
                            ft.Text("Tipo de tanque", size=13, color="#666"),
                            elementos_UI["dropdown_Tipo_de_tanque"],
                            ft.Text("Orientación de la placa", size=13, color="#666"),
                            elementos_UI["dropdown_Placa horizontal o vertical"],
                        ],
                        spacing=10,
                    ),
                    bgcolor="#1A1A2E",
                    border_radius=12,
                    padding=24,
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#00000018",
                        offset=ft.Offset(0, 3),
                        
                    ),
                    expand=1,
                ),

                # Columna derecha - Imágenes
                ft.Container(
                    height=400,
                    width=400,
                    content=ft.Row(
                        controls=[
                            elementos_UI["imagen_tanque"],
                            elementos_UI["imagen_placa"],
                        ],
                        spacing=1,
                        
                    ),
                    bgcolor="#1A1A2E",
                    border_radius=12,
                    padding=24,
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#00000018",
                        offset=ft.Offset(0, 3),
                    ),
                    expand=1,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )