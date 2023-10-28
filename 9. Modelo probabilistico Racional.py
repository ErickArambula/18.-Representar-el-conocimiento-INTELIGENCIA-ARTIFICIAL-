# Importar la biblioteca para trabajar con probabilidades
from fractions import Fraction

# Definir los estados y las probabilidades de un evento
estados = ["A", "B", "C"]
probabilidades = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]

# Calcular la probabilidad condicional de un evento dada una observación
def probabilidad_condicional(evento, observacion):
    if evento in estados:
        indice = estados.index(evento)
        return probabilidades[indice]
    else:
        return Fraction(0)

# Calcular la probabilidad total utilizando el teorema de la probabilidad total
def probabilidad_total(observacion):
    prob_total = Fraction(0)
    for estado in estados:
        prob_total += probabilidad_condicional(estado, observacion)
    return prob_total

# Tomar una decisión basada en la probabilidad máxima
def tomar_decision(observacion):
    prob_maxima = Fraction(0)
    decision = None
    for estado in estados:
        prob_condicional = probabilidad_condicional(estado, observacion)
        if prob_condicional > prob_maxima:
            prob_maxima = prob_condicional
            decision = estado
    return decision

# Realizar una observación y tomar una decisión
observacion = "A"
decision = tomar_decision(observacion)

# Imprimir los resultados
print(f"Observación: {observacion}")
print(f"Decisión: {decision}")
s