"""
Modelo simple de una persona con propiedades de acceso.
Incluye validación básica y método para mostrar información.
"""

class Persona:
    def __init__(self, nombre: str, fecha_nac: str, direccion: str, telefono: str, email: str = ""):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre.strip()
        self._fecha_nac = fecha_nac.strip()
        self._direccion = direccion.strip()
        self._telefono = telefono.strip()
        self._email = email.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def fecha_nac(self) -> str:
        return self._fecha_nac

    @property
    def direccion(self) -> str:
        return self._direccion

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def email(self) -> str:
        return self._email

    def mostrar_info(self) -> str:
        return " | ".join([
            f"Nombre: {self.nombre}",
            f"Fecha de nacimiento: {self.fecha_nac}",
            f"Dirección: {self.direccion}",
            f"Teléfono: {self.telefono}",
            f"Email: {self.email if self.email else 'No registrado'}"
        ])