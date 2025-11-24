from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    nombre: str
    completada: bool = False
