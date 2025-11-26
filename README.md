# bibliotenjo
Repositorio para clases de programacion Biblioteca Tenjo 2025

- Requisitos:
 Un Editor de Desarollo Integrado, Integrated Development Editor. Mi recomendacion es Visual Studio Code.
 Python Instalado. Se recomienda instalar el Python Package Installer, pip.
 Configurar el IDE con el Python, para realizar debugger usando el IDE.

## Para el ejemplo_intermedio

Ir al terminal de Windows de la carpeta de ejemplo_intermedio

```python
cd ejemplo_intermedio
```

Revisar que contiene el archivo de logs
```python
type .\logs\app.log
```
Se recomienda colocar varios puntos de debug (breakpoints) y luego, realizar la ejecucion del IDE en modo debug.
Colocar variables en Watch para realizar la verificacion del codigo.

## Para el ejemplo_avanzado

Se ejecuta en shell
pip install -r requirements.txt
y luego

uvicorn main:app --reload

En una ventana aparte se puede ir al navegador e ir a http://127.0.0.1:8000/tareas y a http://127.0.0.1:8000/docs#/default/raiz__get

en un shell se puede ejecuta

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":1,\"nombre\":\"Aprender Python\",\"completada\":false}"

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":30,\"nombre\":\"Aprender Python 3\",\"completada\":true}"


API en JSON: http://127.0.0.1:8000/

Lista de tareas: http://127.0.0.1:8000/tareas

Documentación interactiva: http://127.0.0.1:8000/docs