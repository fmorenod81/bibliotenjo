# bibliotenjo
Repositorio para clases de programacion Biblioteca Tenjo 2025

- Requisitos:
   - Un Editor de Desarollo Integrado, Integrated Development Editor. Mi recomendacion es Visual Studio Code.
   - Python Instalado. Se recomienda instalar el Python Package Installer, pip.
   - Configurar el IDE con el Python, para realizar debugger usando el IDE.

## Para el ejemplo_intermedio

Ir al terminal de Windows de la carpeta de ejemplo_intermedio

```
cd ejemplo_intermedio
```

Revisar que contiene el archivo de logs
```
type .\logs\app.log
```

Leer el codigo de los archivos, empezar con 

Se recomienda colocar varios puntos de debug (breakpoints) y luego, realizar la ejecucion del IDE en modo debug.
Colocar variables en Watch para realizar la verificacion del codigo.

## Para el ejemplo_avanzado

Ir al terminal de Windows de la carpeta de ejemplo_avanzado

```python
cd ejemplo_avanzado
```

Se crea un entorno virtual, en algunos casos es recomendable para evitar incompatibilidad de versiones.

```python
python -m venv venv

.\venv\Scripts\activate

```

Luego, se procede a realizar la instalacion de dependencias

```python
pip install -r requirements.txt
```

Para el inicio del debug usando el ejemplo completo de Microsoft usando [FastAPI](https://code.visualstudio.com/docs/python/tutorial-fastapi), sin embargo, segui este ejemplo de [Youtube](https://youtu.be/C-bie4ZY_o0?t=227) usando el audio en español; y poner breakpoints en diferentes lugares para detener el procedimiento.

Si es muy complicado, se puede usar la opcion de -pero es importante quitar el punto de "from .models import Tarea" para que sea "from models import Tarea"-

```
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

para salir de uvicorn, se oprime simulateamente ctrl+c .

Ahora si vamos a empezar a probar usando el navegador o linea de consola.

Por el navegador (Chrome, Edge, Firefox) ir a :
```
http://127.0.0.1:8000/
```
o a 
```
http://127.0.0.1:8000/docs
```
y mirar las tareas vacias
```
http://127.0.0.1:8000/tareas
```

en una terminal separada se puede ejecuta:

```python

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":1,\"nombre\":\"Aprender Python\",\"completada\":false}"

```
y mas revisar las tareas o los docs para ejecucion. Se pueden agregar mas registros

```python
curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":30,\"nombre\":\"Aprender Python 3\",\"completada\":true}"

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":35,\"nombre\":\"Aprender OOP\",\"completada\":false}"

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":45,\"nombre\":\"Aprender Portugues\",\"completada\":true}"

```
Luego, se puede hacer la comprobacion del mismo usando curl

```python
curl http://127.0.0.1:8000/
```
o la lista de tareas usando
```
curl http://127.0.0.1:8000/tareas
```

Si deseas salir de tu entorno virtual solamente en mismo terminal, escribes

```python
deactivate 
```