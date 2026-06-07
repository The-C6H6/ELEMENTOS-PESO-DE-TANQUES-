import flet as ft

def dropdown_tanque():
    return ft.Dropdown(
    width=300,
    value="P",
    options=[
        ft.DropdownOption(key="P", text="Tanque Sujeto a Presión"),
        ft.DropdownOption(key="Patm", text="Tanque Atmosférico"),
    ],
)
    
def dropdown_placa_horizontal_vertical():
    return ft.Dropdown(
    width=300,
    value="H",
    options=[
        ft.DropdownOption(key="H", text="Placa Horizontal"),
        ft.DropdownOption(key="V", text="Placa Vertical"),
    ],
)