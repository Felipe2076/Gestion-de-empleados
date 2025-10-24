from Dominio.Empleado import Empleado
from Persistencia.ConexionBD import ConexionBD
from typing import Optional, List
from Dominio.Departamento import Departamento
from Dominio.Cargo import Cargo


class RepositorioEmpleados:
    """Repositorio MySQL para empleados con fallback JSON simple.

    Requiere que exista una base de datos con tabla `Empleados` con columnas
    compatibles. Usa `ConexionBD` para ejecutar consultas.
    """

    def __init__(self, db_conf: dict = None):
        self._db_conf = db_conf or {}
        self._conexion = ConexionBD(**self._db_conf)

    def guardar(self, empleado: Empleado) -> None:
        query = """
            INSERT INTO Empleados (
                id, nombre, fecha_nac, direccion, telefono,
                fecha_ingreso, salario, departamento, cargo, email
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nombre = VALUES(nombre),
                fecha_nac = VALUES(fecha_nac),
                direccion = VALUES(direccion),
                telefono = VALUES(telefono),
                fecha_ingreso = VALUES(fecha_ingreso),
                salario = VALUES(salario),
                departamento = VALUES(departamento),
                cargo = VALUES(cargo),
                email = VALUES(email)
        """
        params = (
            empleado.id_empleado,
            empleado.nombre,
            empleado.fecha_nac,
            empleado.direccion,
            empleado.telefono,
            empleado._fecha_ingreso,
            empleado.salario,
            getattr(empleado.departamento, "nombre", None),
            getattr(empleado._cargo, "nombre", None),
            empleado.email,
        )
        self._conexion.execute(query, params)

    def obtener_por_id(self, id_empleado: int) -> Optional[Empleado]:
        query = "SELECT * FROM Empleados WHERE id = %s"
        resultados = self._conexion.execute(query, (id_empleado,))
        if not resultados:
            return None
        fila = resultados[0]
        # Reconstruir Departamento y Cargo si existen en tablas relacionadas
        departamento = None
        try:
            dep_nombre = fila.get("departamento")
            if dep_nombre:
                qd = "SELECT * FROM Departamentos WHERE nombre = %s"
                rdep = self._conexion.execute(qd, (dep_nombre,))
                if rdep:
                    drow = rdep[0]
                    departamento = Departamento(nombre=drow.get("nombre"))
        except Exception:
            departamento = None

        try:
            cargo_nombre = fila.get("cargo")
            if cargo_nombre:
                qc = "SELECT * FROM Cargos WHERE nombre = %s"
                rc = self._conexion.execute(qc, (cargo_nombre,))
                if rc:
                    crow = rc[0]
                    cargo = Cargo(nombre=crow.get("nombre"), nivel=crow.get("nivel"))
        except Exception:
            cargo = None

        return Empleado(
            nombre=fila.get("nombre"),
            fecha_nac=str(fila.get("fecha_nac")),
            direccion=fila.get("direccion"),
            telefono=fila.get("telefono"),
            id_empleado=fila.get("id"),
            fecha_ingreso=str(fila.get("fecha_ingreso")),
            salario=fila.get("salario"),
            departamento=departamento,
            email=fila.get("email") or "",
        )

    def listar_todos(self) -> List[Optional[Empleado]]:
        query = "SELECT id FROM Empleados"
        filas = self._conexion.execute(query)
        return [self.obtener_por_id(f.get("id")) for f in filas]

    def eliminar(self, id_empleado: int) -> bool:
        query = "DELETE FROM Empleados WHERE id = %s"
        self._conexion.execute(query, (id_empleado,))
        return True

    def actualizar(self, id_empleado: int, cambios: dict) -> Optional[Empleado]:
        campos = ", ".join(f"{k} = %s" for k in cambios.keys())
        valores = list(cambios.values()) + [id_empleado]
        query = f"UPDATE Empleados SET {campos} WHERE id = %s"
        self._conexion.execute(query, tuple(valores))
        return self.obtener_por_id(id_empleado)
