class RegistroTiempo:
    def __init__(self, empleado, proyecto, fecha: str, horas: float):
        if empleado is None:
            raise ValueError("El empleado no puede ser None.")
        if proyecto is None:
            raise ValueError("El proyecto no puede ser None.")
        if not fecha or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero.")

        self._empleado = empleado
        self._proyecto = proyecto
        self._fecha = fecha.strip()
        self._horas = horas

    
    def empleado(self):
        return self._empleado

    
    def proyecto(self):
        return self._proyecto

    
    def fecha(self) -> str:
        return self._fecha

    
    def horas(self) -> float:
        return self._horas

    def mostrar_info(self) -> str:
        return (
            f"Registro de tiempo | "
            f"Empleado: {self._empleado.nombre} | "
            f"Proyecto: {self._proyecto.nombre} | "
            f"Fecha: {self._fecha} | "
            f"Horas trabajadas: {self._horas:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"RegistroTiempo(empleado={self._empleado.nombre!r}, "
            f"proyecto={self._proyecto.nombre!r}, fecha={self._fecha!r}, horas={self._horas})"
        )