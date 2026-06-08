import flet as ft




def agregar_pasos(elementos_UI, pasos: list[dict]):
    """
    pasos = [
        {"formula": "V = π × r² × h", "valor": "= 3.1416 × (0.5)² × 2.0", "resultado": "= 1.571 m³"},
        {"formula": "m_cuerpo = ρ × V_acero", "valor": "= 7850 × 0.032", "resultado": "= 251.2 kg"},
    ]
    """
    col = elementos_UI["columna_pasos"]
    col.controls.clear()

    for i, paso in enumerate(pasos, 1):
        col.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(controls=[
                            ft.Container(
                                content=ft.Text(str(i), size=11, color="white", weight=ft.FontWeight.BOLD),
                                bgcolor="#7C3AED",
                                border_radius=50,
                                width=22, height=22,
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Text(paso["formula"], size=13, color="#1E1B4B", weight=ft.FontWeight.BOLD),
                        ], spacing=8),
                        ft.Text(paso["valor"],     size=12, color="#4B5563"),
                        ft.Text(paso["resultado"], size=13, color="#2563EB", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=2,
                ),
                bgcolor="white",
                border_radius=8,
                padding=12,
                shadow=ft.BoxShadow(blur_radius=4, color="#7C3AED11", offset=ft.Offset(0, 2)),
            )
        )

    elementos_UI["pagina"].update()


def boton_calcular():
    return ft.Button(content="Calcular", width=300, height=40, bgcolor="#007bff", color="white", 
                     )





