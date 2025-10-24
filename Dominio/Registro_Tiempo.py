from datetime import datetime
class RegistroTiempo:
    def __init__(self, id_registro: int,fecha: datetime, horas_trabajadas: float, descripcion: str,empleado,proyecto):
        self._id_registro = id_registro
        self._fecha = fecha
        self._horas = horas_trabajadas
        self._descripcion = descripcion
        self._empleado = empleado
        self._proyecto = proyecto
    
    def registrar(self):
        return f"El empleado {self._empleado._nombre} ha registrado {self._horas} horas en el proyecto {self._proyecto._nombre}"