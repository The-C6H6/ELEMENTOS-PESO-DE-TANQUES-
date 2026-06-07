import flet as ft
from UI import dropdown_tanque, dropdown_placa_horizontal_vertical, distribucion_pagina, dropdown_cabezal
from UI import tf_diametro_tanque, tf_altura_tanque, tf_presion_operacion
from UI import boton_calcular

def main(page: ft.Page):
    page.title = "Calculadora de Peso de tanques"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1450
    page.window.height = 720
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    elementos_UI = {}
    #Estaticos
    elementos_UI["imagen_placa"] = ft.Image(src="./assets/placa horizontal.png", width=300, height=300)
    elementos_UI["imagen_tanque"] = ft.Image(src="./assets/tanque.png", width=275, height=300)
    elementos_UI["pagina"] = page
    #Dinámicos
    elementos_UI["dropdown_Tipo_de_tanque"] = dropdown_tanque()
    elementos_UI["dropdown_Placa horizontal o vertical"] = dropdown_placa_horizontal_vertical(elementos_UI)
    elementos_UI["dropdown_tipo_cabezal"]=dropdown_cabezal()
    elementos_UI["diametro_tanque"]=tf_diametro_tanque()
    elementos_UI["altura_tanque"]=tf_altura_tanque()
    elementos_UI["Presion_operacion"]=tf_presion_operacion()

    elementos_UI["boton_calcular"]=boton_calcular()

    distribucion_pagina(page, elementos_UI)






if __name__ == "__main__":
    ft.run(main)