"""
Representa el cargo o puesto de un empleado.
"""

class Cargo:
    def __init__(self, nombre: str, nivel: str = "Operativo"):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del cargo no puede estar vacío.")
        self._nombre = nombre.strip()
        self._nivel = nivel.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def nivel(self) -> str:
        return self._nivel

    def __repr__(self) -> str:
        return f"Cargo(nombre={self._nombre!r}, nivel={self._nivel!r})"