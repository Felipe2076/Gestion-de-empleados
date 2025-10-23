"""Script de demostración para la capa de Presentación.

Simula un flujo completo: crear departamento/cargo, crear empleado, crear proyecto,
asignar empleado, registrar tiempo y opcionalmente intentar persistir en MySQL.
"""

from Aplicacion.GestorDeEmpleados import GestorEmpleados
from Aplicacion.GestiorProyectos import GestorProyectos
from Aplicacion.GestiorDeTiempo import GestorTiempo

from Dominio.Departamento import Departamento
from Dominio.Cargo import Cargo


def main():
    print("Iniciando demo de presentación...")

    gestor_empleados = GestorEmpleados()
    gestor_proyectos = GestorProyectos()
    gestor_tiempo = GestorTiempo()

    
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

    if empleado is None:
        print("No se pudo crear el empleado. Abortando demo.")
        return

    print("Empleado creado:", empleado.mostrar_info())

    
    proyecto = gestor_proyectos.crear_proyecto(
        nombre="Sistema Inventario",
        descripcion="Desarrollo de sistema de control de stock",
        fecha_inicio="2025-10-01",
        fecha_fin="2025-12-31"
    )

    if proyecto is None:
        print("No se pudo crear el proyecto. Abortando demo.")
        return

    print("Proyecto creado:", proyecto.nombre)

    
    ok = gestor_proyectos.asignar_empleado(proyecto.nombre, empleado)
    print("Empleado asignado al proyecto:" , ok)

    
    registro = gestor_tiempo.registrar_tiempo(
        empleado=empleado,
        proyecto=proyecto,
        fecha="2025-10-22",
        horas=6.5
    )

    print("Registro creado:", bool(registro))
    if registro:
        try:
            print(registro.mostrar_info())
        except Exception:
            pass

    
    total_empleado = gestor_tiempo.calcular_total_horas_empleado(empleado.id_empleado)
    total_proyecto = gestor_tiempo.calcular_total_horas_proyecto(proyecto.nombre)

    print(f"\n--- Totales ---")
    print(f"Empleado {empleado.nombre}: {total_empleado} horas")
    print(f"Proyecto {proyecto.nombre}: {total_proyecto} horas")

    
    try:
        from Persistencia.RepositorioEmpleados import RepositorioEmpleados
        print("Intentando persistir en MySQL (si está disponible)...")
        try:
            repo = RepositorioEmpleados(db_conf={})
            repo.guardar(empleado)
            print("Empleado guardado (MySQL).")
        except Exception as e:
            print("No se pudo persistir en MySQL:", e)
    except Exception:
        print("Módulo Persistencia.RepositorioEmpleados no disponible; omitiendo guardado en BD.")


if __name__ == "__main__":
    main()
