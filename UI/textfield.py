import flet as ft
#Terminado
def tf_diametro_tanque(variables):
    def on_change_func(e):
        variables['diametro']=e.control.value

    return ft.TextField(label="Diámetro del tanque (ft)", width=300,
                        on_change=on_change_func)    

#Terminado
def tf_altura_tanque(variables):
    def on_change_func(e):
        variables['altura']=e.control.value

    return ft.TextField(label="Altura del tanque (ft)", width=300,
                        on_change=on_change_func) 

#Terminado
def tf_presion_operacion(variables):
    def on_change_func(e):
        variables['Pop']=e.control.value
    return ft.TextField(label="Presión de operación (psi)", width=300,
                        on_change=on_change_func) 

#Terminado
def tf_fatiga_material(variables):
    def on_change_func(e):
        variables['S']=e.control.value
        
    return ft.TextField(label="Fatiga del material (psi)", width=300,
                        on_change=on_change_func)

#Terminado
def tf_densidad_fluido(variables):
    def on_change_func(e):
        variables['densidad_fluido']=e.control.value
    return ft.TextField(label="Densidad del fluido en kg/m³", width=300,
                        on_change=on_change_func)