class Vehiculo:
    
    def __init__(self, marca: str, modelo: str, matricula: str):
        self.marca = marca
        self.modelo = modelo
        self.__matricula = matricula

    def __str__(self) -> str:
        return f"{self.marca.upper()}, {self.modelo.title()} | Matricula: {self.__matricula}"
    
    def set_matricula(self, nueva_matricula: str):
        self.__matricula = nueva_matricula

    def get_matricula(self) -> str:
        return self.__matricula