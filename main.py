import flet as ft
from UI import dropdown_tanque, dropdown_placa_horizontal_vertical, distribucion_pagina


def main(page: ft.Page):
    page.title = "Calculadora de Peso de tanques"
    page.window_width = 950
    page.window_height = 850
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
      
    almacen_variables={
    }

    elementos_UI={
        "dropdown_Tipo_de_tanque":dropdown_tanque(),
        "dropdown_Placa horizontal o vertical":dropdown_placa_horizontal_vertical(),
        "imagen_tanque":ft.Image(src="./assets/tanque.png", width=400, height=400),
    }

    distribucion_pagina(page, elementos_UI)






if __name__ == "__main__":
    ft.run(main)