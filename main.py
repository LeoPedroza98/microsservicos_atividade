import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List

from . import atividade

app = FastAPI()


class Create_atividade(BaseModel):
    disciplina_id: int
    prazo:str
    enunciado:str
    resposta:str
    dataSubmissao:datetime.date
    nota:str
    
class Post_atividade_concluida(BaseModel):
    atividade_id:int
    disciplina_id: int


@app.get('/')
async def index():

    return {"Real": "Python"}


@app.post("/atividade", response_model=atividade.Atividade)
async def create_atividade(atividade_req: Create_atividade):
    atividades = atividade.create_atividade(**atividade_req.dict())

    return atividades

@app.get("/atividade/{atividade_id}", response_model=atividade.Atividade)
async def get_atividade(atividade_id: str):
    print(atividade.ATIVIDADE)
    atividades = atividade.get_atividade(atividade_id=atividade_id)

    if atividades is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return atividades

@app.post("/atividade/{atividade_id}", response_model=atividade.Atividade)
async def post_atividade_concluida(atividade_req: Post_atividade_concluida):
    atividades = atividade.submissão_atividade(**atividade_req.dict())
    
    return atividades
    