"""Pequeño wrapper para conexiones MySQL usando pymysql.

Proporciona un contexto simple para ejecutar queries y cerrar la conexión.
"""

import importlib


class ConexionBD:
    def __init__(self, host="localhost", user="root", password="", db="empleados", port=3306):
        self._conf = {
            "host": host,
            "user": user,
            "password": password,
            "db": db,
            "port": port,
        }
        self._conn = None
        self._pymysql = None

    def connect(self):
        if self._conn is None:
            if self._pymysql is None:
                try:
                    self._pymysql = importlib.import_module("pymysql")
                except ModuleNotFoundError:
                    raise RuntimeError("pymysql no está disponible. Instala 'pymysql' para usar ConexionBD.")
            conf = dict(self._conf)
            conf.update({
                "cursorclass": self._pymysql.cursors.DictCursor,
                "charset": "utf8mb4",
            })
            self._conn = self._pymysql.connect(**conf)
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def execute(self, query, params=None):
        conn = self.connect()
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            try:
                res = cur.fetchall()
            except Exception:
                res = []
        conn.commit()
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
