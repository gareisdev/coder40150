from gestor_turnos.Turno import Turno


class AdministradorTurnos:

    def __init__(self) -> None:
        self.turnos = []

    def agregar_turno(self, turno: Turno):
        self.turnos.append(turno)
    
    def get_turnos(self):
        return self.turnos

