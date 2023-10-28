# Crear una regla
def regla_si_entonces(condicion, conclusion):
    if condicion:
        return conclusion

# Definir una regla
regla_1 = regla_si_entonces("llueve", "usar paraguas")

# Evaluar la regla
condicion_actual = "llueve"
resultado = regla_1(condicion_actual)
print(f"Si {condicion_actual}, entonces {resultado}")

# Crear una red semántica
red_semantica = {
    "Persona": {
        "es_un": "Ser Humano",
        "tiene_edad": 30
    },
    "Perro": {
        "es_un": "Animal",
        "tiene_edad": 5
    }
}

# Acceder a información en la red semántica
print("Una Persona es un", red_semantica["Persona"]["es_un"])
print("Edad de un Perro:", red_semantica["Perro"]["tiene_edad"])
