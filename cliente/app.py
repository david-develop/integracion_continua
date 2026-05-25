import requests
import time
import os

SERVIDOR_URL = os.getenv("SERVIDOR_URL", "http://servidor:5000")

def consultar():
    try:
        respuesta = requests.get(f"{SERVIDOR_URL}/mensaje", timeout=5)
        datos = respuesta.json()
        print(f"[Cliente] Respuesta recibida: {datos}", flush=True)
    except requests.exceptions.ConnectionError:
        print("[Cliente] No se pudo conectar al servidor. Reintentando...", flush=True)
    except Exception as e:
        print(f"[Cliente] Error: {e}", flush=True)

if __name__ == "__main__":
    print("[Cliente] Iniciando. Consultando al servidor cada 5 segundos...", flush=True)
    while True:
        consultar()
        time.sleep(5)
