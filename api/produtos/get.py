from schemas.produto import produtos
from services.db import get_collection

def getProdutos():
    resultado = produtos(get_collection("produtos").find())
    return resultado