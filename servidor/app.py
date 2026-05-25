from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def index():
    return {"servicio": "servidor", "estado": "activo"}

@app.get("/mensaje")
def mensaje():
    return {
        "mensaje": "Hola desde el servidor!",
        "hora": datetime.datetime.now().isoformat()
    }
