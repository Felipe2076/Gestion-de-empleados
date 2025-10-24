class Persona:
    def __init__(self, nombre, fecha_nac, direccion, telefono, email):
        self._nombre = nombre
        self._fecha_nac = fecha_nac
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    def mostrar_info(self):
        return (
            f"Nombre: {self._nombre}\n"
            f"Fecha de nacimiento: {self._fecha_nac}\n"
            f"Dirección: {self._direccion}\n"
            f"Teléfono: {self._telefono}\n"
            f"Email: {self._email}"
        )