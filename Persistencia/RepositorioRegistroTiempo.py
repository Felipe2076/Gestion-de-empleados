from Dominio.Registro_Tiempo import RegistroTiempo
from Persistencia.ConexionBD import ConexionBD
from typing import Optional, List


class RepositorioRegistroTiempo:
    """Repositorio para registros de tiempo."""

    def __init__(self, db_conf: dict = None):
        self._conexion = ConexionBD(**(db_conf or {}))

    def crear(self, registro: RegistroTiempo) -> None:
        query = "INSERT INTO RegistrosTiempo (empleado_id, proyecto_nombre, fecha, horas) VALUES (%s, %s, %s, %s)"
        self._conexion.execute(query, (registro.empleado_id, registro.proyecto_nombre, registro.fecha, registro.horas))

    def obtener_por_id(self, id_registro: int) -> Optional[RegistroTiempo]:
        query = "SELECT * FROM RegistrosTiempo WHERE id = %s"
        filas = self._conexion.execute(query, (id_registro,))
        if not filas:
            return None
        f = filas[0]
        return RegistroTiempo(
            id_registro=f.get("id"),
            empleado_id=f.get("empleado_id"),
            proyecto_nombre=f.get("proyecto_nombre"),
            fecha=str(f.get("fecha")),
            horas=float(f.get("horas")),
        )

    def listar_por_empleado(self, empleado_id: int) -> List[RegistroTiempo]:
        query = "SELECT * FROM RegistrosTiempo WHERE empleado_id = %s"
        filas = self._conexion.execute(query, (empleado_id,))
        return [self.obtener_por_id(f.get("id")) for f in filas]

    def eliminar(self, id_registro: int) -> bool:
        query = "DELETE FROM RegistrosTiempo WHERE id = %s"
        self._conexion.execute(query, (id_registro,))
        return True
