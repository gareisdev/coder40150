from datetime import datetime
from gestor_turnos.Cliente import Cliente
from gestor_turnos.Vehiculo import Vehiculo


class Turno:

    def __init__(self, fecha_turno: str, cliente: Cliente, vehiculo: Vehiculo, motivo_reparacion: str):

            self.fecha_turno = datetime.strptime(fecha_turno, "%d/%m/%Y")
            self.cliente = cliente
            self.vehiculo = vehiculo
            self.motivo_reparacion = motivo_reparacion

    def __str__(self) -> str:
        return f"Fecha: {self.fecha_turno.strftime('%d/%m/%Y')} | Cliente: {self.cliente.get_documento()} | Vehiculo: {self.vehiculo.get_matricula()} | Motivo: {self.motivo_reparacion}"
