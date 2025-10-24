class Usuario:
    def __init__(self, id_usuario: int, username: str, password: str, empleado):
        if id_usuario is None or int(id_usuario) <= 0:
            raise ValueError("id_usuario debe ser un entero positivo")
        if not username or not username.strip():
            raise ValueError("El nombre de usuario no puede estar vacío")

        self._id_usuario = int(id_usuario)
        self._username = username.strip()
        self._password = password
        self._empleado = empleado

    
    def id_usuario(self) -> int:
        return self._id_usuario

    
    def username(self) -> str:
        return self._username

    
    def password(self) -> str:
        return self._password

    
    def empleado(self):
        return self._empleado

    def verificar_credencial(self, input_password, cifrador) -> bool:
        return cifrador.descifrar(self._password) == input_password

    def mostrar_info(self) -> str:
        return f"Usuario: {self._username} | ID: {self._id_usuario} | Empleado: {self._empleado._nombre}"

    def __repr__(self) -> str:
        return f"Usuario(id_usuario={self._id_usuario}, username={self._username!r})"