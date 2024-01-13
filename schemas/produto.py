def produto(produto):
    return {
        "id": str(produto["_id"]),
        "nome": produto["nome"],
        "ativo": bool(produto["ativo"])
    }

def produtos(produtos) -> list:
    return [produto(c) for c in produtos]