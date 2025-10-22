"""
Representa el horario laboral de un empleado.
"""

class Horario:
    def __init__(self, empleado, dia: str, hora_inicio: str, hora_fin: str):
        if not dia or not dia.strip():
            raise ValueError("El día no puede estar vacío.")
        if not hora_inicio or not hora_fin:
            raise ValueError("Las horas de inicio y fin no pueden estar vacías.")
        self._empleado = empleado
        self._dia = dia.strip()
        self._hora_inicio = hora_inicio.strip()
        self._hora_fin = hora_fin.strip()

    @property
    def empleado(self):
        return self._empleado

    @property
    def dia(self) -> str:
        return self._dia

    @property
    def hora_inicio(self) -> str:
        return self._hora_inicio

    @property
    def hora_fin(self) -> str:
        return self._hora_fin

    def mostrar_info(self) -> str:
        return (
            f"Horario | Día: {self._dia} | Inicio: {self._hora_inicio} | Fin: {self._hora_fin}"
        )
