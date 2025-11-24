# bibliotenjo
Repositorio para clases de programacion Biblioteca Tenjo 2025
## Para el ejemplo_intermedio
## Para el ejemplo_avanzado

Se ejecuta en shell
pip install -r requirements.txt
y luego

uvicorn main:app --reload

En una ventana aparte se puede ir al navegador e ir a http://127.0.0.1:8000/tareas y a http://127.0.0.1:8000/docs#/default/raiz__get

en un shell se puede ejecuta

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":1,\"nombre\":\"Aprender Python\",\"completada\":false}"

curl -X POST http://127.0.0.1:8000/tareas -H "Content-Type: application/json" -d "{\"id\":30,\"nombre\":\"Aprender Python 3\",\"completada\":true}"

