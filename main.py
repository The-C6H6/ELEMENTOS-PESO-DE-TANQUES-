import flet as ft
from UI import dropdown_material ,dropdown_tanque, dropdown_placa_horizontal_vertical, distribucion_pagina, dropdown_cabezal, dropdown_eficiencia_soldadura, dropdown_norma, dropdown_fondo
from UI import tf_diametro_tanque, tf_altura_tanque, tf_presion_operacion, tf_fatiga_material, tf_densidad_fluido, tf_angulo_tapa,tf_angulo_cabezal
from UI import boton_calcular

def main(page: ft.Page):
    page.title = "Calculadora de Peso de tanques"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1450
    page.window.height = 720
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    elementos_UI = {}
    
    variables_dinamicas={
        "E":0.85,
        "C":1/8,
        "diametro":None,
        "altura":None,
        "Pop":None,
        "S":None,
        "densidad_fluido":None,
        "Tanque":"P",
        "norma":"ASME",
        "distribucion":'H', 
        'cabezal':'plano',
        'fondo':'plano',
        'angulo cabezal':0,
        'angulo fondo':0
    

    }

    pasos = [
        {"formula": "V = π × r² × h", "valor": "= 3.1416 × (0.5)² × 2.0", "resultado": "= 1.571 m³"},
        {"formula": "m_cuerpo = ρ × V_acero", "valor": "= 7850 × 0.032", "resultado": "= 251.2 kg"},
    ]

    #Estaticos
    elementos_UI["imagen_placa"] = ft.Image(src="./assets/placa horizontal.png", width=300, height=300)
    elementos_UI["imagen_tanque"] = ft.Image(src="./assets/tanque.png", width=275, height=360)
    elementos_UI["pagina"] = page
    #Dinámicos
    
    elementos_UI["dropdown_Placa horizontal o vertical"] = dropdown_placa_horizontal_vertical(elementos_UI, variables_dinamicas)
    elementos_UI["diametro_tanque"]=tf_diametro_tanque(variables_dinamicas)
    elementos_UI["altura_tanque"]=tf_altura_tanque(variables_dinamicas)
    elementos_UI["Presion_operacion"]=tf_presion_operacion(variables_dinamicas)
    elementos_UI["fatiga_material"]=tf_fatiga_material(variables_dinamicas)
    
    elementos_UI["dropdown_tipo_fondo"]=dropdown_fondo(variables_dinamicas, elementos_UI)
    
    elementos_UI["dropdown_eficiencia_soldadura"]=dropdown_eficiencia_soldadura(variables_dinamicas)
    elementos_UI['densidad_fluido']=tf_densidad_fluido(variables_dinamicas)
    elementos_UI['Material']=dropdown_material(variables_dinamicas)
    elementos_UI['dropdown_norma']=dropdown_norma(variables_dinamicas)
    elementos_UI['angulo_cabezal']=tf_angulo_cabezal(variables_dinamicas)
    elementos_UI['angulo_fondo']=tf_angulo_tapa(variables_dinamicas)
    elementos_UI["dropdown_cabezal"]=dropdown_cabezal(variables_dinamicas, elementos_UI)
    elementos_UI["dropdown_Tipo_de_tanque"] = dropdown_tanque(elementos_UI, variables_dinamicas)
    elementos_UI["boton_calcular"]=boton_calcular(elementos_UI, pasos)
    distribucion_pagina(page, elementos_UI)

    

    





if __name__ == "__main__":
    ft.run(main)