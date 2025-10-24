from Dominio.Proyecto import Proyecto
from Persistencia.conexionBD import conexionbd
from typing import Optional, List


class RepositorioProyectos:
    """Repositorio simple para proyectos."""

    def __init__(self, db_conf: dict = None):
        self._conexion = conexionbd(**(db_conf or {}))

    def crear(self, proyecto: Proyecto) -> None:
        query = "INSERT INTO Proyectos (nombre, descripcion, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"
        self._conexion.execute(query, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin))

    def obtener_por_nombre(self, nombre: str) -> Optional[Proyecto]:
        query = "SELECT * FROM Proyectos WHERE nombre = %s"
        filas = self._conexion.execute(query, (nombre,))
        if not filas:
            return None
        f = filas[0]
        return Proyecto(
            id_proyecto=f.get("id"),
            nombre=f.get("nombre"),
            descripcion=f.get("descripcion"),
            fecha_inicio=str(f.get("fecha_inicio")),
            fecha_fin=str(f.get("fecha_fin")),
        )

    def listar_todos(self) -> List[Proyecto]:
        query = "SELECT * FROM Proyectos"
        filas = self._conexion.execute(query)
        return [self.obtener_por_nombre(f.get("nombre")) for f in filas if f.get("nombre")]

    def eliminar(self, nombre: str) -> bool:
        query = "DELETE FROM Proyectos WHERE nombre = %s"
        self._conexion.execute(query, (nombre,))
        return True

    def actualizar(self, nombre: str, cambios: dict) -> Optional[Proyecto]:
        campos = ", ".join(f"{k} = %s" for k in cambios.keys())
        valores = list(cambios.values()) + [nombre]
        query = f"UPDATE Proyectos SET {campos} WHERE nombre = %s"
        self._conexion.execute(query, tuple(valores))
        return self.obtener_por_nombre(cambios.get("nombre", nombre))

