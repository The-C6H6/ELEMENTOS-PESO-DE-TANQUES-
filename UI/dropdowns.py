import flet as ft
from calculos import factor_corrosion


#Terminado
def dropdown_tanque(componentes, variables_dinamicas):

    def on_seleccion(e):
        componentes['Presion_operacion'].visible=False if e.control.value=="Patm" else True
        variables_dinamicas['Tanque']=e.control.value
        if e.control.value=="Patm" : 
            componentes['dropdown_cabezal'].options=[ft.DropdownOption(key="plano", text="Plano")]
            componentes['dropdown_cabezal'].value='plano'
            componentes['dropdown_tipo_fondo'].options=[ft.DropdownOption(key="plano", text="Plano")]
            componentes['dropdown_tipo_fondo'].value= 'plano'

            componentes['dropdown_norma'].options=[ft.DropdownOption(key="API_650", text="API 650")]
            componentes['dropdown_norma'].value='API_650'
            variables_dinamicas['norma']='API_650'


        else:
            componentes['dropdown_cabezal'].options=[
                ft.DropdownOption(key="plano", text="Plano"),
                ft.DropdownOption(key="eliptico", text="Elíptico"),
                ft.DropdownOption(key="torisferico", text="Torisférico"),
                ft.DropdownOption(key="hemisferico", text="Hemisférico"),
                ft.DropdownOption(key="conico", text="Cónico"),
            ]
            componentes['dropdown_tipo_fondo'].options=[
                ft.DropdownOption(key="plano", text="Plano"),
                ft.DropdownOption(key="eliptico", text="Elíptico"),
                ft.DropdownOption(key="torisferico", text="Torisférico"),
                ft.DropdownOption(key="hemisferico", text="Hemisférico"),
                ft.DropdownOption(key="conico", text="Cónico"),
            ]

            componentes['dropdown_norma'].options=[
            ft.DropdownOption(key="ASME", text="ASME"),
            ft.DropdownOption(key="API-ASME", text="API-ASME"),
            ]
            componentes['dropdown_norma'].value='ASME'
            variables_dinamicas['norma']='ASME'


    return ft.Dropdown(
    width=300,
    value="P",
    options=[
        ft.DropdownOption(key="P", text="Tanque Sujeto a Presión"),
        ft.DropdownOption(key="Patm", text="Tanque Atmosférico"),
    ],
    on_select=on_seleccion
)
    
#Terminado
def dropdown_placa_horizontal_vertical(elementos_UI, variables):
    def on_seleccion(e):
        variables['distribucion'] = e.control.value
        if variables['distribucion']  == "H":
            elementos_UI["imagen_placa"].src = "./assets/placa horizontal.png"
        else:
            elementos_UI["imagen_placa"].src = "./assets/placa vertical.png"


    return ft.Dropdown(
        width=300,
        value="H",
        options=[
            ft.DropdownOption(key="H", text="Placa Horizontal"),
            ft.DropdownOption(key="V", text="Placa Vertical"),
        ],
        on_select=on_seleccion,  
    )

#Terminado
def dropdown_cabezal(variables):

    def on_seleccion(e):
        variables['cabezal']=e.control.value

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
        on_select=on_seleccion
    )

#Terminado
def dropdown_fondo(variables):

    def on_seleccion(e):
        variables['fondo']=e.control.value

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
        on_select=on_seleccion
    )

#Terminado
def dropdown_eficiencia_soldadura(variables):

    def on_seleccion(e):
        variables['E']=float(e.control.value)
        

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

    return ft.Dropdown(
        width=300,
        value="carbono",
        options=[
            
            ft.DropdownOption(key="carbono", text="Acero al C."),
            ft.DropdownOption(key="inox", text="Acero Inox."),


        ],
        on_select=on_seleccion
    )

#Terminado
def dropdown_norma(variables):
    def on_seleccion(e):
        variables['norma']=e.control.value
 

      
    return ft.Dropdown(
        width=300,
        value="ASME",
        options=[
            
            ft.DropdownOption(key="ASME", text="ASME"),
            ft.DropdownOption(key="API-ASME", text="API-ASME"),

        ],
        on_select=on_seleccion
    )