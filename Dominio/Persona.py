from datetime import date

class Persona:
    def __init__(self, nombre: str,  fecha_nacimiento:date, direccion: str, telefono:str):
        self._nombre = nombre
        self._direccion = direccion
        self._fecha_nacimiento = fecha_nacimiento
        self._telefono = telefono
    
    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre}, Fecha Nac: {self.fecha_nac.strftime('%Y-%m-%d')}, "
            f"Dirección: {self.direccion}, Teléfono: {self.telefono}"
        )
