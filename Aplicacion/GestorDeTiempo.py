from Dominio.Registro_Tiempo import RegistroTiempo
from Dominio.Empleado import Empleado
from Dominio.Proyecto import Proyecto

class GestorDeTiempo:
    def __init__(self):
        self._registros = []

    def registrar_tiempo(self, empleado, proyecto, fecha, horas):
        try:
            asignados = getattr(proyecto, "listar_empleados")()
        except Exception:
            asignados = []
        if empleado not in asignados:
            return None
        registro = RegistroTiempo(empleado, proyecto, fecha, horas)
        self._registros.append(registro)
        return registro

    def listar_registros(self):
        return list(self._registros)

    def obtener_registros_por_empleado(self, id_empleado):
        return [r for r in self._registros if r.empleado.id_empleado == id_empleado]

    def obtener_registros_por_proyecto(self, nombre_proyecto):
        nombre_proyecto = (nombre_proyecto or "").strip().lower()
        return [r for r in self._registros if r.proyecto.nombre.strip().lower() == nombre_proyecto]

    def calcular_total_horas_empleado(self, id_empleado):
        return sum(r.horas for r in self._registros if r.empleado.id_empleado == id_empleado)

    def calcular_total_horas_proyecto(self, nombre_proyecto):
        nombre_proyecto = (nombre_proyecto or "").strip().lower()
        total = 0
        for r in self._registros:
            try:
                pnombre = r.proyecto.nombre.strip().lower()
            except Exception:
                pnombre = getattr(r._proyecto, "_nombre", "").strip().lower()
            if pnombre == nombre_proyecto:
                total += r.horas
        return total