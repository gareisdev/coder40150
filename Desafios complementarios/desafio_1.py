
class Persona:

    def __init__(self, nombre: str, apellido: str, documento: str, saldo: float = 0.0) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.__saldo = saldo
    
    def __str__(self) -> str:
        return f"{self.apellido.upper()}, {self.nombre.capitalize()} - Documento: {self.documento}"
        
    def get_saldo(self):
        return self.__saldo
    
    def realizar_pago(self, monto):
        self.__saldo -= monto
    
    def realizar_deposito(self, monto):
        self.__saldo += monto


class Banco:

    def __init__(self, nombre, direccion) -> None:
        self.clientes = []
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self) -> str:
        return f"Banco {self.nombre}. Direccion: {self.direccion}"

    def agregar_persona(self, persona: Persona):
        self.clientes.append(persona)
    
    def consultar_cuenta_bancaria(self, documento: str) -> Persona:
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente


# -------------------

# Creamos un banco
banco = Banco("Torphy - Goyette", "144 Tyson Creek")

# Creamos algunos clientes
cliente1 = Persona("Maude", "Marks", "31759695", 921.00)
cliente2 = Persona("Barbara", "Koch", "32546333", 493.00)

# Los agregamos al banco (vemos como tenemos una relacion de AGREGACION)
banco.agregar_persona(cliente1)
banco.agregar_persona(cliente2)

# Obtenemos sus saldos
cliente = banco.consultar_cuenta_bancaria("31759695")

# Validamos que hayamos obtenido un cliente
if cliente:
   print(f"Saldo de {cliente}: ${cliente.get_saldo()}")

# Hacemos algunas operaciones
cliente1.realizar_pago(100)

# Obtenemos sus saldos
cliente = banco.consultar_cuenta_bancaria("31759695")

# Validamos que hayamos obtenido un cliente
if cliente:
   print(f"Saldo de {cliente}: ${cliente.get_saldo()}")