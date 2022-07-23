

class Animal:
    def __init__(self,nombre) -> None:
        self.nombre = nombre

    def hablar(self):
        pass


class Vaca(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def hablar(self):
        return "Muuu"

class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def hablar(self):
        return "Miau"

    def cazar_ratones(self):
        pass

g1 = Gato("Pepe")
p1 = Perro("Dogo")
v1 = Vaca("Lola")

animales = [g1, p1, v1]

for animal in animales:
    print( animal.hablar() )