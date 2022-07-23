


class Animal:

    def __init__(self, especie: str, alimentacion: str, tiene_pelo: bool, patas: int) -> None:
        self.especie = especie
        self.alimentacion = alimentacion
        self.tiene_pelo = tiene_pelo
        self.patas = patas

    def comunicarse(self):
        print("Soy un animal y me estoy comunicando")

    def reproducirse(self):
        pass

    def comer(self):
        pass

    def moverse(self):
        pass

    def __str__(self):
        return f"Soy un animal de la especie {self.especie}. Soy {self.alimentacion} y tengo {self.patas} patas"



class Perro(Animal):
    
    def comunicarse(self):
        print("Guau")

class Felinos:
    pass

class Gato(Felinos, Animal):

    def __init__(self, especie: str, alimentacion: str, tiene_pelo: bool, patas: int, nombre: str ) -> None:
        super().__init__(especie, alimentacion, tiene_pelo, patas)
        self.nombre = nombre
        
    
    def print_nombre(self):
        print(self.nombre)

    def comunicarse(self):
        super().comunicarse()
        print("Miau")

    def __str__(self):
        cadena = super().__str__() + f".Mi nombre es: {self.nombre}"
        return cadena

class Vaca(Animal):
    pass

gatito = Gato("Felino", "Carnivoro", True, 4, "Pepe")

print(Gato.__mro__)