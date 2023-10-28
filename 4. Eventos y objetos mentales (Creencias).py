# Crear una lista de creencias iniciales
creencias = ["El cielo es azul", "El sol es caliente", "2 + 2 = 4"]

# Agregar una nueva creencia
nueva_creencia = "Los gatos son mamíferos"
creencias.append(nueva_creencia)

# Verificar si una creencia existe
if "El sol es caliente" in creencias:
    print("Sí, es una creencia.")

# Eliminar una creencia
if "El cielo es azul" in creencias:
    creencias.remove("El cielo es azul")

# Mostrar todas las creencias
print("Creencias actuales:")
for creencia in creencias:
    print(creencia)
