
class Cliente:

    def __init__(self, nombre: str, apellido: str, documento: str):
        self.nombre = nombre
        self.apellido = apellido
        self.__documento = documento

    def __str__(self) -> str:
        return f"{self.apellido.upper()}, {self.nombre.title()} | Documento: {self.__documento}"
    
    def set_documento(self, nuevo_documento: str):
        self.__documento = nuevo_documento

    def get_documento(self) -> str:
        return self.__documento
