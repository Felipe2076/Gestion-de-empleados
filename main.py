# main.py
from Persistencia.ConexionBD import ConexionBD
from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestorProyectos import GestorProyectos
from Aplicacion.GestorDeTiempo import GestiorDeTiempo
from Presentacion.cli import  menu_principal

# ------------------------------------------------------------------
#  Punto de entrada principal del sistema de gestión de empleados
# ------------------------------------------------------------------

def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

    # 1️⃣ Conectar a la base de datos
    conexion = ConexionBD()
    conexion.connect()
    print("✅ Conexión a la base de datos establecida.")

    # 2️⃣ Inicializar los gestores de aplicación
    Gestor_empleado = GestorDeEmpleados()
    Gestor_proyecto = GestorProyectos()
    Gestor_tiempo = GestiorDeTiempo()

    # 3️⃣ Iniciar la interfaz de usuario (CLI)
    try:
        menu_principal(GestorDeEmpleados, GestorProyectos, GestiorDeTiempo)
    except KeyboardInterrupt:
        print("\n🚪 Programa finalizado por el usuario.")
    finally:
        try:
            conexion.cerrar()
            print("🔒 Conexión cerrada.")
        except Exception:
            pass


# Ejecuta main() solo si se llama directamente
if __name__ == "__main__":
    main()
