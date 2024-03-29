import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.produtos.get import getProdutos, getProduto
from api.clientes.get import getClientes, getCliente
from api.produtos.post import postProduto
from api.clientes.post import postCliente
from api.produtos.put import putProduto
from api.clientes.put import putCliente
from api.produtos.delete import deleteProduto
from api.clientes.delete import deleteCliente
from models.cliente import Cliente
from models.produto import Produto

app = FastAPI(
    title="DataStone API by Ju",
    summary="Está é a API desenvolvida por Jucilene Nunes da Silva para o teste de desenvolvimento da DatStone.",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/clientes")
def getClientesRoute():
    return getClientes()

@app.get("/clientes/{id}")
def getClienteRoute(id: str):
    return getCliente(id)

@app.post("/clientes")
def postClienteRoute(cliente: Cliente):
    return postCliente(dict(cliente))

@app.put("/clientes/{id}")
def putClienteRoute(id: str, cliente: Cliente):
    return putCliente(id, dict(cliente))

@app.delete("/clientes/{id}")
def putClienteRoute(id: str):
    return deleteCliente(id)

@app.get("/produtos")
def getProdutosRoute():
    return getProdutos()

@app.get("/produtos/{id}")
def getProdutoRoute(id: str):
    return getProduto(id)

@app.post("/produtos")
def getProdutoRoute(produto: Produto):
    return postProduto(dict(produto))

@app.put("/produtos/{id}")
def putProdutoRoute(id: str, produto: Produto):
    return putProduto(id, produto)

@app.delete("/produtos/{id}")
def putProdutoRoute(id: str):
    return deleteProduto(id)

def runApi():
    uvicorn.run(app, port=8181)