"""
Representa una tarea asignada dentro de un proyecto.
"""

class Tarea:
    def __init__(self, nombre: str, descripcion: str, responsable, estado: str = "Pendiente"):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la tarea no puede estar vacío.")
        if not descripcion or not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._nombre = nombre.strip()
        self._descripcion = descripcion.strip()
        self._responsable = responsable
        self._estado = estado.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def responsable(self):
        return self._responsable

    @property
    def estado(self) -> str:
        return self._estado

    def cambiar_estado(self, nuevo_estado: str):
        self._estado = nuevo_estado.strip()

    def __repr__(self) -> str:
        return f"Tarea(nombre={self._nombre!r}, estado={self._estado!r})"