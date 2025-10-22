from Dominio.Empleado import Empleado
from Dominio.Departamento import Departamento
from Dominio.Cargo import Cargo

class GestorEmpleados:
    """
    Clase encargada de gestionar empleados dentro del sistema.
    Permite crear, buscar, listar y modificar empleados.
    """

    def __init__(self):
        self._empleados = []

    def crear_empleado(self, nombre, fecha_nac, direccion, telefono,
                    id_empleado, fecha_ingreso, salario,
                    departamento: Departamento, cargo: Cargo, email=""):
        """
        Crea un nuevo empleado y lo agrega a la lista interna.
        Retorna el objeto creado o None si ocurre un error.
        """
        if self.buscar_por_id(id_empleado):
            print(f"Ya existe un empleado con ID {id_empleado}.")
            return None

        try:
            empleado = Empleado(
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
            
            empleado._cargo = cargo
            self._empleados.append(empleado)
            return empleado
        except Exception as e:
            print("Error al crear empleado:", e)
            return None

    def listar_empleados(self):
        """
        Retorna una lista de todos los empleados registrados.
        """
        return list(self._empleados)

    def buscar_por_id(self, id_empleado):
        """
        Busca un empleado por su ID. Retorna el objeto o None si no se encuentra.
        """
        return next((emp for emp in self._empleados if emp.id_empleado == id_empleado), None)

    def asignar_departamento(self, id_empleado, nuevo_departamento: Departamento):
        """
        Asigna un nuevo departamento a un empleado existente.
        Retorna True si se actualiza correctamente, False si no se encuentra.
        """
        empleado = self.buscar_por_id(id_empleado)
        if empleado:
            empleado._departamento = nuevo_departamento  
            return True
        return False

    def asignar_cargo(self, id_empleado, nuevo_cargo: Cargo):
        """
        Asigna un nuevo cargo a un empleado existente.
        Retorna True si se actualiza correctamente, False si no se encuentra.
        """
        empleado = self.buscar_por_id(id_empleado)
        if empleado:
            empleado._cargo = nuevo_cargo  
            return True
        return False