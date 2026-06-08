import flet as ft
from calculos import factor_corrosion

def dropdown_tanque():
    return ft.Dropdown(
    width=300,
    value="P",
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
        value="H",
        options=[
            ft.DropdownOption(key="H", text="Placa Horizontal"),
            ft.DropdownOption(key="V", text="Placa Vertical"),
        ],
        on_select=on_seleccion,  
    )

def dropdown_cabezal():
    return ft.Dropdown(
        width=300,

        value='plano',
        options=[
            ft.DropdownOption(key="plano", text="Plano"),
            ft.DropdownOption(key="eliptico", text="Elíptico"),
            ft.DropdownOption(key="torisferico", text="Torisférico"),
            ft.DropdownOption(key="hemisferico", text="Hemisférico"),
            ft.DropdownOption(key="conico", text="Cónico"),
        ],
    )






#Terminado
def dropdown_eficiencia_soldadura(variables):

    def on_seleccion(e):
        variables['E']=float(e.control.value)
        print(variables['E'])
        

    return ft.Dropdown(
        width=300,
        value="0.85",
        options=[
            
            ft.DropdownOption(key="1.00", text="Radiografiado 100%"),
            ft.DropdownOption(key="0.85", text="Radiografiado parcial"),
            ft.DropdownOption(key="0.70", text="No examinado"),

        ],

        on_select=on_seleccion
    )

#Terminado
def dropdown_material(variables):
    def on_seleccion(e):
        corrosion=factor_corrosion(e.control.value)
        variables['C']=corrosion
        print(variables['C'])

    return ft.Dropdown(
        width=300,
        value="carbono",
        options=[
            
            ft.DropdownOption(key="carbono", text="Acero al C."),
            ft.DropdownOption(key="inox", text="Acero Inox."),


        ],
        on_select=on_seleccion
    )