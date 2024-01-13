from pydantic import BaseModel, Field

class Produto(BaseModel):
    id: str = Field(default=None)
    nome: str
    ativo: bool