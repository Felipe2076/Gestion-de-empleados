from Persistencia.conexionBD import conexionbd
from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestorDeProyectos import GestorProyectos
from Aplicacion.GestorDeTiempo import GestorDeTiempo
from Presentacion.menu import menu

def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

    conexion = conexionbd()
    conexion.obtener_conexion()
    print("Conexión a la base de datos establecida.")

    gestor_empleado = GestorDeEmpleados()
    gestor_proyecto = GestorProyectos()
    gestor_tiempo = GestorDeTiempo()

    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
    finally:
        try:
            conexion.cerrar()
            print("Conexión cerrada.")
        except Exception:
            pass


# Ejecuta main() solo si se llama directamente
if __name__ == "__main__":
    main()
