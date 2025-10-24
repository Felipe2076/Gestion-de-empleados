from Dominio.Registro_Tiempo import RegistroTiempo
from datetime import datetime

class GestorRegistroTiempo:
    def __init__(self):
        self._registros = []

    def registrar_tiempo(self):
        try:
            id_registro = int(input("ID del registro: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            horas = float(input("Horas trabajadas: "))
            descripcion = input("Descripción del trabajo: ")

            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()

            registro = RegistroTiempo(id_registro, fecha, horas, descripcion)
            self._registros.append(registro)
            print("Registro de tiempo creado correctamente.")
        except ValueError as e:
            print(f"Error al registrar tiempo: {e}")

    def listar_registros(self):
        if not self._registros:
            print("No hay registros de tiempo.")
            return
        for r in self._registros:
            print("\n" + r.mostrar_info())

    def actualizar_descripcion(self):
        try:
            id_registro = int(input("ID del registro a actualizar: "))
            for r in self._registros:
                if r.id_registro == id_registro:
                    nueva_desc = input(f"Descripción actual: {r.descripcion}\nNueva descripción: ")
                    r.descripcion = nueva_desc
                    print("Descripción actualizada.")
                    return
            print("Registro no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")

    def eliminar_registro(self):
        try:
            id_registro = int(input("ID del registro a eliminar: "))
            for r in self._registros:
                if r.id_registro == id_registro:
                    self._registros.remove(r)
                    print("Registro eliminado.")
                    return
            print("Registro no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")