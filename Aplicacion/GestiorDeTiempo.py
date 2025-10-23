from typing import List
from Dominio.Registro_Tiempo import RegistroTiempo
from Dominio.Empleado import Empleado
from Dominio.Proyecto import Proyecto

class GestiorDeTiempo:
    """
    Registra horas por empleado/proyecto.
    Mantiene exactamente el nombre que importas en Run_Gestor_Tiempo.py.
    """

    def __init__(self):
        self._registros: List[RegistroTiempo] = []

    def registrar_tiempo(self, empleado: Empleado, proyecto: Proyecto, fecha: str, horas: float) -> RegistroTiempo:
        # Validación: el empleado debe estar asignado al proyecto
        try:
            asignados = getattr(proyecto, "listar_empleados")()
        except Exception:
            asignados = []
        if empleado not in asignados:
            raise ValueError("El empleado no está asignado al proyecto; asígnalo antes de registrar horas.")

        reg = RegistroTiempo(empleado, proyecto, fecha, horas)
        self._registros.append(reg)
        return reg

    def listar_registros(self) -> List[RegistroTiempo]:
        return list(self._registros)

    def calcular_total_horas_empleado(self, id_empleado: int) -> float:
        total = 0.0
        for r in self._registros:
            # Empleado en tu dominio expone id_empleado como _id_empleado con @property id_empleado
            try:
                rid = r.empleado.id_empleado
            except Exception:
                rid = getattr(r._empleado, "_id_empleado", None)
            if rid == id_empleado:
                total += r.horas
        return total

    def calcular_total_horas_proyecto(self, nombre_proyecto: str) -> float:
        nombre_proyecto = (nombre_proyecto or "").strip().lower()
        total = 0.0
        for r in self._registros:
            try:
                pnombre = r.proyecto.nombre.strip().lower()
            except Exception:
                pnombre = getattr(r._proyecto, "_nombre", "").strip().lower()
            if pnombre == nombre_proyecto:
                total += r.horas
        return total
