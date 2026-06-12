from .general import (
    area_cilindrica,
    volumen_cc,
    espesor_tapa_presion,
    espesor_placa_comercial,
    area_tapa_p,
    base_tapa_plana_criterio,
)
import math


def calculo_cuerpo_cilindrico_presion(
    diametro: float, altura: float, P: float, S: float, E: float, C: float
):
    area_cilindro = area_cilindrica(diametro, altura)
    num_placas_cilindro = area_cilindro / 40
    t = (P * diametro / 12) / (2 * S * E - P) + C
    t_comer = espesor_placa_comercial(t)
    peso = num_placas_cilindro * (t_comer * 16) * 48
    volumen = volumen_cc(diametro, altura)

    return {
        "Título": "valores",
        "espesor": t,
        "espesor_comercial": t_comer,
        "peso": peso,
        "num_placas": num_placas_cilindro,
        "area_cilindro": area_cilindro,
        "volumen_total": volumen,
        "volumen_fluido": 0.8 * volumen,
    }


def calculo_tapa_presion(tipo_tapa, norma, P, D, S, E, C, alpha_grados):
    t_min = espesor_tapa_presion(tipo_tapa, norma, P, D, S, E, C, alpha_grados)
    t_comercial = espesor_placa_comercial(t_min)
    area = area_tapa_p(tipo_tapa, D)
    longitud = base_tapa_plana_criterio(D) if tipo_tapa == "plano" else D
    num_placas = area_tapa_p(tipo_tapa, D)
    peso = t_comercial * 48 * num_placas

    return {
        "Título": "valores",
        "Diametro": longitud,
        "tipo tapa": tipo_tapa,
        "area": area,
        "placas totales": num_placas,
        "placas redondeadas": math.ceil(num_placas),
        "espesor calculado": t_min,
        "espesor comercial": t_comercial,
        "peso": peso,
    }
