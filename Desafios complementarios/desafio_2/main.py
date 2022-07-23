
from datetime import datetime
from gestor_turnos.Cliente import Cliente
from gestor_turnos.Vehiculo import Vehiculo
from gestor_turnos.Turno import Turno
from gestor_turnos.administrador_turnos import AdministradorTurnos


administrador_turnos = AdministradorTurnos()

def create_menu():
    return """
    1) Crear turno 
    2) Buscar turno 
    3) Editar turno 
    4) Eliminar turno 
    5) Ver los turnos del dia
    6) Salir        
    """

def crear_turno():

    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    documento = input("Documento del cliente: ")

    cliente = Cliente(nombre, apellido, documento)

    marca = input("Marca del vehiculo: ")
    modelo = input("Modelo del vehiculo: ")
    matricula = input("Matricula del vehiculo: ")

    vehiculo = Vehiculo(marca, modelo, matricula)


    fecha = input("Ingrese la fecha del turno (formato: dd/mm/YYYY): ")
    motivo = input("Ingrese el motivo de la reparacion: ")
    turno = Turno(fecha, cliente, vehiculo, motivo)

    administrador_turnos.agregar_turno(turno)



def algoritmo_busqueda(turnos: list, fecha: str, documento_cliente: str, matricula_vehiculo: str) -> tuple:
    for indice, turno in enumerate(turnos):
        if turno.fecha_turno.strftime("%d/%m/%Y") == fecha and turno.cliente.get_documento() == documento_cliente and turno.vehiculo.get_matricula() == matricula_vehiculo:
            return indice, turno
    else:
        print("Turno no encontrado")
        return None, None


def buscar_turno():

    fecha = input("Ingrese la fecha (formato dd/mm/YYY): ")
    documento_cliente = input("Ingrese el documento del cliente: ")
    matricula_vehiculo = input("Ingrese la matricula del vehiculo: ")

    info_turno = algoritmo_busqueda(administrador_turnos.get_turnos(), fecha, documento_cliente,matricula_vehiculo)
    
    if info_turno[1] != None:
        print("Turno encontrado:", info_turno[1])
    else:
        print("Turno no encontrado")


def editar_turno():
    fecha = input("Ingrese la fecha (formato dd/mm/YYY): ")
    documento_cliente = input("Ingrese el documento del cliente: ")
    matricula_vehiculo = input("Ingrese la matricula del vehiculo: ")

    info_turno = algoritmo_busqueda(administrador_turnos.get_turnos(), fecha, documento_cliente,matricula_vehiculo)

    indice = info_turno[0]

    if indice != None:
        nueva_fecha = input("Ingrese la nueva fecha (formato dd/mm/YYY): ")
        nuevo_motivo = input("Ingrese el nuevo motivo: ")

        administrador_turnos.turnos[indice].fecha_turno = datetime.strptime(nueva_fecha, "%d/%m/%Y")
        administrador_turnos.turnos[indice].motivo = nuevo_motivo
    else:
        print("Turno no encontrado")
    

def eliminar_turno():
    fecha = input("Ingrese la fecha (formato dd/mm/YYY): ")
    documento_cliente = input("Ingrese el documento del cliente: ")
    matricula_vehiculo = input("Ingrese la matricula del vehiculo: ")

    info_turno = algoritmo_busqueda(administrador_turnos.get_turnos(), fecha, documento_cliente,matricula_vehiculo)

    indice = info_turno[0]

    if indice != None:    
        del administrador_turnos.turnos[indice]
    else:
        print("Turno no encontrado")
    

def turnos_del_dia():

    fecha_actual = datetime.now()

    for turno in administrador_turnos.get_turnos():
        if turno.fecha_turno.strftime("%d/%m/%Y") == fecha_actual.strftime("%d/%m/%Y"):
            print(turno)



# Comienzo del programa
print(create_menu())
opcion = int(input("--> "))

while( 1 <= opcion <6 ):
    if opcion == 1:
        crear_turno()
    elif opcion == 2:
        buscar_turno()
    elif opcion == 3:
        editar_turno()
    elif opcion == 4:
        eliminar_turno()
    elif opcion == 5:
        turnos_del_dia()

    print(create_menu())
    opcion = int(input("--> "))

else:
    print("Saliendo... ")
