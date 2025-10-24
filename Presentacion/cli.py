from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestorDeProyectos import GestorProyectos

def menu():
    gestor_empleados = GestorDeEmpleados()
    gestor_proyectos = GestorProyectos()

    while True:
        print("\n--- Menú CLI ---")
        print("1. Crear empleado")
        print("2. Listar empleados")
        print("3. Crear proyecto")
        print("4. Listar proyectos")
        print("0. Salir")
        opc = input("Opción: ")

        if opc == "1":
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha nac (YYYY-MM-DD): ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            id_empleado = int(input("ID empleado: "))
            fecha_ingreso = input("Fecha ingreso (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            departamento = input("Departamento: ")
            email = input("Email: ")

            empleado = gestor_empleados.crear_empleado(
                nombre=nombre,
                fecha_nac=fecha_nac,
                direccion=direccion,
                telefono=telefono,
                id_empleado=id_empleado,
                fecha_ingreso=fecha_ingreso,
                salario=salario,
                departamento=departamento,
                email=email
            )
            print("Empleado creado:", empleado)

        elif opc == "2":
            empleados = gestor_empleados.listar_empleados()
            for e in empleados:
                print(e)

        elif opc == "3":
            nombre = input("Nombre proyecto: ")
            descripcion = input("Descripción: ")
            inicio = input("Inicio (YYYY-MM-DD): ")
            fin = input("Fin (YYYY-MM-DD): ")
            proyecto = gestor_proyectos.crear_proyecto(nombre, descripcion, inicio, fin)
            print("Proyecto creado:", proyecto)

        elif opc == "4":
            proyectos = gestor_proyectos.listar_proyectos()
            for p in proyectos:
                print(p)

        elif opc == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")
