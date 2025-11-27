from fastapi import FastAPI
from models import Tarea

app = FastAPI()
tareas_db = []

@app.get("/tareas")
def listar():
    return tareas_db

@app.post("/tareas")
def crear(tarea: Tarea):
    tareas_db.append(tarea)
    return {"mensaje": "Tarea creada", "tarea": tarea}

@app.get("/")
def raiz():
    mensaje = "API de tareas - Python 3.12 + FastAPI"
    return {"mensaje": "API de tareas - Python 3.12 + FastAPI"}

@app.get("/yellow")
def yellow():
    return {"cualquier": "Devuelve un yellow"}

#@app.get("/contar")
#def contar():
#    return len(tareas_db)