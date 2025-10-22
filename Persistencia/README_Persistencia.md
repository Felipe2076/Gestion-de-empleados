# Persistencia — resumen rápido

Este documento contiene la explicación breve de cómo la capa de Persistencia se integra con las demás capas, un ejemplo de código de uso, y la sentencia SQL sugerida para crear la tabla `Empleados`.

## 1) Cómo se conecta con otras capas
- Desde la capa de Aplicación (por ejemplo, `GestorDeEmpleados`) se instancia o recibe el `RepositorioEmpleados` y llama a métodos como `guardar`, `obtener_por_id`, `listar_todos`.
- Desde la capa de Dominio se manipulan objetos `Empleado` que el repositorio traduce a consultas SQL.

Flujo típico:

```py
# En GestorDeEmpleados (capa de aplicación)
from Persistencia.RepositorioEmpleados import RepositorioEmpleados

repo = RepositorioEmpleados(db_conf={"host":"localhost", "user":"root", "password":"", "db":"sistema"})
repo.guardar(mi_empleado)
```

Ventajas:
- Desacoplamiento: los gestores no dependen de SQL.
- Reutilización: `ConexionBD` se puede usar en otros repositorios.
- Escalabilidad: puedes añadir repositorios (Proyectos, Registros, etc.).

## 2) Ejemplo de integración (GestorDeEmpleados -> Repositorio)

```py
from Persistencia import create_conexion
from Persistencia.RepositorioEmpleados import RepositorioEmpleados

# crear conexión y repositorio
conn = create_conexion(host="localhost", user="root", password="", db="sistema")
repo = RepositorioEmpleados(db_conf={"host":"localhost", "user":"root", "password":"", "db":"sistema"})

# suponer que 'empleado' es instancia de Dominio.Empleado
repo.guardar(empleado)

empleado_recuperado = repo.obtener_por_id(empleado.id_empleado)
```

## 3) SQL sugerido para `Empleados`

```sql
CREATE TABLE Empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(200) NOT NULL,
  fecha_nac DATE,
  direccion VARCHAR(300),
  telefono VARCHAR(50),
  fecha_ingreso DATE,
  salario DECIMAL(12,2),
  departamento VARCHAR(150),
  cargo VARCHAR(150),
  email VARCHAR(200)
);
```

Notas:
- Ajusta tipos de columna según necesidades (por ejemplo `DECIMAL` para salario). Si usas `datetime` cambia el tipo.

## 4) Frase de defensa corta

"La capa de persistencia permite que el sistema trabaje con objetos de alto nivel mientras delega el almacenamiento a una estructura especializada y segura. Cumple con principios de arquitectura limpia y facilita la escalabilidad y mantenimiento." 
