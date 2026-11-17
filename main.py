from fastapi import FastAPI
import random # Modulo nativo para elejir elementos al lazar

app = FastAPI()

# Dictionary of teach words to practice
tech_vocabulary = [
    {
        "word": "Deploy",
        "pronunciation": "/di'ploi/",
        "meaning": "Lanzar o publicar el codigo a un servidor real.",
        "example_sentence": "I need to deploy the new API today"
    },
    {
        "word": "Commit",
        "pronunciation": "/ka'mit/",
        "meaning": "Guardar los cambios en el repositorio.",
        "example_sentence": "Don't forget to commit your code."
    },
    {
        "word": "Request",
        "pronunciation": "/ri'kwest/",
        "meaning": "Una peticion de datos que se hace al servidor.",
        "example_sentence": "The server received a new request."
    }
]

# Route 1: Sensor Data (Refactored to English)
@app.get("/")
def read_sensores():
    return {
        "status": "operational",
        "cpu_temp": "45C",
        "fan_speed": "1200 RPM",
        "message": "Server is running perfectly."
    }

# Route 2: English Practice Endpoint 
@app.get("/word")
def get_random_word():
    return random.choice(tech_vocabulary)