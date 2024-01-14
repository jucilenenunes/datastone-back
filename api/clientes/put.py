from bson import ObjectId
from pymongo import ReturnDocument
from models.cliente import Cliente
from schemas.cliente import cliente
from services.db import get_collection

def putCliente(id: str, cliente_alterado: Cliente):
    resultado = get_collection("clientes").find_one_and_update(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": dict(cliente_alterado)
        },
        return_document = ReturnDocument.AFTER
    )
    return cliente(resultado)