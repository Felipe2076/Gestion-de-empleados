from Dominio.Registro_Tiempo import RegistroTiempo
from Persistencia.Conexion_BD import ConexionBD
from typing import Optional, List


class RepositorioRegistroTiempo:
    """Repositorio MySQL para registros de tiempo."""

    def __init__(self, db_conf: dict = None):
        self._conexion = ConexionBD(**(db_conf or {}))

    def crear(self, registro: RegistroTiempo) -> None:
        query = """
            INSERT INTO RegistrosTiempo (empleado_id, proyecto_nombre, fecha, horas)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            registro.empleado_id,
            registro.proyecto_nombre,
            registro.fecha,
            registro.horas,
        )
        self._conexion.ejecutar(query, params)

    def obtener_por_id(self, id_registro: int) -> Optional[RegistroTiempo]:
        query = "SELECT * FROM RegistrosTiempo WHERE id = %s"
        filas = self._conexion.ejecutar(query, (id_registro,))
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
        filas = self._conexion.ejecutar(query, (empleado_id,))
        return [
            RegistroTiempo(
                id_registro=f.get("id"),
                empleado_id=f.get("empleado_id"),
                proyecto_nombre=f.get("proyecto_nombre"),
                fecha=str(f.get("fecha")),
                horas=float(f.get("horas")),
            )
            for f in filas
        ]

    def eliminar(self, id_registro: int) -> bool:
        query = "DELETE FROM RegistrosTiempo WHERE id = %s"
        self._conexion.ejecutar(query, (id_registro,))
        return True

    def actualizar(self, id_registro: int, cambios: dict) -> Optional[RegistroTiempo]:
        campos = ", ".join(f"{k} = %s" for k in cambios.keys())
        valores = list(cambios.values()) + [id_registro]
        query = f"UPDATE RegistrosTiempo SET {campos} WHERE id = %s"
        self._conexion.ejecutar(query, tuple(valores))
        return self.obtener_por_id(id_registro)

    def cerrar(self):
        self._conexion.cerrar()
