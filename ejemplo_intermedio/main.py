from utils import cargar_logs, filtrar_severidad, contar_eventos
from pathlib import Path

def main():
    #ruta = "./logs/app.log"
    BASE_DIR = Path(__file__).parent
    ruta = BASE_DIR / "logs" / "app.log"
    #print (f"La ruta es {ruta}")
    logs = cargar_logs(ruta)

    severidad = "ERROR"
    filtrados = filtrar_severidad(logs, severidad)
    conteo = contar_eventos(filtrados)

    print(f"Total {severidad}: {conteo}")

if __name__ == "__main__":
    main()
