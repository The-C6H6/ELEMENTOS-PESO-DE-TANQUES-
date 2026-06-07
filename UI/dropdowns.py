import flet as ft

def dropdown_tanque():
    return ft.Dropdown(
    width=300,
    value=None,
    options=[
        ft.DropdownOption(key="P", text="Tanque Sujeto a Presión"),
        ft.DropdownOption(key="Patm", text="Tanque Atmosférico"),
    ],
)
    




def dropdown_placa_horizontal_vertical(elementos_UI):

    def on_seleccion(e):
        valor = e.control.value
        if valor == "H":
            elementos_UI["imagen_placa"].src = "./assets/placa horizontal.png"
        else:
            elementos_UI["imagen_placa"].src = "./assets/placa vertical.png"

        elementos_UI["pagina"].update()

    return ft.Dropdown(
        width=300,
        label="Orientación de la placa",
        value="H",
        options=[
            ft.DropdownOption(key="H", text="Placa Horizontal"),
            ft.DropdownOption(key="V", text="Placa Vertical"),
        ],
        on_select=on_seleccion,  
    )

def dropdown_cabezal():
    pass