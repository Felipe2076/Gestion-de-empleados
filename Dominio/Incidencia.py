"""
Representa una incidencia laboral (ausencia, bloqueo, problema).
"""

class Incidencia:
    def __init__(self, empleado, fecha: str, tipo: str, descripcion: str):
        if not fecha or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de incidencia no puede estar vacío.")
        if not descripcion or not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._empleado = empleado
        self._fecha = fecha.strip()
        self._tipo = tipo.strip()
        self._descripcion = descripcion.strip()

    @property
    def empleado(self):
        return self._empleado

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def descripcion(self) -> str:
        return self._descripcion

    def mostrar_info(self) -> str:
        return (
            f"Incidencia | Fecha: {self._fecha} | Tipo: {self._tipo} | "
            f"Descripción: {self._descripcion}"
        )