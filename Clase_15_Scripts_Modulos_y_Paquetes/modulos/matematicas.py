


def suma(a,b):
    return a+b


def resta(a,b):
    return a-b


def dividir(a,b):
    return a//b


def multiplicacion(a,b):
    return a*b


def modulo(a,b):
    return a%b

class NumerosImaginarios:

    def __init__(self, real, imaginaria) -> None:
        self.real = real
        self.imaginaria = imaginaria
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginaria}i"


pi = 3.14159