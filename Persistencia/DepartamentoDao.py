from Dominio.Departamento import Departamento
from Persistencia.conexionBD import conexionbd
from typing import Optional, List


class DepartamentoDao:
	"""DAO simple para Departamentos usando ConexionBD."""

	def __init__(self, db_conf: dict = None):
		self._conexion = conexionbd(**(db_conf or {}))

	def crear(self, departamento: Departamento) -> None:
		query = "INSERT INTO Departamentos (nombre) VALUES (%s)"
		self._conexion.execute(query, (departamento.nombre,))

	def obtener_por_nombre(self, nombre: str) -> Optional[Departamento]:
		query = "SELECT * FROM Departamentos WHERE nombre = %s"
		filas = self._conexion.execute(query, (nombre,))
		if not filas:
			return None
		f = filas[0]
		return Departamento(nombre=f.get("nombre"))

	def listar_todos(self) -> List[Departamento]:
		query = "SELECT * FROM Departamentos"
		filas = self._conexion.execute(query)
		return [Departamento(nombre=f.get("nombre")) for f in filas]

	def eliminar(self, nombre: str) -> bool:
		query = "DELETE FROM Departamentos WHERE nombre = %s"
		self._conexion.execute(query, (nombre,))
		return True

	def actualizar(self, nombre: str, nuevo_nombre: str) -> Optional[Departamento]:
		query = "UPDATE Departamentos SET nombre = %s WHERE nombre = %s"
		self._conexion.execute(query, (nuevo_nombre, nombre))
		return self.obtener_por_nombre(nuevo_nombre)
