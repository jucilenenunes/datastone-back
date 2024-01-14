from bson import ObjectId
from services.db import get_collection

def deleteProduto(id: str):
    resultado = get_collection("produtos").delete_one(
        {
            "_id": ObjectId(id)
        }
    )
    return resultado.deleted_count