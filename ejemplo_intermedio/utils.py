from pathlib import Path
from typing import List

def cargar_logs(ruta: str) -> List[str]:
    ruta = Path(ruta).resolve()
    return Path(ruta).read_text().splitlines()

def filtrar_severidad(logs: List[str], nivel: str) -> List[str]:
    return [l for l in logs if nivel in l]

def contar_eventos(logs_filtrados: List[str]) -> int:
    return len(logs_filtrados)
