"""CLI mínima para la capa de Presentación.

Permite crear empleados y listar empleados y proyectos.
"""

from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
from Aplicacion.GestiorProyectos import GestorProyectos


# Presentacion/cli.py

def menu_principal(gestor_empleados=None, gestor_proyectos=None, gestor_tiempo=None):
    """
    Modo flexible:
      - Si se llama desde main.py, recibirá los 3 gestores por parámetro.
      - Si se ejecuta este archivo directamente, crea los gestores aquí.
    """
    # Fallback: crea gestores solo si no vinieron por parámetro
    if gestor_empleados is None or gestor_proyectos is None or gestor_tiempo is None:
        # IMPORTS PEREZOSOS para evitar problemas de rutas/nombres
        try:
            # tu archivo es GestorDeEmpleados.py pero clase puede ser GestorDeEmpleados o GestorEmpleados (alias)
            from Aplicacion.GestorDeEmpleados import GestorDeEmpleados
        except ImportError:
            from Aplicacion.GestorDeEmpleados import GestorEmpleados as GestorDeEmpleados

        # OJO: el archivo correcto es GestiorProyectos.py (con 'r' después de Gestio)
        from Aplicacion.GestiorProyectos import GestorProyectos
        from Aplicacion.GestiorDeTiempo import GestiorDeTiempo

        gestor_empleados = GestorDeEmpleados()
        gestor_proyectos = GestorProyectos()
        gestor_tiempo = GestiorDeTiempo()

    while True:
        print("\n--- Menú CLI ---")
        print("1. Crear empleado")
        print("2. Listar empleados")
        print("3. Crear proyecto")
        print("4. Listar proyectos")
        print("0. Salir")
        opc = input("Opción: ").strip()

        if opc == "1":
            nombre = input("Nombre: ").strip()
            fecha_nac = input("Fecha nac (YYYY-MM-DD): ").strip()
            direccion = input("Dirección: ").strip()
            telefono = input("Teléfono: ").strip()
            id_empleado = int(input("ID empleado: ").strip())
            fecha_ingreso = input("Fecha ingreso: ").strip()
            salario = float(input("Salario: ").strip())
            departamento = input("Departamento: ").strip()

            empleado = gestor_empleados.crear_empleado(
                nombre=nombre,
                fecha_nac=fecha_nac,
                direccion=direccion,
                telefono=telefono,
                id_empleado=id_empleado,
                fecha_ingreso=fecha_ingreso,
                salario=salario,
                departamento=None,  # simplificado
                cargo=None,
                email=""
            )
            print("✅ Empleado creado:", empleado)

        elif opc == "2":
            print(gestor_empleados.listar_empleados())

        elif opc == "3":
            nombre = input("Nombre proyecto: ").strip()
            descripcion = input("Descripción: ").strip()
            inicio = input("Inicio (YYYY-MM-DD): ").strip()
            fin = input("Fin (YYYY-MM-DD): ").strip()
            p = gestor_proyectos.crear_proyecto(nombre, descripcion, inicio, fin)
            print("✅ Proyecto creado:", p)

        elif opc == "4":
            print(gestor_proyectos.listar_proyectos())

        elif opc == "0":
            break
        else:
            print("Opción no válida")


# Permite ejecutar este archivo directamente (python -m Presentacion.cli)
if __name__ == "__main__":
    menu_principal()

