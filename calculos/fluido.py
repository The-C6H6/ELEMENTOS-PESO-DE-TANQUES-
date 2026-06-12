

def calculo_peso_fluido(volumen_fluido, densidad_fluido):
    densidad_fluido=densidad_fluido*0.0283168   #Conversion de kg/m3 a kg/ft3
    peso_fluido=volumen_fluido*densidad_fluido
    return peso_fluido