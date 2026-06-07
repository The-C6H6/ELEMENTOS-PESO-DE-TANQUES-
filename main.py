import flet as ft
from UI import dropdown_tanque, dropdown_placa_horizontal_vertical, distribucion_pagina


def main(page: ft.Page):
    page.title = "Calculadora de Peso de tanques"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
      
    tanque_p={
        "tanque:":{"Tipo":"P", "Diametro":None, "Altura":None, "S":None, "E":None, "C":None},
        "placa:":{"Espesor":None, "Orientacion":None},
        

    }

    tanque_atmosferico={
        "tanque:":{"Tipo":"Patm", "Diametro":None, "Altura":None, "Anillos":None},
        "placa:":{"Espesor":None, "Orientacion":None},


    }

    

    elementos_UI={
        "dropdown_Tipo_de_tanque":dropdown_tanque(),
        "dropdown_Placa horizontal o vertical": dropdown_placa_horizontal_vertical(),
        "imagen_tanque":ft.Image(src="./assets/tanque.png", width=300, height=300),
        "imagen_placa":ft.Image(src="./assets/placa horizontal.png", width=265, height=265),
        "pagina":page
    }

    distribucion_pagina(page, elementos_UI)






if __name__ == "__main__":
    ft.run(main)