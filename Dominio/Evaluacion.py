"""
Representa una evaluación de desempeño de un empleado.
"""

class Evaluacion:
    def __init__(self, empleado, fecha: str, evaluador: str, comentario: str, puntaje: int):
        if not fecha or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")
        if not evaluador or not evaluador.strip():
            raise ValueError("El evaluador no puede estar vacío.")
        if puntaje < 0 or puntaje > 100:
            raise ValueError("El puntaje debe estar entre 0 y 100.")
        self._empleado = empleado
        self._fecha = fecha.strip()
        self._evaluador = evaluador.strip()
        self._comentario = comentario.strip()
        self._puntaje = puntaje

    @property
    def empleado(self):
        return self._empleado

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def evaluador(self) -> str:
        return self._evaluador

    @property
    def comentario(self) -> str:
        return self._comentario

    @property
    def puntaje(self) -> int:
        return self._puntaje

    def mostrar_info(self) -> str:
        return (
            f"Evaluación | Fecha: {self._fecha} | Evaluador: {self._evaluador} | "
            f"Puntaje: {self._puntaje} | Comentario: {self._comentario}"
        )