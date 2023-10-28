# Importar la biblioteca para trabajar con valores de probabilidad
from fractions import Fraction

# Crear una afirmación con un valor de probabilidad
afirmacion = "Llueve"
probabilidad = Fraction(1, 2)  # Probabilidad del 50%

# Verificar si la afirmación es verdadera
import random

if random.random() < probabilidad:
    print(f"Sí, {afirmación} es verdadero con probabilidad {probabilidad}.")
else:
    print(f"No, {afirmación} no es verdadero con probabilidad {probabilidad}.")
