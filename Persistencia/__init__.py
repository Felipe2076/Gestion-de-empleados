"""
Paquete Persistencia para la gestión de almacenamiento de datos.

Contiene utilidades para acceso a base de datos (MySQL) y repositorios.

Notas:
- La dependencia 'pymysql' se importa dinámicamente dentro de ConexionBD.connect().
- Si no usas MySQL, puedes usar persistencia en JSON desde RepositorioEmpleados.
"""

import logging

__all__ = [
    "ConexionBD",
    "RepositorioEmpleados",
    "DepartamentoDao",
    "RepositorioProyectos",
    "RepositorioRegistroTiempo",
    "create_conexion"
]

logger = logging.getLogger(__name__)

try:
    from .Conexion_BD import ConexionBD
except Exception:
    ConexionBD = None
    logger.debug("No se pudo importar ConexionBD", exc_info=True)

try:
    from .RepositorioEmpleados import RepositorioEmpleados
except Exception:
    RepositorioEmpleados = None
    logger.debug("No se pudo importar RepositorioEmpleados", exc_info=True)

try:
    from .DepartamentoDao import DepartamentoDao
except Exception:
    DepartamentoDao = None
    logger.debug("No se pudo importar DepartamentoDao", exc_info=True)

try:
    from .RepositorioProyectos import RepositorioProyectos
except Exception:
    RepositorioProyectos = None
    logger.debug("No se pudo importar RepositorioProyectos", exc_info=True)

try:
    from .RepositorioRegistroTiempo import RepositorioRegistroTiempo
except Exception:
    RepositorioRegistroTiempo = None
    logger.debug("No se pudo importar RepositorioRegistroTiempo", exc_info=True)

def create_conexion(**conf):
    if ConexionBD is None:
        raise RuntimeError("ConexionBD no está disponible. Revisa las dependencias e imports.")
    return ConexionBD(**conf)
