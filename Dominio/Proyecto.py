class Proyecto:
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str,
                fecha_inicio: str, fecha_fin: str):
        if id_proyecto is None or int(id_proyecto) <= 0:
            raise ValueError("id_proyecto debe ser un entero positivo")
        if not nombre:
            raise ValueError("El nombre del proyecto no puede estar vacío")

        self._id_proyecto = int(id_proyecto)
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._empleados = []

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def fecha_inicio(self) -> str:
        return self._fecha_inicio

    @property
    def fecha_fin(self) -> str:
        return self._fecha_fin

    def asignar_empleado(self, empleado) -> None:
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    def eliminar_empleado(self, empleado) -> None:
        try:
            self._empleados.remove(empleado)
        except ValueError:
            pass

    def listar_empleados(self) -> list:
        return list(self._empleados)

    def mostrar_info(self) -> str:
        return (
            f"Proyecto: {self._nombre} | "
            f"Inicio: {self._fecha_inicio} | Fin: {self._fecha_fin} | "
            f"Descripción: {self._descripcion} | "
            f"Empleados asignados: {len(self._empleados)}"
        )

    def __repr__(self) -> str:
        return f"Proyecto(id_proyecto={self._id_proyecto}, nombre={self._nombre!r})"