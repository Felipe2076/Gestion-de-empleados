"""Paquete Aplicacion para la gestión de lógica del sistema.
Contiene los gestores que coordinan empleados, proyectos y tiempo trabajado.

Este __init__ usa importaciones seguras (try/except) para no romper la carga del
paquete si algún submódulo cambia de nombre o lanza errores. Los módulos se
pueden seguir importando directamente: `from Aplicacion.GestorDeEmpleados import GestorEmpleados`.
"""

from typing import Any

__all__ = ["GestorEmpleados", "GestorProyectos", "GestorTiempo"]

 
try:
	from .GestorDeEmpleados import GestorEmpleados  # type: Any
except Exception:
	GestorEmpleados = None  # type: ignore

try:
	from .GestiorProyectos import GestorProyectos  # type: Any
except Exception:
	GestorProyectos = None  # type: ignore

try:
	from .GestiorDeTiempo import GestorTiempo  # type: Any
except Exception:
	GestorTiempo = None  # type: ignore