class Departamento:
    def __init__(self, id_departamento: int, nombre: str, ubicacion: str):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.empleados = []
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.asignar_departamento(self)
    
    def mostrar_info(self) -> str:
        return f"Departamento: {self.nombre} | Ubicación: {self.ubicacion} | Empleados: {len(self.empleados)}"