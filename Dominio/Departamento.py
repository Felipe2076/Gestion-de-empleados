"""
Representa un departamento simple.
"""

class Departamento:
    def __init__(self, nombre: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del departamento no puede estar vacío")
        self._nombre = nombre.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    def __repr__(self) -> str:
        return f"Departamento(nombre={self._nombre!r})"