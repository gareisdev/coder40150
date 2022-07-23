

class Persona:

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def hablar(self, mensaje):
        print(f"Hola! Soy {self.nombre} y te queria decir: {mensaje}")

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
