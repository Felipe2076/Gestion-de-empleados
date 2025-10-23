from Dominio.Registro_Tiempo import RegistroTiempo
from Dominio.Empleado import Empleado
from Dominio.Proyecto import Proyecto

class GestorTiempo:
    """
    Gestiona el registro de tiempo trabajado por empleados en proyectos.
    """

    def __init__(self):
        self._registros = []

    def registrar_tiempo(self, empleado: Empleado, proyecto: Proyecto, fecha: str, horas: float):
        """
        Registra horas trabajadas por un empleado en un proyecto en una fecha específica.
        """
        if horas <= 0:
            print("Las horas deben ser mayores a cero.")
            return None

        if not self._empleado_asignado(empleado, proyecto):
            print(f"El empleado {empleado.nombre} no está asignado al proyecto {proyecto.nombre}.")
            return None

        try:
            registro = RegistroTiempo(empleado, proyecto, fecha, horas)
            self._registros.append(registro)
            return registro
        except Exception as e:
            print("Error al registrar tiempo:", e)
            return None

    def _empleado_asignado(self, empleado: Empleado, proyecto: Proyecto) -> bool:
        """
        Verifica si el empleado está asignado al proyecto.
        """
        return empleado in proyecto.empleados_asignados

    def obtener_registros_por_empleado(self, id_empleado: int):
        """
        Retorna todos los registros de tiempo de un empleado por su ID.
        """
        return [r for r in self._registros if r.empleado.id_empleado == id_empleado]

    def obtener_registros_por_proyecto(self, nombre_proyecto: str):
        """
        Retorna todos los registros de tiempo asociados a un proyecto.
        """
        return [r for r in self._registros if r.proyecto.nombre == nombre_proyecto]

    def calcular_total_horas_empleado(self, id_empleado: int) -> float:
        """
        Calcula el total de horas trabajadas por un empleado.
        """
        return sum(r.horas for r in self._registros if r.empleado.id_empleado == id_empleado)

    def calcular_total_horas_proyecto(self, nombre_proyecto: str) -> float:
        """
        Calcula el total de horas registradas en un proyecto.
        """
        return sum(r.horas for r in self._registros if r.proyecto.nombre == nombre_proyecto)