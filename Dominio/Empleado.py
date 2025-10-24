from Dominio.Persona import Persona

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, fecha_nac, direccion, telefono, fecha_ingreso, salario, departamento=None):
        super().__init__(nombre, fecha_nac, direccion, telefono)
        self.id_empleado = id_empleado
        self.fecha_ingreso = fecha_ingreso
        self.salario = salario
        self.departamento = departamento
        self.proyectos = []
        self.registros_tiempo = []

    def asignar_proyecto(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
            proyecto.asignar_empleado(self)

    def registrar_tiempo(self, registro):
        self.registros_tiempo.append(registro)
        registro.empleado = self

    def mostrar_info(self):
        base_info = super().mostrar_info()
        depto = self.departamento.nombre if self.departamento else "Sin asignar"
        return (
            f"{base_info}, ID: {self.id_empleado}, Ingreso: {self.fecha_ingreso}, "
            f"Salario: ${self.salario}, Departamento: {depto}"
        )