import flet as ft
from UI import dropdown_tanque, dropdown_placa_horizontal_vertical

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
        "dropdown_Placa horizontal o vertical":dropdown_placa_horizontal_vertical()
    }

    page.add(
        ft.Text("Seleccione el tipo de tanque:"),
        elementos_UI["dropdown_Tipo_de_tanque"],
        ft.Text("Seleccione la orientación de la placa:"),
        elementos_UI["dropdown_Placa horizontal o vertical"]
    )



if __name__ == "__main__":
    ft.run(main)