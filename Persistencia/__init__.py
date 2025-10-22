"""Paquete Persistencia para la gestión de almacenamiento de datos.

Contiene utilidades para acceso a base de datos (MySQL) y repositorios.

Notas:
- La dependencia "pymysql" se importa dinámicamente dentro de `ConexionBD.connect()`.
  Si no quieres usar MySQL puedes usar las funciones de persistencia en JSON en
  `RepositorioEmpleados`.
"""

from typing import Optional, Dict, Any
import logging

__all__ = ["ConexionBD", "RepositorioEmpleados", "create_conexion"]

logger = logging.getLogger(__name__)

# Importar módulos de forma robusta para que el paquete no falle al importarse
try:
	from .ConexionBD import ConexionBD
except Exception:
	ConexionBD = None  # type: ignore
	logger.debug("No se pudo importar ConexionBD", exc_info=True)

try:
	from .RepositorioEmpleados import RepositorioEmpleados
except Exception:
	RepositorioEmpleados = None  # type: ignore
	logger.debug("No se pudo importar RepositorioEmpleados", exc_info=True)


def create_conexion(**conf: Dict[str, Any]):
	"""Helper para crear una instancia de ConexionBD.

	Uso:
		from Persistencia import create_conexion
		conn = create_conexion(host="localhost", user="root", db="mi_bd")

	Lanza RuntimeError si `ConexionBD` no está disponible (por ejemplo, falta pymysql).
	"""
	if ConexionBD is None:
		raise RuntimeError("ConexionBD no está disponible. Revisa las dependencias e imports.")
	return ConexionBD(**conf)
