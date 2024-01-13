import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="DataStone API by Ju",
    summary="Está é a API desenvolvida por Jucilene Nunes da Silva para o teste de desenvolvimento da DatStone.",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)

@app.get("/")
async def getTeste():
    return "Olá Ju!"

def runApi():
    uvicorn.run(app, port=8181)