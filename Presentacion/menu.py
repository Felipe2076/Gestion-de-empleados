from Aplicacion.GestorDeEmpleados import GestorEmpleados
from Aplicacion.GestiorProyectos import GestorProyectos
from Aplicacion.GestiorDeTiempo import GestorTiempo

from Dominio.Departamento import Departamento
from Dominio.Cargo import Cargo


def _input_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except Exception:
        return 0


def run_menu():
    gestor_empleados = GestorEmpleados()
    gestor_proyectos = GestorProyectos()
    gestor_tiempo = GestorTiempo()

    while True:
        print("\n=== Menú Gestión de Empleados ===")
        print("1) Ejecutar demo rápido")
        print("2) Crear empleado")
        print("3) Listar empleados")
        print("4) Crear proyecto")
        print("5) Listar proyectos")
        print("6) Asignar empleado a proyecto")
        print("7) Registrar tiempo")
        print("8) Mostrar totales (empleado/proyecto)")
        print("9) Persistir empleado (si está habilitado)")
        print("0) Salir")

        opt = input("Selecciona una opción: ").strip()

        if opt == "1":
            from Presentacion.main import main as demo_main

            demo_main()

        elif opt == "2":
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha nacimiento (YYYY-MM-DD): ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            id_empleado = _input_int("ID empleado (número): ")
            fecha_ingreso = input("Fecha ingreso (YYYY-MM-DD): ")
            salario = float(input("Salario: ") or 0)
            dep_nombre = input("Departamento: ")
            cargo_nombre = input("Cargo: ")
            cargo_nivel = input("Nivel cargo (opcional): ") or ""
            email = input("Email: ")

            dep = Departamento(dep_nombre)
            cargo = Cargo(cargo_nombre, cargo_nivel)

            emp = gestor_empleados.crear_empleado(
                nombre=nombre,
                fecha_nac=fecha_nac,
                direccion=direccion,
                telefono=telefono,
                id_empleado=id_empleado,
                fecha_ingreso=fecha_ingreso,
                salario=salario,
                departamento=dep,
                cargo=cargo,
                email=email,
            )
            print("Empleado creado:" , bool(emp))

        elif opt == "3":
            emps = gestor_empleados.listar_empleados()
            if not emps:
                print("No hay empleados.")
            for e in emps:
                try:
                    print(e.mostrar_info())
                except Exception:
                    print(f"Empleado id={getattr(e,'id_empleado',None)}")

        elif opt == "4":
            nombre = input("Nombre proyecto: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
            p = gestor_proyectos.crear_proyecto(nombre, descripcion, fecha_inicio, fecha_fin)
            print("Proyecto creado:", bool(p))

        elif opt == "5":
            proys = gestor_proyectos.listar_proyectos()
            if not proys:
                print("No hay proyectos.")
            for p in proys:
                print(f"Proyecto: {p.nombre} - {getattr(p,'descripcion', '')}")

        elif opt == "6":
            id_empleado = _input_int("ID empleado: ")
            nombre_proy = input("Nombre proyecto: ")
            emp = gestor_empleados.buscar_por_id(id_empleado)
            if not emp:
                print("Empleado no encontrado.")
            else:
                ok = gestor_proyectos.asignar_empleado(nombre_proy, emp)
                print("Asignado:", ok)

        elif opt == "7":
            id_empleado = _input_int("ID empleado: ")
            nombre_proy = input("Nombre proyecto: ")
            emp = gestor_empleados.buscar_por_id(id_empleado)
            proyecto = gestor_proyectos.buscar_por_nombre(nombre_proy)
            if not emp or not proyecto:
                print("Empleado o proyecto no encontrados.")
            else:
                horas = float(input("Horas: ") or 0)
                reg = gestor_tiempo.registrar_tiempo(emp, proyecto, input("Fecha (YYYY-MM-DD): "), horas)
                print("Registro creado:", bool(reg))

        elif opt == "8":
            id_empleado = _input_int("ID empleado para totales: ")
            nombre_proy = input("Nombre proyecto para totales: ")
            print("Total empleado:", gestor_tiempo.calcular_total_horas_empleado(id_empleado))
            print("Total proyecto:", gestor_tiempo.calcular_total_horas_proyecto(nombre_proy))

        elif opt == "9":
            id_empleado = _input_int("ID empleado a persistir: ")
            emp = gestor_empleados.buscar_por_id(id_empleado)
            if not emp:
                print("Empleado no encontrado.")
            else:
                try:
                    from Persistencia.RepositorioEmpleados import RepositorioEmpleados
                    repo = RepositorioEmpleados(db_conf={})
                    repo.guardar(emp)
                    print("Empleado persistido (intento realizado).")
                except Exception as e:
                    print("No se pudo persistir:", e)

        elif opt == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    run_menu()
