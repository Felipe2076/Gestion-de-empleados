from Dominio.Proyecto import Proyecto
from datetime import datetime

class GestorProyectos:
    def __init__(self):
        self._proyectos = []

    def crear_proyecto(self):
        try:
            id_proyecto = int(input("ID del proyecto: "))
            nombre = input("Nombre del proyecto: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")

            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

            proyecto = Proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin)
            self._proyectos.append(proyecto)
            print("Proyecto creado correctamente.")
        except ValueError as e:
            print(f"Error al crear proyecto: {e}")

    def listar_proyectos(self):
        if not self._proyectos:
            print("No hay proyectos registrados.")
            return
        for p in self._proyectos:
            print("\n" + p.mostrar_info())

    def actualizar_descripcion(self):
        try:
            id_proyecto = int(input("ID del proyecto a actualizar: "))
            for p in self._proyectos:
                if p.id_proyecto == id_proyecto:
                    nueva_desc = input(f"Descripción actual: {p.descripcion}\nNueva descripción: ")
                    p.descripcion = nueva_desc
                    print("Descripción actualizada.")
                    return
            print("Proyecto no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")

    def eliminar_proyecto(self):
        try:
            id_proyecto = int(input("ID del proyecto a eliminar: "))
            for p in self._proyectos:
                if p.id_proyecto == id_proyecto:
                    self._proyectos.remove(p)
                    print("Proyecto eliminado.")
                    return
            print("Proyecto no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")