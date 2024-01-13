from bson import ObjectId
from schemas.produto import produto, produtos
from services.db import get_collection

def getProdutos():
    resultado = produtos(get_collection("produtos").find())
    return resultado

def getProduto(id: str):
    resultado = produto(get_collection("produtos").find_one({
            "_id": ObjectId(id)
        }))
    return resultado