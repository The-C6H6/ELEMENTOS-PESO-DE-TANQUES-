from .general import area_cc, volumen_cc

def calculo_cuerpo_cilindrico(diametro:float, altura:float, P:float, S:float, E:float, C:float):
    area_cilindro=area_cc(diametro, altura)
    num_placas_cilindro=area_cilindro/40 
    t = (P * diametro/12) / (2*S*E - P) + C
    peso=num_placas_cilindro*t*48
    volumen=volumen_cc(diametro, altura)

    return {
           "espesor": t, 
           "peso": peso, 
           "num_placas": num_placas_cilindro, 
           "area_cilindro": area_cilindro,
           "volumen_total": volumen,
           "volumen_fluido": 0.8 * volumen
           }





def calculo_tapa(tipo_tapa):
    pass



def calculo_fondo(tipo_fondo):
    pass    









def calculo_peso_fluido(volumen_fluido, densidad_fluido):
    densidad_fluido=densidad_fluido*0.0283168   #Conversion de kg/m3 a kg/ft3
    peso_fluido=volumen_fluido*densidad_fluido
    return peso_fluido