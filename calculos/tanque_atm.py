from .general import base_tapa_plana_criterio, niveles_tanque
import math 

def calculo_cuerpo_cilindrico(distribucion, diametro, altura):
    niveles=  niveles_tanque(distribucion, altura)  








#Terminado
def calculo_tapa(diametro, c, angulo=0):
    if angulo==0 or angulo is None or angulo=='':
        longitud = base_tapa_plana_criterio(diametro)
        area=longitud**2
    else:
        angulo_radianes = math.radians(angulo)
        area=(diametro**2)/(3000*math.sin(angulo_radianes))

    num_placas=area/40
    espesor=1/16+c
    peso=num_placas*(espesor*16)*48

    return{
        "longitud":longitud,
        "area":area,
        "num_placas":num_placas,
        "espesor":espesor,
        "peso":peso
    }



#Terminado
def calculo_fondo(diametro, c):
    longitud= base_tapa_plana_criterio(diametro)
    area=longitud**2
    num_placas=area/40
    espesor=1/4+c
    peso=num_placas*(espesor*16)*48

    return{
        "longitud":longitud,
        "area":area,
        "num_placas":num_placas,
        "espesor":espesor,
        "peso":peso
    }
    
    
