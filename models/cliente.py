from pydantic import BaseModel, Field
from typing import List

class Cliente(BaseModel):
    id: str = Field(default=None)
    nome: str
    documento: str
    telefone: str
    email: str
    ativo: bool
    produtos: List[int]