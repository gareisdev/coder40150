
class Mamifero:
    def __init__(self, cant_mamas, esperanza_vida) -> None:
        self.cant_mamas = cant_mamas
        self.esperanza_vida = esperanza_vida

    def mamar(self):
        print("Me estoy alimentando")
    
    def nacer(self):
        print("Hello world!")


class AnimalMarino:
    
    def __init__(self, tiene_branquias, especie) -> None:
        self.tiene_branquias = tiene_branquias
        self.especie = especie

    def nadar(self):
        print("Estoy nadando")

class Cetaceo(Mamifero, AnimalMarino):
    
    def __init__(self, cant_mamas, esperanza_vida, tiene_branquias, especie, notas, vive_en, peso):

        Mamifero.__init__(self, cant_mamas, esperanza_vida)
        AnimalMarino.__init__(self, tiene_branquias, especie)    

        self.notas = notas
        self.vive_en = vive_en
        self.peso = peso



animal = Cetaceo(2, 10, True, "Imaginaria", "ninguna porque me distraje", "Rio parana", 250)
print(animal.cant_mamas)