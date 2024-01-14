from services.db import get_collection

def postCliente(novo_cliente):
    resultado = get_collection("clientes").insert_one(novo_cliente)
    return str(resultado.inserted_id)