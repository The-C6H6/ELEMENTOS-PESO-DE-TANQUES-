import flet as ft

from calculos.fluido import calculo_peso_fluido
from calculos.general import presion_diseno
from calculos.tanque_atm import (
    calculo_cuerpo_cilindrico_p_atm,
    calculo_fondo,
    calculo_tapa_p_atm,
)
from calculos.tanque_presion import (
    calculo_cuerpo_cilindrico_presion,
    calculo_tapa_presion,
)


def _a_float(valor, nombre):
    if valor is None or valor == "":
        raise ValueError(f"Ingresa un valor para {nombre}.")
    try:
        return float(str(valor).replace(",", "."))
    except ValueError as exc:
        raise ValueError(f"El valor de {nombre} debe ser numérico.") from exc


def _fmt(valor, unidad="", decimales=3):
    if valor is None:
        return "—"
    texto = f"{valor:,.{decimales}f}".rstrip("0").rstrip(".")
    return f"{texto} {unidad}".strip()


def _fmt_lista(valores, unidad="", decimales=3):
    return ", ".join(_fmt(valor, unidad, decimales) for valor in valores)


def agregar_pasos(elementos_UI, pasos: list[dict]):
    """
    pasos = [
        {"formula": "V = π × r² × h", "valor": "= 3.1416 × (0.5)² × 2.0", "resultado": "= 1.571 m³"},
        {"formula": "m_cuerpo = ρ × V_acero", "valor": "= 7850 × 0.032", "resultado": "= 251.2 kg"},
    ]
    """
    col = elementos_UI["columna_pasos"]
    col.controls.clear()

    for i, paso in enumerate(pasos, 1):
        col.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        str(i),
                                        size=11,
                                        color="white",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    bgcolor="#7C3AED",
                                    border_radius=50,
                                    width=22,
                                    height=22,
                                    alignment=ft.Alignment.CENTER,
                                ),
                                ft.Text(
                                    paso["formula"],
                                    size=13,
                                    color="#1E1B4B",
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ],
                            spacing=8,
                        ),
                        ft.Text(paso["valor"], size=12, color="#4B5563"),
                        ft.Text(
                            paso["resultado"],
                            size=13,
                            color="#2563EB",
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    spacing=2,
                ),
                bgcolor="white",
                border_radius=8,
                padding=12,
                shadow=ft.BoxShadow(
                    blur_radius=4, color="#7C3AED11", offset=ft.Offset(0, 2)
                ),
            )
        )

    elementos_UI["pagina"].update()


def _agregar_error(elementos_UI, mensaje):
    agregar_pasos(
        elementos_UI,
        [
            {
                "formula": "No se pudo completar el cálculo",
                "valor": mensaje,
                "resultado": "Revisa los datos de entrada.",
            }
        ],
    )


def _actualizar_resultados(
    elementos_UI,
    *,
    peso_total,
    peso_fluido,
    peso_cuerpo,
    peso_cabezal,
    peso_fondo,
    volumen,
):
    elementos_UI["resultado_peso_total"].value = _fmt(peso_total, "kg")
    elementos_UI["resultado_peso_fluido"].value = _fmt(peso_fluido, "kg")
    elementos_UI["resultado_peso_cuerpo"].value = _fmt(peso_cuerpo, "kg")
    elementos_UI["resultado_peso_cabezal"].value = _fmt(peso_cabezal, "kg")
    elementos_UI["resultado_peso_fondo"].value = _fmt(peso_fondo, "kg")
    elementos_UI["resultado_volumen"].value = _fmt(volumen, "ft³")


def _pasos_presion(
    variables, cuerpo, cabezal, fondo, peso_fluido, peso_total, p_diseno
):
    diametro = _a_float(variables["diametro"], "diámetro")
    altura = _a_float(variables["altura"], "altura")
    presion_operacion = _a_float(variables["Pop"], "presión de operación")
    esfuerzo = _a_float(variables["S"], "fatiga del material")
    densidad = _a_float(variables["densidad_fluido"], "densidad del fluido")
    eficiencia = variables["E"]
    corrosion = variables["C"]

    return [
        {
            "formula": "Presión de diseño: P = 1.1·Pop si Pop > 300; si no, P = Pop + 30",
            "valor": f"Pop = {_fmt(presion_operacion, 'psi')}",
            "resultado": f"P = {_fmt(p_diseno, 'psi')}",
        },
        {
            "formula": "Área del cuerpo: A = π·D·H",
            "valor": f"A = 3.1416 × {_fmt(diametro, 'ft')} × {_fmt(altura, 'ft')}",
            "resultado": f"A = {_fmt(cuerpo['area_cilindro'], 'ft²')}",
        },
        {
            "formula": "Placas del cuerpo: N = A / 40",
            "valor": f"N = {_fmt(cuerpo['area_cilindro'], 'ft²')} / 40",
            "resultado": f"N = {_fmt(cuerpo['num_placas'], 'placas')}",
        },
        {
            "formula": "Espesor del cuerpo: t = (P·D/12) / (2·S·E - P) + C",
            "valor": f"t = ({_fmt(p_diseno, 'psi')} × {_fmt(diametro, 'ft')} / 12) / (2 × {_fmt(esfuerzo, 'psi')} × {eficiencia} - {_fmt(p_diseno, 'psi')}) + {_fmt(corrosion, 'in')}",
            "resultado": f"t mínimo = {_fmt(cuerpo['espesor'], 'in')} → t comercial = {_fmt(cuerpo.get('espesor_comercial'), 'in')}",
        },
        {
            "formula": "Peso del cuerpo: Wc = N·(t comercial·16)·48",
            "valor": f"Wc = {_fmt(cuerpo['num_placas'])} × ({_fmt(cuerpo.get('espesor_comercial'), 'in')} × 16) × 48",
            "resultado": f"Wc = {_fmt(cuerpo['peso'], 'kg')}",
        },
        {
            "formula": "Volumen total: V = (π·D²/4)·H; volumen de fluido = 0.8·V",
            "valor": f"V = (3.1416 × {_fmt(diametro, 'ft')}² / 4) × {_fmt(altura, 'ft')}",
            "resultado": f"V = {_fmt(cuerpo['volumen_total'], 'ft³')} ; Vfluido = {_fmt(cuerpo['volumen_fluido'], 'ft³')}",
        },
        {
            "formula": "Peso del fluido: Wf = Vfluido·(ρ·0.0283168)",
            "valor": f"Wf = {_fmt(cuerpo['volumen_fluido'], 'ft³')} × ({_fmt(densidad, 'kg/m³')} × 0.0283168)",
            "resultado": f"Wf = {_fmt(peso_fluido, 'kg')}",
        },
        {
            "formula": f"Espesor del cabezal ({variables['cabezal']}) según {variables['norma']}",
            "valor": f"Se evalúa la fórmula del tipo de cabezal con P={_fmt(p_diseno, 'psi')}, D={_fmt(diametro, 'ft')}, S={_fmt(esfuerzo, 'psi')}, E={eficiencia}, C={_fmt(corrosion, 'in')}",
            "resultado": f"t = {_fmt(cabezal['espesor calculado'], 'in')} → t comercial = {_fmt(cabezal['espesor comercial'], 'in')}; peso = {_fmt(cabezal['peso'], 'kg')}",
        },
        {
            "formula": f"Espesor del fondo ({variables['fondo']}) según {variables['norma']}",
            "valor": f"Se evalúa la fórmula del tipo de fondo con P={_fmt(p_diseno, 'psi')}, D={_fmt(diametro, 'ft')}, S={_fmt(esfuerzo, 'psi')}, E={eficiencia}, C={_fmt(corrosion, 'in')}",
            "resultado": f"t = {_fmt(fondo['espesor calculado'], 'in')} → t comercial = {_fmt(fondo['espesor comercial'], 'in')}; peso = {_fmt(fondo['peso'], 'kg')}",
        },
        {
            "formula": "Peso total del tanque: W = Wcuerpo + Wcabezal + Wfondo + Wfluido",
            "valor": f"W = {_fmt(cuerpo['peso'], 'kg')} + {_fmt(cabezal['peso'], 'kg')} + {_fmt(fondo['peso'], 'kg')} + {_fmt(peso_fluido, 'kg')}",
            "resultado": f"Wtotal = {_fmt(peso_total, 'kg')}",
        },
    ]


def _pasos_atmosferico(variables, cuerpo, cabezal, fondo, peso_fluido, peso_total):
    diametro = _a_float(variables["diametro"], "diámetro")
    altura = _a_float(variables["altura"], "altura")
    esfuerzo = _a_float(variables["S"], "fatiga del material")
    densidad = _a_float(variables["densidad_fluido"], "densidad del fluido")
    eficiencia = variables["E"]
    corrosion = variables["C"]
    paso_altura = 4 if variables["distribucion"] == "H" else 10

    return [
        {
            "formula": "Perímetro y área del cuerpo: Pm = π·D; A = Pm·H",
            "valor": f"Pm = 3.1416 × {_fmt(diametro, 'ft')} ; A = {_fmt(cuerpo['perimetro'], 'ft')} × {_fmt(altura, 'ft')}",
            "resultado": f"Pm = {_fmt(cuerpo['perimetro'], 'ft')} ; A = {_fmt(cuerpo['area cuerpo'], 'ft²')}",
        },
        {
            "formula": "Niveles/anillos: n = H / paso de placa",
            "valor": f"n = {_fmt(altura, 'ft')} / {paso_altura} ft",
            "resultado": f"n calculado = {_fmt(cuerpo['niveles'])}; n real = {cuerpo['niveles reales']}",
        },
        {
            "formula": "Placas: Ntotal = A / 40; Nanillo = perímetro / ancho de placa",
            "valor": f"Ntotal = {_fmt(cuerpo['area cuerpo'], 'ft²')} / 40",
            "resultado": f"Ntotal = {_fmt(cuerpo['placas totales'])}; Nanillo = {_fmt(cuerpo['placas anillo'])}",
        },
        {
            "formula": "Espesores por nivel: t = (2.604·H·D·ρ/1000)/(E·S) + C",
            "valor": f"Con D={_fmt(diametro, 'ft')}, ρ={_fmt(densidad, 'kg/m³')}, E={eficiencia}, S={_fmt(esfuerzo, 'psi')}, C={_fmt(corrosion, 'in')}",
            "resultado": f"t mínimos = [{_fmt_lista(cuerpo['espesores minimos'], 'in')}]; t comerciales = [{_fmt_lista(cuerpo['espesores comerciales'], 'in')}]",
        },
        {
            "formula": "Peso por anillo: Wanillo = 48·(t comercial·16)·Nanillo·fracción de nivel",
            "valor": "Se calcula para cada nivel y se suman los anillos.",
            "resultado": f"Pesos por anillo = [{_fmt_lista(cuerpo['pesos de cada anillo'], 'kg')}]; Wcuerpo = {_fmt(cuerpo['peso cc'], 'kg')}",
        },
        {
            "formula": "Volumen total: V = (π·D²/4)·H; volumen de fluido = 0.8·V",
            "valor": f"V = (3.1416 × {_fmt(diametro, 'ft')}² / 4) × {_fmt(altura, 'ft')}",
            "resultado": f"V = {_fmt(cuerpo['volumen total'], 'ft³')} ; Vfluido = {_fmt(cuerpo['volumen_fluido'], 'ft³')}",
        },
        {
            "formula": "Peso del fluido: Wf = Vfluido·(ρ·0.0283168)",
            "valor": f"Wf = {_fmt(cuerpo['volumen_fluido'], 'ft³')} × ({_fmt(densidad, 'kg/m³')} × 0.0283168)",
            "resultado": f"Wf = {_fmt(peso_fluido, 'kg')}",
        },
        {
            "formula": "Tapa atmosférica: plana si ángulo = 0; cónica si hay ángulo",
            "valor": f"Área = {_fmt(cabezal['area'], 'ft²')}; placas = área / 40; espesor = 1/16 + C",
            "resultado": f"Tipo = {cabezal['tipo tapa']}; t = {_fmt(cabezal['espesor'], 'in')}; peso = {_fmt(cabezal['peso'], 'kg')}",
        },
        {
            "formula": "Fondo atmosférico: área = longitud²; espesor = 1/4 + C",
            "valor": f"Área = {_fmt(fondo['area'], 'ft²')}; placas = área / 40",
            "resultado": f"t = {_fmt(fondo['espesor'], 'in')}; peso = {_fmt(fondo['peso'], 'kg')}",
        },
        {
            "formula": "Peso total del tanque: W = Wcuerpo + Wtapa + Wfondo + Wfluido",
            "valor": f"W = {_fmt(cuerpo['peso cc'], 'kg')} + {_fmt(cabezal['peso'], 'kg')} + {_fmt(fondo['peso'], 'kg')} + {_fmt(peso_fluido, 'kg')}",
            "resultado": f"Wtotal = {_fmt(peso_total, 'kg')}",
        },
    ]


def boton_calcular(elementos_UI, variables):
    def boton_presionado(e):
        try:
            diametro = _a_float(variables["diametro"], "diámetro")
            altura = _a_float(variables["altura"], "altura")
            esfuerzo = _a_float(variables["S"], "fatiga del material")
            densidad = _a_float(variables["densidad_fluido"], "densidad del fluido")
            eficiencia = float(variables["E"])
            corrosion = float(variables["C"])

            if variables["Tanque"] == "Patm":
                cuerpo = calculo_cuerpo_cilindrico_p_atm(
                    variables["distribucion"],
                    diametro,
                    altura,
                    eficiencia,
                    esfuerzo,
                    corrosion,
                    densidad,
                )
                cabezal = calculo_tapa_p_atm(
                    diametro,
                    corrosion,
                    _a_float(variables.get("angulo cabezal", 0), "ángulo del cabezal"),
                )
                fondo = calculo_fondo(diametro, corrosion)
                peso_cuerpo = cuerpo["peso cc"]
                volumen_fluido = cuerpo["volumen_fluido"]
                volumen_total = cuerpo["volumen total"]
                peso_fluido = calculo_peso_fluido(volumen_fluido, densidad)
                peso_total = peso_cuerpo + cabezal["peso"] + fondo["peso"] + peso_fluido
                pasos = _pasos_atmosferico(
                    variables, cuerpo, cabezal, fondo, peso_fluido, peso_total
                )
            else:
                presion_operacion = _a_float(variables["Pop"], "presión de operación")
                p_diseno = presion_diseno(presion_operacion)
                cuerpo = calculo_cuerpo_cilindrico_presion(
                    diametro, altura, p_diseno, esfuerzo, eficiencia, corrosion
                )
                cabezal = calculo_tapa_presion(
                    variables["cabezal"],
                    variables["norma"],
                    p_diseno,
                    diametro,
                    esfuerzo,
                    eficiencia,
                    corrosion,
                    _a_float(variables.get("angulo cabezal", 0), "ángulo del cabezal"),
                )
                fondo = calculo_tapa_presion(
                    variables["fondo"],
                    variables["norma"],
                    p_diseno,
                    diametro,
                    esfuerzo,
                    eficiencia,
                    corrosion,
                    _a_float(variables.get("angulo fondo", 0), "ángulo del fondo"),
                )
                peso_cuerpo = cuerpo["peso"]
                volumen_fluido = cuerpo["volumen_fluido"]
                volumen_total = cuerpo["volumen_total"]
                peso_fluido = calculo_peso_fluido(volumen_fluido, densidad)
                peso_total = peso_cuerpo + cabezal["peso"] + fondo["peso"] + peso_fluido
                pasos = _pasos_presion(
                    variables, cuerpo, cabezal, fondo, peso_fluido, peso_total, p_diseno
                )

            _actualizar_resultados(
                elementos_UI,
                peso_total=peso_total,
                peso_fluido=peso_fluido,
                peso_cuerpo=peso_cuerpo,
                peso_cabezal=cabezal["peso"],
                peso_fondo=fondo["peso"],
                volumen=volumen_total,
            )
            agregar_pasos(elementos_UI, pasos)
        except ValueError as exc:
            _agregar_error(elementos_UI, str(exc))
        except ZeroDivisionError:
            _agregar_error(
                elementos_UI,
                "No se puede dividir entre cero; revisa presión, fatiga y eficiencia de soldadura.",
            )

    return ft.Button(
        content="Calcular",
        width=300,
        height=40,
        bgcolor="#007bff",
        color="white",
        on_click=boton_presionado,
    )
