from services.db import get_collection

def postProduto(novo_produto):
    resultado = get_collection("produtos").insert_one(novo_produto)
    return str(resultado.inserted_id)