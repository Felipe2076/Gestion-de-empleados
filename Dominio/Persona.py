class Persona:
    """Modelo simple de una persona con propiedades de acceso."""

    def __init__(self, nombre: str, fecha_nac: str, direccion: str, telefono: str, email: str = ""):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre
        self._fecha_nac = fecha_nac
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

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
        info = [
            f"Nombre: {self.nombre}",
            f"Fecha de nacimiento: {self.fecha_nac}",
            f"Dirección: {self.direccion}",
            f"Teléfono: {self.telefono}",
            f"Email: {self.email if self.email else 'No registrado'}"
        ]
        return " | ".join(info)