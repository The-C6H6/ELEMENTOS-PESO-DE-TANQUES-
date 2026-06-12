import flet as ft

def distribucion_pagina(page, elementos_UI):
    page.padding = 30
    page.bgcolor = "#EEF2FF"

    # ── Header ──────────────────────────────────────────────────────────────
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.PROPANE_TANK_OUTLINED, color="white", size=28),
                ft.Text("Calculadora de Peso de Tanques", size=22, weight=ft.FontWeight.BOLD, color="white"),
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

    # ── Panel controles ──────────────────────────────────────────────────────
    panel_controles = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Parámetros del tanque", size=15, weight=ft.FontWeight.BOLD, color="#2563EB"),
                ft.Divider(height=1, color="#BFDBFE"),
                ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["dropdown_Tipo_de_tanque"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["dropdown_Placa horizontal o vertical"]], spacing=4, expand=1),
                ], spacing=16),

                #Modificado
                ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["dropdown_eficiencia_soldadura"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["Material"]], spacing=4, expand=1),
                ], spacing=16),

                 ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["densidad_fluido"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["dropdown_norma"]], spacing=4, expand=1),
                ], spacing=16),

                ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["dropdown_cabezal"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["dropdown_tipo_fondo"]], spacing=4, expand=1),
                ], spacing=16),


                ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["diametro_tanque"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["altura_tanque"]], spacing=4, expand=1),
                ], spacing=16),
                ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["fatiga_material"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["Presion_operacion"]], spacing=4, expand=1),
                    
                ], spacing=16),

                    ft.Row(controls=[
                    ft.Column(controls=[elementos_UI["angulo_cabezal"]], spacing=4, expand=1),
                    ft.Column(controls=[elementos_UI["angulo_fondo"]], spacing=4, expand=1),
                    
                ], spacing=16),





                ft.Container(height=10),
                elementos_UI["boton_calcular"],
            ],
            spacing=14,
        ),
        bgcolor="white", border_radius=14, padding=24,
        shadow=ft.BoxShadow(blur_radius=16, color="#2563EB22", offset=ft.Offset(0, 4)),
        expand=1,
    )

    # ── Panel imágenes ───────────────────────────────────────────────────────
    panel_imagenes = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Vista previa", size=15, weight=ft.FontWeight.BOLD, color="#2563EB"),
                ft.Divider(height=1, color="#BFDBFE"),
                ft.Container(
                    content=ft.Row(
                        controls=[elementos_UI["imagen_tanque"], elementos_UI["imagen_placa"]],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=16,
                    ),
                    bgcolor="#EFF6FF", border_radius=10, padding=20, expand=True,
                ),
            ],
            spacing=12, expand=True,
        ),
        bgcolor="white", border_radius=14, padding=24,
        shadow=ft.BoxShadow(blur_radius=16, color="#2563EB22", offset=ft.Offset(0, 4)),
        expand=1,
    )

    # ── Panel resultados ─────────────────────────────────────────────────────
    elementos_UI["resultado_peso_total"]   = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_peso_cuerpo"]  = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_peso_cabezal"] = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_peso_fondo"]   = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_volumen"]      = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_espesor"]      = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    elementos_UI["resultado_peso_fluido"]  = ft.Text("—", size=13, color="#111827", weight=ft.FontWeight.BOLD, expand=1)
    def fila_resultado(label, control, es_par):
        return ft.Container(
            content=ft.Row(controls=[
                ft.Text(label, size=13, color="#374151", expand=2),
                control,
            ]),
            bgcolor="#F0F4FF" if es_par else "white",
            padding=ft.Padding.symmetric(horizontal=16, vertical=10),
            border_radius=6,
        )

    panel_resultados = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[
                    ft.Icon(ft.Icons.CALCULATE_OUTLINED, color="#2563EB", size=20),
                    ft.Text("Resultados del cálculo", size=15, weight=ft.FontWeight.BOLD, color="#2563EB"),
                ], spacing=8),
                ft.Divider(height=1, color="#BFDBFE"),
                ft.Container(
                    content=ft.Row(controls=[
                        ft.Text("Parámetro", size=12, weight=ft.FontWeight.BOLD, color="#6B7280", expand=2),
                        ft.Text("Valor",     size=12, weight=ft.FontWeight.BOLD, color="#6B7280", expand=1),
                    ]),
                    padding=ft.Padding.symmetric(horizontal=16, vertical=6),
                ),
                fila_resultado("Peso total del tanque (kg)",  elementos_UI["resultado_peso_total"],   True),
                fila_resultado("Peso del fluido (kg)",       elementos_UI["resultado_peso_fluido"],      False),
                fila_resultado("Peso del cuerpo (kg)",        elementos_UI["resultado_peso_cuerpo"],  True),
                fila_resultado("Peso del cabezal (kg)",       elementos_UI["resultado_peso_cabezal"], False),
                fila_resultado("Peso del fondo (kg)",         elementos_UI["resultado_peso_fondo"],   True),
                fila_resultado("Volumen del tanque (ft³)",     elementos_UI["resultado_volumen"],      False),
                
                #fila_resultado("Espesor de pared (in)",       elementos_UI["resultado_espesor"],      True),
                
            ],
            spacing=4,
        ),
        bgcolor="white", border_radius=14, padding=24,
        margin=ft.Margin.only(top=20),
        shadow=ft.BoxShadow(blur_radius=16, color="#2563EB22", offset=ft.Offset(0, 4)),
    )

    # ── Panel paso a paso ────────────────────────────────────────────────────

    # Columna donde se inyectarán los pasos al calcular
    elementos_UI["columna_pasos"] = ft.Column(
        expand=1,
        controls=[
            ft.Text(
                "Los pasos aparecerán aquí después de calcular.",
                size=13,
                color="#9CA3AF",
                italic=True,
            )
        ],
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
    )

    panel_pasos = ft.Container(
        content=ft.Column(
            expand=1,   
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Row(controls=[
                    ft.Icon(ft.Icons.FUNCTIONS, color="#7C3AED", size=20),
                    ft.Text("Desarrollo del cálculo", size=15, weight=ft.FontWeight.BOLD, color="#7C3AED"),
                ], spacing=8),
                ft.Divider(height=1, color="#DDD6FE"),
                ft.Container(
                    content=elementos_UI["columna_pasos"],
                    height=320,
                    expand=True,
                    bgcolor="#FAFAFF",
                    border_radius=8,
                    padding=16,
                ),
            ],
            spacing=12,
        ),
        bgcolor="white", border_radius=14, padding=24,
        margin=ft.Margin.only(top=20),
        shadow=ft.BoxShadow(blur_radius=16, color="#7C3AED22", offset=ft.Offset(0, 4)),
        expand=True,
    )

    # ── Layout principal ─────────────────────────────────────────────────────
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
                panel_resultados,
                panel_pasos,
            ],
            expand=True,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )
    )














