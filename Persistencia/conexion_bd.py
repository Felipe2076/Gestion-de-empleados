import pymysql

class ConexionBD:
    def __init__(self, host="localhost", user="root", password="", db="empresa"):
        self._config = {
            "host": host,
            "user": user,
            "password": password,
            "db": db
        }
        self._conexion = None
        self._cursor = None
        self.connect()

    def connect(self):
        try:
            self._conexion = pymysql.connect(**self._config)
            self._cursor = self._conexion.cursor()
        except Exception as e:
            raise RuntimeError(f"No se pudo conectar a la base de datos: {e}")

    def ejecutar(self, query, params=None):
        try:
            self._cursor.execute(query, params or ())
            self._conexion.commit()
            return self._cursor.fetchall()
        except Exception as e:
            self._conexion.rollback()
            raise RuntimeError(f"Error al ejecutar la consulta: {e}")

    def cerrar(self):
        if self._cursor:
            self._cursor.close()
        if self._conexion:
            self._conexion.close()
        self._cursor = None
        self._conexion = None