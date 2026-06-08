def espesor_placa_comercial(espesor_calculado):
    for i in range(1,16):
        if espesor_calculado< i/16:
            return [i/16, i]
    else:
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

