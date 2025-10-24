from Dominio.Proyecto import Proyecto
from Dominio.Empleado import Empleado

class GestorProyectos:
    def __init__(self):
        self._proyectos = []

    def crear_proyecto(self, nombre, descripcion, fecha_inicio, fecha_fin):
        if self.buscar_por_nombre(nombre):
            return None
        proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_fin)
        self._proyectos.append(proyecto)
        return proyecto

    def listar_proyectos(self):
        return list(self._proyectos)

    def buscar_por_nombre(self, nombre):
        nombre = (nombre or "").strip().lower()
        return next((p for p in self._proyectos if p.nombre.strip().lower() == nombre), None)

    def eliminar_proyecto(self, nombre):
        proyecto = self.buscar_por_nombre(nombre)
        if proyecto:
            self._proyectos.remove(proyecto)
            return True
        return False

    def asignar_empleado(self, nombre_proyecto, empleado):
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if not proyecto:
            return False
        try:
            proyecto.asignar_empleado(empleado)
            return True
        except Exception:
            return False

    def listar_empleados_de_proyecto(self, nombre_proyecto):
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if not proyecto:
            return []
        try:
            return proyecto.listar_empleados()
        except Exception:
            return []