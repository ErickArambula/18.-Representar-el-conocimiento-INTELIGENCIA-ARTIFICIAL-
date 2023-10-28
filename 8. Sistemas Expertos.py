# Base de conocimiento
base_conocimiento = {
    "soleado": "lleva gafas de sol",
    "lluvioso": "lleva un paraguas",
    "nublado": "no necesitas nada especial",
    "ventoso": "sujeta bien tus pertenencias"
}

# Función de consulta al sistema experto
def sistema_experto(condicion):
    if condicion in base_conocimiento:
        return base_conocimiento[condicion]
    else:
        return "No tengo recomendaciones para esa condición."

# Interacción con el usuario
while True:
    condicion_actual = input("¿Cuál es la condición del tiempo? (soleado, lluvioso, nublado, ventoso): ")
    recomendacion = sistema_experto(condicion_actual)
    print(recomendacion)
    continuar = input("¿Deseas hacer otra consulta? (s/n): ")
    if continuar.lower() != "s":
        break
