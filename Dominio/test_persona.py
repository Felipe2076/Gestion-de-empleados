"""
Prueba unitaria para el método mostrar_info de la clase Persona.
Verifica que todos los datos aparezcan correctamente en la salida.
"""

try:
    from Dominio.Persona import Persona
except ImportError as e:
    print("Error al importar la clase Persona:", e)
    exit(1)

def test_mostrar_info():
    try:
        p = Persona("Ana", "1990-01-01", "Calle Falsa 123", "555-1234", "ana@example.com")
        info = p.mostrar_info()
        assert "Ana" in info
        assert "1990-01-01" in info
        assert "Calle Falsa 123" in info
        assert "555-1234" in info
        assert "ana@example.com" in info
        print("test_mostrar_info passed")
    except AssertionError as e:
        print("Fallo en test_mostrar_info:", e)
    except Exception as e:
        print("Error inesperado en test_mostrar_info:", e)

if __name__ == "__main__":
    test_mostrar_info()