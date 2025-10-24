from datetime import date, datetime
from Dominio.Persona import Persona
class Empleado(Persona):
    def __init__ (self, id_empleado:int, nombre: str, fecha_nac: date, direccion: str, telefono: str, fecha_ingreso: datetime, salario: float, departamento=None, email: str = "", cargo =""):
        super().__init__(nombre, fecha_nac, direccion, telefono)
        self._id_empleado = id_empleado
        self._fecha_ingreso = fecha_ingreso
        self._salario = salario
        self._departamento = departamento
        self._email = email
        self._cargo = cargo
        self._proyectos = []
        self.registros_tiempo = []
    def asignar_proyecto(self, proyecto):
        if proyecto not in self._proyectos:
            self._proyectos.append(proyecto)
            proyecto.asignar_empleado(self)
    
    def registrar_tiempo(self, registro):
        self.registros_tiempo.append(registro)
        registro.empleado = self
    def mostrar_info(self):
        base_info = super().mostrar_info()
        depto = self._departamento.nombre if self._departamento else "Sin asignar"
        return (
            f"{base_info}, ID: {self.id_empleado}, Ingreso: {self.fecha_ingreso.strftime('%Y-%m-%d %H:%M')}, "
            f"Salario: ${self.salario}, Cargo: {self.cargo}, Email: {self.email}, Departamento: {depto}"
        )
