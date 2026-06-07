

def calculo_cuerpo_cilindrico(diametro, altura, P, S, E, C):
    pi=3.1416
    area_cilindro=pi*diametro*altura
    num_placas_cilindro=area_cilindro/40 
    t = (P * diametro) / (2*S*E - P) + C
    peso=num_placas_cilindro*t*48



def calculo_tapa():
    pass



def calculo_fondo():
    pass    