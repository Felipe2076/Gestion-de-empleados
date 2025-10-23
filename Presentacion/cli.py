"""CLI mínima para la capa de Presentación.

Permite crear empleados y listar empleados y proyectos.
"""

from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestiorProyectos import GestorProyectos


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
            fecha_ingreso = input("Fecha ingreso: ")
            salario = float(input("Salario: "))
            departamento = input("Departamento: ")
            
            empleado = gestor_empleados.crear_empleado(
                nombre=nombre, fecha_nac=fecha_nac, direccion=direccion, telefono=telefono,
                id_empleado=id_empleado, fecha_ingreso=fecha_ingreso, salario=salario,
                departamento=None, cargo=None, email=""
            )
            print("Empleado creado:", empleado)
        elif opc == "2":
            print(gestor_empleados.listar_empleados())
        elif opc == "3":
            nombre = input("Nombre proyecto: ")
            descripcion = input("Descripción: ")
            inicio = input("Inicio: ")
            fin = input("Fin: ")
            p = gestor_proyectos.crear_proyecto(nombre, descripcion, inicio, fin)
            print("Proyecto creado:", p)
        elif opc == "4":
            print(gestor_proyectos.listar_proyectos())
        elif opc == "0":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
