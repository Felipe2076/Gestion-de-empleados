from Dominio.Empleado import Empleado
from Dominio.Departamento import Departamento

class GestorDeEmpleados:
    def __init__(self):
        self._empleados = []

    def crear_empleado(self, nombre, fecha_nac, direccion, telefono,
                    id_empleado, fecha_ingreso, salario,
                    departamento, email=""):
        if self.buscar_por_id(id_empleado):
            return None
        try:
            empleado = Empleado(
                id_empleado=id_empleado,
                nombre=nombre,
                fecha_nac=fecha_nac,
                direccion=direccion,
                telefono=telefono,
                fecha_ingreso=fecha_ingreso,
                salario=salario,
                departamento=departamento,
                email=email
            )
            self._empleados.append(empleado)
            return empleado
        except Exception:
            return None

    def listar_empleados(self):
        return list(self._empleados)

    def buscar_por_id(self, id_empleado):
        return next((e for e in self._empleados if e.id_empleado == id_empleado), None)

    def eliminar_empleado(self, id_empleado):
        empleado = self.buscar_por_id(id_empleado)
        if empleado:
            self._empleados.remove(empleado)
            return True
        return False

    def actualizar_datos(self, id_empleado, direccion=None, telefono=None, email=None):
        empleado = self.buscar_por_id(id_empleado)
        if not empleado:
            return False
        if direccion:
            empleado.direccion = direccion
        if telefono:
            empleado.telefono = telefono
        if email:
            empleado.email = email
        return True

    def asignar_departamento(self, id_empleado, nuevo_departamento):
        empleado = self.buscar_por_id(id_empleado)
        if empleado:
            empleado.departamento = nuevo_departamento
            return True
        return False

    def mostrar_info_empleado(self, id_empleado):
        empleado = self.buscar_por_id(id_empleado)
        if not empleado:
            return "Empleado no encontrado."
        return empleado.mostrar_info() if hasattr(empleado, "mostrar_info") else str(empleado)