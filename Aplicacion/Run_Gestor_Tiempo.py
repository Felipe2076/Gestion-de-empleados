import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dominio.Empleado import Empleado
from Dominio.Proyecto import Proyecto
from Aplicacion.GestorDeTiempo import GestorTiempo

gestor = GestorTiempo()

empleado = Empleado(
    id_empleado=101,
    nombre="Empleado Genérico",
    fecha_nac="1995-05-15",
    direccion="Dirección X",
    telefono="987654321",
    fecha_ingreso="2022-03-01",
    salario=850000,
    departamento=None
)

proyecto = Proyecto(
    nombre="Proyecto Genérico",
    descripcion="Descripción de prueba",
    fecha_inicio="2024-01-01",
    fecha_fin="2024-12-31"
)

proyecto.asignar_empleado(empleado)

registro = gestor.registrar_tiempo(
    empleado=empleado,
    proyecto=proyecto,
    fecha="2024-06-10",
    horas=7
)

print("Registro creado:", registro)
print("Total horas del empleado:", gestor.calcular_total_horas_empleado(101))
print("Total horas del proyecto:", gestor.calcular_total_horas_proyecto("Proyecto"))