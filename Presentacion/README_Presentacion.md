# Capa de Presentación

Este directorio contiene scripts y utilidades para presentar y probar el sistema:

- `run_demo.py`: demo no interactiva que crea datos de ejemplo, asigna empleados a proyectos y registra tiempo.
- `cli.py`: CLI mínima para crear/listar empleados y proyectos desde consola.

Instrucciones rápidas:

```powershell
& "C:/Users/aixav/OneDrive/Escritorio/Gestion de empleados/.venv/Scripts/python.exe" "c:/Users/aixav/OneDrive/Escritorio/Gestion de empleados/Presentacion/run_demo.py"

# o iniciar la CLI
& "C:/Users/aixav/OneDrive/Escritorio/Gestion de empleados/.venv/Scripts/python.exe" "c:/Users/aixav/OneDrive/Escritorio/Gestion de empleados/Presentacion/cli.py"
```

Notas:
- Los scripts usan los gestores de la capa `Aplicacion` y los modelos de `Dominio`.
- `run_demo.py` intentará persistir un empleado en MySQL si `Persistencia.RepositorioEmpleados` está disponible y configurado.
