class Marco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_atributo(self, nombre_atributo, valor):
        self.atributos[nombre_atributo] = valor

    def obtener_atributo(self, nombre_atributo):
        return self.atributos.get(nombre_atributo, None)

# Crear un marco para representar una persona
persona = Marco("Persona")
persona.agregar_atributo("nombre", "Juan")
persona.agregar_atributo("edad", 30)
persona.agregar_atributo("ciudad", "Ciudad de Ejemplo")

# Mostrar la información de la persona
print("Nombre:", persona.obtener_atributo("nombre"))
print("Edad:", persona.obtener_atributo("edad"))
print("Ciudad:", persona.obtener_atributo("ciudad"))
