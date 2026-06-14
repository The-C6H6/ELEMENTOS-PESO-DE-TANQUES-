from .general import base_tapa_plana_criterio, niveles_tanque, placas_totales, placas_nivel, perimetro_cilindrico, area_cilindrica, volumen_cc, espesores_pared_atm, pesos_anillos
import math 

#Terminado
def calculo_cuerpo_cilindrico_p_atm(distribucion, diametro, altura, E, S, C, densidad):
    niveles =  niveles_tanque(distribucion, altura)  
    niveles_rounded=math.ceil(niveles)
    placas=placas_totales(diametro=diametro, altura=altura)
    perimetro=perimetro_cilindrico(diametro)
    area_cuerpo=area_cilindrica(diametro=diametro, altura=altura)
    volumen_total=volumen_cc(diametro=diametro, altura=altura)
    placas_anillo=placas_nivel(diametro=diametro, distribucion=distribucion)
    t, t_comercial=espesores_pared_atm(altura, diametro, E, S, C, densidad, distribucion)
    pesos_por_anillo=pesos_anillos(espesor_comercial=t_comercial, nivel_calculado=niveles, placas_por_anillo=placas_anillo)
    peso_total_cc=sum(pesos_por_anillo)
    return{
        'Título':'valores',
        'niveles':niveles,
        'niveles reales':niveles_rounded,
        'placas totales':placas,
        'placas redondeadas':math.ceil(placas),
        'perimetro':perimetro,
        'area cuerpo':area_cuerpo,
        'volumen total':volumen_total,
        "volumen_fluido": 0.8 * volumen_total,
        'placas anillo':placas_anillo,
        'placas anillo redondeadas': math.ceil(placas_anillo),
        'pesos de cada anillo':pesos_por_anillo,
        'espesores minimos':t,
        'espesores comerciales':t_comercial,
        'peso cc':peso_total_cc
    }


#Terminado
def calculo_tapa_p_atm(diametro, c, angulo:float=0):
    if angulo==0 or angulo is None or angulo=='':
        tipo_tapa='Plana'
        longitud = base_tapa_plana_criterio(diametro)
        area=longitud**2
    else:
        tipo_tapa='Cónica'
        longitud = None
        angulo_radianes = math.radians(angulo)
        area=(diametro**2)/(3000*math.sin(angulo_radianes))

    num_placas=area/40
    espesor=1/16+c
    peso=num_placas*(espesor*16)*48

    return{
        'Título':'valores',
        "longitud":longitud,
        "tipo tapa": tipo_tapa,
        "area":area,
        "placas totales":num_placas,
        "placas redondeadas": math.ceil(num_placas),
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
        'Título':'valores',
        "longitud":longitud,
        "area":area,
        "placas totales":num_placas,
        "placas redondeadas": math.ceil(num_placas),
        "espesor":espesor,
        "peso":peso
    }
    
    
