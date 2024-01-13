import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.produto import Produto

app = FastAPI(
    title="DataStone API by Ju",
    summary="Está é a API desenvolvida por Jucilene Nunes da Silva para o teste de desenvolvimento da DatStone.",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)

origins = [
    "http://localhost:8080",
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
    return { "teste": "Ok"}

@app.get("/clientes/{ìd}")
def getClienteRoute(id: str):
    return { "teste": "Ok"}

@app.post("/clientes")
def postClienteRoute():
    return { "teste": "Ok"}

@app.put("/clientes/{id}")
def putClienteRoute(id: str):
    return { "teste": "Ok"}

@app.delete("/clientes/{id}")
def putClienteRoute(id: str):
    return { "teste": "Ok"}

@app.get("/produtos")
def getProdutosRoute():
    return { "teste": "Ok"}

@app.get("/produtos/{id}")
def getProdutoRoute(id: str):
    return { "teste": "Ok"}

@app.post("/produtos")
def getProdutoRoute(produto: Produto):
    return { "teste": "Ok"}

@app.put("/produtos/{id}")
def putProdutoRoute(id: str, produto: Produto):
    return { "teste": "Ok"}

@app.delete("/produtos/{id}")
def putProdutoRoute(id: str):
    return { "teste": "Ok"}

def runApi():
    uvicorn.run(app, port=8181)