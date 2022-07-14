

from gestor_pagos.tarjeta import Tarjeta
from gestor_pagos.persona import Persona

personita = Persona("Leonel", "Gareis")
personita.hablar("compra dolares cuando puedas")
print("Persona: ", personita)


tarj = Tarjeta('debito', 'Banco XXX', 'Leonel Gareis')
print( "Creando tarjeta ------> ", tarj.propietario, tarj.banco_emisor)
