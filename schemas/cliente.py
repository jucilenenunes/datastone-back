def cliente(cliente):
    return {
        "id": str(cliente["_id"]),
        "nome": cliente["nome"],
        "documento": cliente["documento"],
        "telefone": cliente["telefone"],
        "email": cliente["email"],
        "ativo": bool(cliente["ativo"]),
        "produtos": cliente["produtos"]
    }

def clientes(clientes) -> list:
    return [cliente(c) for c in clientes]