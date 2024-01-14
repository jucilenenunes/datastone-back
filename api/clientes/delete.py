from bson import ObjectId
from services.db import get_collection

def deleteCliente(id: str):
    resultado = get_collection("clientes").delete_one(
        {
            "_id": ObjectId(id)
        }
    )
    return resultado.deleted_count