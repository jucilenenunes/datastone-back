from bson import ObjectId
from pymongo import ReturnDocument
from models.produto import Produto
from schemas.produto import produto
from services.db import get_collection

def putProduto(id: str, produto_alterado: Produto):
    resultado = get_collection("produtos").find_one_and_update(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": dict(produto_alterado)
        },
        return_document = ReturnDocument.AFTER
    )
    return produto(resultado)