from datetime import date, datetime

class Usuario:
    def __init__(self,
                id_empleado: int,
                nombre: str,
                direccion: str,
                telefono: str,
                correo: str,
                fecha_nacimiento: date,
                fecha_ingreso: datetime,
                salario: float,
                puesto: str):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.salario = salario
        self.puesto = puesto
        self.departamento = None
        self.proyectos = []

    def asignar_departamento(self, departamento):
        self.departamento = departamento

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_info(self) -> str:
        return f"{self.nombre} ({self.puesto}) - ${self.salario}"