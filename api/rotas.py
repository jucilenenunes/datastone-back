import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getTeste():
    return "Olá Ju!"

uvicorn.run(app, port=8181)