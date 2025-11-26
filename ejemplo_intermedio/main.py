from utils import cargar_logs, filtrar_severidad, contar_eventos
from pathlib import Path


def main():
    BASE_DIR = Path(__file__).parent
    ruta = BASE_DIR / "logs" / "app.log"
    logs = cargar_logs(ruta)

    severidad = "ERROR"
    filtrados = filtrar_severidad(logs, severidad)
    conteo = contar_eventos(filtrados)

    print(f"Total {severidad}: {conteo}")

# Inicia por medio de esta funcion
if __name__ == "__main__":
    print("Ejecutando main.py")
    main()
