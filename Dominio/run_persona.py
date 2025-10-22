"""
Script de prueba para la clase Persona del paquete Dominio.
Crea una instancia y muestra su información.
"""

try:
    from Dominio.Persona import Persona
except ImportError as e:
    print("Error al importar la clase Persona:", e)
    exit(1)

def main():
    try:
        persona = Persona(
            nombre="Juan",
            fecha_nac="1985-05-20",
            direccion="Av. Siempreviva 742",
            telefono="600-0000",
            email="juan@ejemplo.com"
        )
        print("Información de la persona:")
        print(persona.mostrar_info())
    except Exception as e:
        print("Error al crear o mostrar la persona:", e)

if __name__ == "__main__":
    main()
