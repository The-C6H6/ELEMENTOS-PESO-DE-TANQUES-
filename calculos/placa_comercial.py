def espesor_placa_comercial(espesor_calculado):
    for i in range(1,16):
        if espesor_calculado< i/16:
            return [i/16, i]
    
    else:
        return espesor_calculado
    

    