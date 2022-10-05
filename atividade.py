
import datetime
from enum import Enum
from typing import List

from uuid import UUID, uuid4

from pydantic import BaseModel

class Atividade(BaseModel):
    atividade_id: UUID
    disciplina_id: int
    prazo:str
    enunciado:str
    resposta:str
    dataSubmissao:datetime.date
    nota:str
    
    
ATIVIDADE = {}


def create_atividade(disciplina_id:int,prazo:str,enunciado:str,resposta:str,dataSubmissao:datetime.date,nota:str):
    atividade = Atividade(
        atividade_id= uuid4(),
        disciplina_id= disciplina_id,
        prazo=prazo,
        enunciado=enunciado,
        resposta=resposta,
        dataSubmissao=dataSubmissao,
        nota=nota
    )
    ATIVIDADE[str(atividade.atividade_id)] = atividade
    return atividade


def get_atividade(atividad_id: str):
    return ATIVIDADE.get(atividad_id)

def submissão_atividade(atividade_id :int ):
    atividadeConcluida = Atividade(
        atividade_id= atividade_id
    )
       
    ATIVIDADE[str(atividadeConcluida.atividade_id)] = atividadeConcluida
    return atividadeConcluida
