import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestiorProyectos import GestorProyectos
from Aplicacion.GestiorDeTiempo import GestiorDeTiempo

from Dominio.Departamento import Departamento
from Dominio.Cargo import Cargo
from Dominio.Tarea import Tarea

def main():
    gestor_empleados = GestorDeEmpleados()
    gestor_proyectos = GestorProyectos()
    gestor_tiempo = GestiorDeTiempo()

    dep_logistica = Departamento("Logística")
    cargo_analista = Cargo("Analista", "Técnico")

    
    empleado = gestor_empleados.crear_empleado(
        nombre="Felipe",
        fecha_nac="1990-03-15",
        direccion="Calle Central 123",
        telefono="555-0000",
        id_empleado=1,
        fecha_ingreso="2022-01-10",
        salario=1200000,
        departamento=dep_logistica,
        cargo=cargo_analista,
        email="felipe@empresa.com"
    )

    
    proyecto = gestor_proyectos.crear_proyecto(
        nombre="Sistema Inventario",
        descripcion="Desarrollo de sistema de control de stock",
        fecha_inicio="2025-10-01",
        fecha_fin="2025-12-31"
    )

    gestor_proyectos.asignar_empleado("Sistema Inventario", empleado)

    registro = gestor_tiempo.registrar_tiempo(
        empleado=empleado,
        proyecto=proyecto,
        fecha="2025-10-22",
        horas=6.5
    )

    print("\n--- Registro creado ---")
    if registro:
        print(registro.mostrar_info())

    print("\n--- Total horas por empleado ---")
    total_empleado = gestor_tiempo.calcular_total_horas_empleado(1)
    print(f"Empleado {empleado.nombre}: {total_empleado} horas")

    print("\n--- Total horas por proyecto ---")
    total_proyecto = gestor_tiempo.calcular_total_horas_proyecto("Sistema Inventario")
    print(f"Proyecto {proyecto.nombre}: {total_proyecto} horas")

if __name__ == "__main__":
    main()