import math



def espesor_placa_comercial(espesor_calculado: float):
    for i in range(1, 17):
        if espesor_calculado <= i / 16:
            return i / 16

    return espesor_calculado



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
        

def placas_nivel(diametro,distribucion):
    perimetro=perimetro_cilindrico(diametro)
    if distribucion =='H':
        return perimetro/10
    else:
        return perimetro/4



def placas_totales(diametro,altura):
    return area_cilindrica(diametro, altura)/40


def area_cilindrica(diametro, altura):
    return perimetro_cilindrico(diametro)*altura
    

def perimetro_cilindrico(diametro):
    PI=3.1416
    return PI*diametro



def espesor_pared_atm(H, D,E, S, C, densidad ):
    return (2.604 * H * D * densidad/1000) / (E * S) + C



def espesores_pared_atm(H, diametro, E, S, C, densidad, distribucion):
    t=[]
    t_comercial=[]
  
    while H > 0:
        T=espesor_pared_atm(H=H, D=diametro,E=E, S=S, C=C, densidad=densidad)
        T_comercial=espesor_placa_comercial(T)
        t.append(T)
        t_comercial.append(T_comercial)
        H-=4 if distribucion =='H'else 10
    return t , t_comercial




def pesos_anillos(espesor_comercial:list, nivel_calculado:float, placas_por_anillo:float):
    w=[]
    nivel_actual=nivel_calculado
    for espesor in espesor_comercial:
        if nivel_actual <= 0:
            break
        if nivel_actual<1:
            w_anillo=48*(espesor*16)*placas_por_anillo*nivel_actual
            w.append(w_anillo) 
            return w

        w_anillo=48*(espesor*16)*placas_por_anillo
        w.append(w_anillo)
        nivel_actual-=1
    return w 


    



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





