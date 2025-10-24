from Dominio.Proyecto import Proyecto
from Persistencia.Conexion_BD import ConexionBD
from typing import Optional, List


class RepositorioProyectos:
    """Repositorio MySQL para proyectos."""

    def __init__(self, db_conf: dict = None):
        self._conexion = ConexionBD(**(db_conf or {}))

    def crear(self, proyecto: Proyecto) -> None:
        query = """
            INSERT INTO Proyectos (nombre, descripcion, fecha_inicio, fecha_fin)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            proyecto.nombre,
            proyecto.descripcion,
            proyecto.fecha_inicio,
            proyecto.fecha_fin,
        )
        self._conexion.ejecutar(query, params)

    def obtener_por_nombre(self, nombre: str) -> Optional[Proyecto]:
        query = "SELECT * FROM Proyectos WHERE nombre = %s"
        filas = self._conexion.ejecutar(query, (nombre,))
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
        filas = self._conexion.ejecutar(query)
        return [
            Proyecto(
                id_proyecto=f.get("id"),
                nombre=f.get("nombre"),
                descripcion=f.get("descripcion"),
                fecha_inicio=str(f.get("fecha_inicio")),
                fecha_fin=str(f.get("fecha_fin")),
            )
            for f in filas
        ]

    def eliminar(self, nombre: str) -> bool:
        query = "DELETE FROM Proyectos WHERE nombre = %s"
        self._conexion.ejecutar(query, (nombre,))
        return True

    def actualizar(self, nombre: str, cambios: dict) -> Optional[Proyecto]:
        campos = ", ".join(f"{k} = %s" for k in cambios.keys())
        valores = list(cambios.values()) + [nombre]
        query = f"UPDATE Proyectos SET {campos} WHERE nombre = %s"
        self._conexion.ejecutar(query, tuple(valores))
        return self.obtener_por_nombre(cambios.get("nombre", nombre))

    def cerrar(self):
        self._conexion.cerrar()

