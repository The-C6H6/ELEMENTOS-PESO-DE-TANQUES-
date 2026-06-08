from .general import area_cc, volumen_cc, espesor_tapa_no_plana, espesor_placa_comercial

def calculo_cuerpo_cilindrico(diametro:float, altura:float, P:float, S:float, E:float, C:float):
    area_cilindro=area_cc(diametro, altura)
    num_placas_cilindro=area_cilindro/40 
    t = (P * diametro/12) / (2*S*E - P) + C
    t_comer=espesor_placa_comercial(t)
    peso=num_placas_cilindro * (t_comer*16) *48
    volumen=volumen_cc(diametro, altura)


    return {
           "espesor": t, 
           "peso": peso, 
           "num_placas": num_placas_cilindro, 
           "area_cilindro": area_cilindro,
           "volumen_total": volumen,
           "volumen_fluido": 0.8 * volumen
           }





def calculo_tapa(tipo_tapa, norma, P, D, S,E, C):
    pass



def calculo_fondo(tipo_fondo, norma):
    pass    





def calculo_peso_fluido(volumen_fluido, densidad_fluido):
    densidad_fluido=densidad_fluido*0.0283168   #Conversion de kg/m3 a kg/ft3
    peso_fluido=volumen_fluido*densidad_fluido
    return peso_fluido