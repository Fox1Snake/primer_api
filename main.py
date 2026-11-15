from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_sensores():
    return {
        "estado": "opertativo",
        "cpu_temp": "45C",
        "ventilador": "1200 RPM",
        "mensaje": "Servidor funcionando perfecto"
    }