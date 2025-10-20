class Departamento:
    """Representa un departamento simple."""

    def __init__(self, nombre: str):
        if not nombre:
            raise ValueError("El nombre del departamento no puede estar vacío")
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre

    def __repr__(self) -> str:
        return f"Departamento(nombre={self._nombre!r})"
