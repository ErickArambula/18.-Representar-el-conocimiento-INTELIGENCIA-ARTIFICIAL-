# Crear una base de conocimiento con reglas iniciales
base_conocimiento = {
    "puede_volar": ["pájaros"],
    "no_puede_volar": ["pájaros que están enfermos"]
}

# Función para verificar si un objeto puede volar
def puede_volar(objeto):
    if objeto in base_conocimiento["puede_volar"]:
        return True
    elif objeto in base_conocimiento["no_puede_volar"]:
        return False
    else:
        return None

# Verificar si un pájaro puede volar
objeto_a_verificar = "pájaros"
resultado = puede_volar(objeto_a_verificar)

if resultado is None:
    print(f"No sabemos si {objeto_a_verificar} puede volar.")
elif resultado:
    print(f"Sí, {objeto_a_verificar} puede volar.")
else:
    print(f"No, {objeto_a_verificar} no puede volar.")
