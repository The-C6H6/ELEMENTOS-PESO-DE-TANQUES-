import flet as ft


def distribucion_pagina(page, elementos_UI):
        page.add(
        ft.Text("Seleccione el tipo de tanque:"),
        elementos_UI["dropdown_Tipo_de_tanque"],
        ft.Text("Seleccione la orientación de la placa:"),
        elementos_UI["dropdown_Placa horizontal o vertical"],
        elementos_UI["imagen_tanque"],
    )