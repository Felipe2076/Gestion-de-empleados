from Persona import Persona


def test_mostrar_info():
    p = Persona("Ana", "1990-01-01", "Calle Falsa 123", "555-1234", "ana@example.com")
    info = p.mostrar_info()
    assert "Ana" in info
    assert "1990-01-01" in info
    assert "Calle Falsa 123" in info
    assert "555-1234" in info
    assert "ana@example.com" in info


if __name__ == "__main__":
    test_mostrar_info()
    print("test_persona passed")
