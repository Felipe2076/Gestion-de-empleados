class Departamento:
    def __init__(self, id_departamento: int, nombre: str, ubicacion: str):
        if id_departamento is None or int(id_departamento) <= 0:
            raise ValueError("id_departamento debe ser un entero positivo")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del departamento no puede estar vacío")

        self._id_departamento = int(id_departamento)
        self._nombre = nombre.strip()
        self._ubicacion = ubicacion.strip()
        self._empleados = []

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    def agregar_empleado(self, empleado) -> None:
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            empleado.departamento = self

    def eliminar_empleado(self, empleado) -> None:
        try:
            self._empleados.remove(empleado)
        except ValueError:
            pass

    def listar_empleados(self) -> list:
        return list(self._empleados)

    def mostrar_info(self) -> str:
        return (
            f"Departamento: {self._nombre} | Ubicación: {self._ubicacion} | "
            f"Empleados asignados: {len(self._empleados)}"
        )

    def __repr__(self) -> str:
        return f"Departamento(id_departamento={self._id_departamento}, nombre={self._nombre!r})"