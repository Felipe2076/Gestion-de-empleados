"""
Registra cambios laborales de un empleado a lo largo del tiempo.
"""

class HistorialLaboral:
    def __init__(self, empleado, fecha: str, cargo, departamento, salario: float):
        if not fecha or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._empleado = empleado
        self._fecha = fecha.strip()
        self._cargo = cargo
        self._departamento = departamento
        self._salario = float(salario)

    @property
    def empleado(self):
        return self._empleado

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def cargo(self):
        return self._cargo

    @property
    def departamento(self):
        return self._departamento

    @property
    def salario(self) -> float:
        return self._salario

    def mostrar_info(self) -> str:
        return (
            f"Historial | Fecha: {self._fecha} | Cargo: {self._cargo.nombre} | "
            f"Departamento: {self._departamento.nombre} | Salario: ${self._salario:.2f}"
        )