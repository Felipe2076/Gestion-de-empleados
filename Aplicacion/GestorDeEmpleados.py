from Dominio.Empleado import Empleado
from datetime import datetime

class GestorEmpleados:
    def __init__(self):
        self._empleados = []

    def crear_empleado(self):
        try:
            id_empleado = int(input("ID empleado: "))
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha nacimiento (YYYY-MM-DD): ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            fecha_ingreso = input("Fecha ingreso (YYYY-MM-DD HH:MM): ")
            salario = float(input("Salario: "))
            departamento = input("Departamento: ")
            cargo = input("Cargo: ")
            email = input("Email: ")

            fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d").date()
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d %H:%M")

            empleado = Empleado(id_empleado, nombre, fecha_nac, direccion, telefono,
                                fecha_ingreso, salario, departamento, cargo, email)
            self._empleados.append(empleado)
            print("Empleado creado correctamente.")
        except ValueError as e:
            print(f"Error al crear empleado: {e}")

    def listar_empleados(self):
        if not self._empleados:
            print("No hay empleados registrados.")
            return
        for emp in self._empleados:
            print("\n" + emp.mostrar_info())

    def actualizar_salario(self):
        try:
            id_empleado = int(input("ID del empleado a actualizar: "))
            for emp in self._empleados:
                if emp.id_empleado == id_empleado:
                    nuevo_salario = float(input(f"Salario actual: {emp.salario}. Nuevo salario: "))
                    emp.salario = nuevo_salario
                    print("Salario actualizado.")
                    return
            print("Empleado no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")

    def eliminar_empleado(self):
        try:
            id_empleado = int(input("ID del empleado a eliminar: "))
            for emp in self._empleados:
                if emp.id_empleado == id_empleado:
                    self._empleados.remove(emp)
                    print("Empleado eliminado.")
                    return
            print("Empleado no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")