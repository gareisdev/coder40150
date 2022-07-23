from datetime import datetime


fecha_actual = datetime.now()

def segundos_cumple(fecha: str) -> float:
    
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")

    diferencia = fecha_dt - fecha_actual
    
    return diferencia.total_seconds()
    