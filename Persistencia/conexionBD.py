import pymysql

class conexionbd:

    def __init__(self):
        self.host = "localhost"          
        self.user = "root"         
        self.password = ""    
        self.database = "base"          

    def obtener_conexion(self):
        """
        Establece y devuelve una conexión con la base de datos.
        """
        try:
            conexion = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Conexión establecida con la base de datos.")
            return conexion
        except pymysql.MySQLError as e:
            print(f"Error de conexión: {e}")
            raise  # Reenvía la excepción para manejarla fuera si es necesario

    def cerrar_conexion(self, conexion):
        """
        Cierra una conexión activa.
        """
        if conexion:
            conexion.close()
            print("Conexión cerrada correctamente.")

