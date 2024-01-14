from pydantic import BaseModel, Field
from typing import List, Optional

class Cliente(BaseModel):
    id: str = Field(default=None)
    nome: str
    documento: str
    telefone: str
    email: str
    ativo: bool
    produtos: Optional[List[int]] = []