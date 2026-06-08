import math



def espesor_placa_comercial(espesor_calculado:float):
    for i in range(1,16):
        if espesor_calculado<= i/16:
            return i/16
    
    return 1



def presion_diseno(presion_operacion):
    if presion_operacion >300:
        return 1.1*presion_operacion
    else:
        return presion_operacion+30




def factor_corrosion(tipo_tuberia):
    if tipo_tuberia == "carbono":
        return 1/8
    else:
        return 1/16


def eficiencia_soldadura(tipo_radiografiado):
    if tipo_radiografiado == "total":
        return 1
    elif tipo_radiografiado == "parcial":
        return 0.85
    else:
        return 0.7
    

def area_cc(diametro, altura):
    pi=3.1416
    area_cilindro=pi*diametro*altura
    return area_cilindro


def volumen_cc(diametro, altura):
    pi=3.1416
    area_base=(pi*diametro**2)/4
    return area_base*altura


def base_tapa_plana_criterio(diametro):
    criterio=4*3.2808       #4 metros a ft
    diametro_tapa= diametro+4/12 if diametro >= criterio else diametro+2/12
    return diametro_tapa



def niveles_tanque(distribucion, altura):
    if distribucion=='H':
        return altura/4
    else:
        return altura/10
        



#Faltan consideraciones
def espesor_tapa_no_plana(tipo_tapa, norma, P, D, S,E, C, alpha_grados=None, d=None, c=None):
     # -------------------------------
    # TAPA ELÍPTICA
    # -------------------------------
    if tipo_tapa == "eliptico":
        if norma == "ASME":
            denominador = (2 * S*E) - (0.2 * P)

        elif norma == "API-ASME":
            denominador = 2 * S*E
        
        return (P * D) / denominador + C

    # -------------------------------
    # TAPA TORIESFÉRICA
    # -------------------------------
    elif tipo_tapa == "toriesferico":

        if norma == "ASME":
            denominador = S*E - (0.1 * P)
        
        elif norma == "API-ASME":
            denominador = S*E

        return (0.885 * P * D/2) / denominador + C

    # -------------------------------
    # TAPA HEMIESFÉRICA
    # -------------------------------
    elif tipo_tapa == "hemiesferico":
        if norma == "ASME":
            denominador = (4 * S*E) - (0.4 * P)

        elif norma == "API-ASME":
            denominador = 4 * S*E
        return (P * D) / denominador + C

    # -------------------------------
    # TAPA CÓNICA
    # -------------------------------
    elif tipo_tapa == "conico":
        if alpha_grados is None:
            raise ValueError("Para tapa cónica debes proporcionar alpha_grados.")

        alpha_rad = math.radians(alpha_grados)

        if norma == "ASME":
            denominador = 2 * math.cos(alpha_rad) * (S*E - (0.6 * P))
       
        elif norma == "API-ASME":
            denominador = 2 * S*E * math.cos(alpha_rad)
            
        return (P * D) / denominador + C
    
    # -------------------------------
    # TAPA PLANA
    # -------------------------------
    elif tipo_tapa == "plano":
        if d is None:
            raise ValueError("Para tapa plana debes proporcionar diametro de placa.")
        return d*math.sqrt(c*P/S*E)





