from Persona import Persona
from Departamento import Departamento

class Empleado(Persona):
    def __init__(self, nombre: str, fecha_nac: str, direccion: str, telefono: str,
                id_empleado: int, fecha_ingreso: str, salario: float, departamento: Departamento, email: str = ""):
        super().__init__(nombre, fecha_nac, direccion, telefono, email)
        self._id_empleado = id_empleado
        self._fecha_ingreso = fecha_ingreso
        if id_empleado <= 0:
            raise ValueError("id_empleado debe ser un entero positivo")
        if salario < 0:
            raise ValueError("salario no puede ser negativo")
        self._salario = float(salario)
        self._departamento = departamento
        self._proyectos = []

    def calcular_salario(self) -> float:
        return self._salario

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def salario(self) -> float:
        return self._salario

    @property
    def departamento(self) -> Departamento:
        return self._departamento

    def mostrar_info(self) -> str:
        return (
            f"{super().mostrar_info()}, "
            f"ID Empleado: {self._id_empleado}, "
            f"Fecha de ingreso: {self._fecha_ingreso}, "
            f"Salario: ${self._salario}"
        )

    def asignar_proyecto(self, proyecto):
        if proyecto not in self._proyectos:
            self._proyectos.append(proyecto)

    def listar_proyectos(self):
        return self._proyectos

