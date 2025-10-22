"""Paquete Aplicacion para la gestión de lógica del sistema.
Contiene los gestores que coordinan empleados, proyectos y tiempo trabajado.
"""

__all__ = ["GestorDeEmpleados", "GestorProyectos", "GestiorDeTiempo"]

from .GestorDeEmpleados import GestorDeEmpleados
# Los archivos actuales se llaman 'GestiorProyectos.py' y 'GestiorDeTiempo.py'
from .GestiorProyectos import GestorProyectos
from .GestiorDeTiempo import GestiorDeTiempo