from bson import ObjectId
from schemas.cliente import cliente, clientes
from services.db import get_collection

def getClientes():
    resultado = clientes(get_collection("clientes").find())
    return resultado

def getCliente(id: str):
    resultado = cliente(get_collection("clientes").find_one({
            "_id": ObjectId(id)
        }))
    return resultado