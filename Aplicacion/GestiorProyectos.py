from Dominio.Proyecto import Proyecto
from typing import List, Optional

class GestorProyectos:
    """
    Gestiona proyectos en memoria.
    NOTA: Mantiene el nombre del módulo/clase tal como los estás importando
    desde Presentacion/cli.py y Run_Gestor_Tiempo.py.
    """

    def __init__(self):
        self._proyectos: List[Proyecto] = []
        self._seq = 1  # autoincrement simple para id_proyecto

    # --- CRUD básico ---
    def crear_proyecto(self, nombre: str, descripcion: str, fecha_inicio: str, fecha_fin: str) -> Proyecto:
        p = Proyecto(self._seq, nombre, descripcion, fecha_inicio, fecha_fin)
        self._seq += 1
        self._proyectos.append(p)
        return p

    def listar_proyectos(self) -> List[Proyecto]:
        return list(self._proyectos)

    def buscar_por_nombre(self, nombre: str) -> Optional[Proyecto]:
        nombre = (nombre or "").strip().lower()
        for p in self._proyectos:
            if p.nombre.strip().lower() == nombre:
                return p
        return None

    def eliminar_por_nombre(self, nombre: str) -> bool:
        p = self.buscar_por_nombre(nombre)
        if not p: 
            return False
        self._proyectos.remove(p)
        return True

    # --- Asignaciones ---
    def asignar_empleado(self, nombre_proyecto: str, empleado) -> bool:
        """
        Asigna un empleado a un proyecto por nombre (como usas en Run_Gestor_Tiempo.py).
        """
        p = self.buscar_por_nombre(nombre_proyecto)
        if not p:
            return False
        p.asignar_empleado(empleado)
        # opcional: reflejar también en el empleado (si usas su lista interna)
        try:
            empleado.asignar_proyecto(p)
        except Exception:
            pass
        return True

    def empleados_del_proyecto(self, nombre_proyecto: str):
        p = self.buscar_por_nombre(nombre_proyecto)
        return p.listar_empleados() if p else []
