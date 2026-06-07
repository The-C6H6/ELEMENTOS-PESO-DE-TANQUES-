import flet as ft
from UI import dropdown_tanque, dropdown_placa_horizontal_vertical, distribucion_pagina


def main(page: ft.Page):
    page.title = "Calculadora de Peso de tanques"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    elementos_UI = {}
    #Estaticos
    elementos_UI["imagen_placa"] = ft.Image(src="./assets/placa horizontal.png", width=300, height=300)
    elementos_UI["imagen_tanque"] = ft.Image(src="./assets/tanque.png", width=300, height=300)
    elementos_UI["pagina"] = page
    #Dinámicos
    elementos_UI["dropdown_Tipo_de_tanque"] = dropdown_tanque()
    elementos_UI["dropdown_Placa horizontal o vertical"] = dropdown_placa_horizontal_vertical(elementos_UI)





    distribucion_pagina(page, elementos_UI)






if __name__ == "__main__":
    ft.run(main)