from Dominio.Proyecto import Proyecto
from Dominio.Empleado import Empleado
from Dominio.Tarea import Tarea

class GestorProyectos:
    """
    Gestiona la creación y administración de proyectos.
    """

    def __init__(self):
        self._proyectos = []

    def crear_proyecto(self, nombre: str, descripcion: str, fecha_inicio: str, fecha_fin: str):
        """
        Crea un nuevo proyecto y lo agrega a la lista interna.
        """
        if self.buscar_por_nombre(nombre):
            print(f"Ya existe un proyecto con nombre '{nombre}'.")
            return None

        try:
            proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_fin)
            self._proyectos.append(proyecto)
            return proyecto
        except Exception as e:
            print("Error al crear proyecto:", e)
            return None

    def buscar_por_nombre(self, nombre: str):
        """
        Busca un proyecto por su nombre.
        """
        return next((p for p in self._proyectos if p.nombre == nombre), None)

    def listar_proyectos(self):
        """
        Retorna todos los proyectos registrados.
        """
        return list(self._proyectos)

    def asignar_empleado(self, nombre_proyecto: str, empleado: Empleado):
        """
        Asigna un empleado a un proyecto existente.
        """
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if proyecto:
            if empleado in proyecto.empleados_asignados:
                print(f"El empleado {empleado.nombre} ya está asignado al proyecto.")
                return False
            proyecto.empleados_asignados.append(empleado)
            return True
        print(f"Proyecto '{nombre_proyecto}' no encontrado.")
        return False

    def agregar_tarea(self, nombre_proyecto: str, tarea: Tarea):
        """
        Agrega una tarea a un proyecto existente.
        """
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if proyecto:
            proyecto.tareas.append(tarea)
            return True
        print(f"Proyecto '{nombre_proyecto}' no encontrado.")
        return False

    def listar_empleados_por_proyecto(self, nombre_proyecto: str):
        """
        Retorna la lista de empleados asignados a un proyecto.
        """
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if proyecto:
            return proyecto.empleados_asignados
        return []

    def listar_tareas_por_proyecto(self, nombre_proyecto: str):
        """
        Retorna la lista de tareas asociadas a un proyecto.
        """
        proyecto = self.buscar_por_nombre(nombre_proyecto)
        if proyecto:
            return proyecto.tareas
        return []