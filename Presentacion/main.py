from Persistencia.Conexion_BD import ConexionBD
from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestorDeProyectos import GestorProyectos
from Aplicacion.GestorDeTiempo import GestorDeTiempo
from Presentacion.menu import run_menu

def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

    conexion = ConexionBD()
    conexion.connect()
    print("Conexión a la base de datos establecida.")

    gestor_empleado = GestorDeEmpleados()
    gestor_proyecto = GestorProyectos()
    gestor_tiempo = GestorDeTiempo()

    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
    finally:
        try:
            conexion.cerrar()
            print("Conexión cerrada.")
        except Exception:
            pass



if __name__ == "__main__":
    main()
