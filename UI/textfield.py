import flet as ft

def tf_diametro_tanque():
    return ft.TextField(label="Diámetro del tanque (ft)", width=300)    

def tf_altura_tanque():
    return ft.TextField(label="Altura del tanque (ft)", width=300)    

def tf_presion_operacion():
    return ft.TextField(label="Presión de operación (psi)", width=300)