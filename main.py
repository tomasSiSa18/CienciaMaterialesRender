import json
import random
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Cargar preguntas desde el archivo JSON
with open("P1Questions.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    questionsP1 = data["questions"]
    
# Modelo de respuesta para una pregunta
class QuestionResponse(BaseModel):
    code: int
    msg: str
    data: dict
    request_id: str
    
# Generar un ID aleatorio (simulación de request_id)
def generate_request_id():
    return str(random.randint(1000000000, 9999999999))

# Endpoint para obtener una pregunta aleatoria de la parte 1
@app.get("/api/randomquestionP1", response_model=QuestionResponse)
def get_random_questionP1():
    question = random.choice(questionsP1)

    response = {
        "code": 200,
        "msg": "Pregunta obtenida con éxito",
        "data": {
            "context": question["context"],
            "question": question["question"]
        },
        "request_id": generate_request_id()
    }

    return response