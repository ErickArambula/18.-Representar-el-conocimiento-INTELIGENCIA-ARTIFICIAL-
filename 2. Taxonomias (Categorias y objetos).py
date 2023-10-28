class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Meow!"

# Crear instancias de animales
fido = Perro("Fido")
whiskers = Gato("Whiskers")

# Acceder a los métodos de hablar
print(fido.nombre, "dice:", fido.hablar())
print(whiskers.nombre, "dice:", whiskers.hablar())
