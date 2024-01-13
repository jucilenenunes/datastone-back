# datastone-back
Projeto iniciado com Python + FastAPI e base MongoDB na tentativa de conquistar uma oportunidade na DataStone, apesar de não ter conhecimento de Python tentarei construir uma API seguindo alguns videos que encontrei de referência e acredito ser possível.

## Ambiente de Desenvolvimento
 - Python 3.10 + Venv + FastAPI + Uvicorn
 - Docker + Docker Compose
 - MongoDB + MongoExpress

### Como subir o ambiente de desenvolvimento
 - Para subir o ambiente basta execuar o seguinte comando:
 `
 docker-compose up -d
 `
 - Assim que o console concluir a execução significa de que o ambiente está rodando, ai é só acessar o MongoExpress para manipularmos o MongoDB, neste link: http://localhost:8081/.
 - Crie um banco com nome "datastone" as collections (tabelas) serão criadas pela própria aplicação.

### Anotações sobre como preparar o ambiente Python
 - Instalar o "Virtual Environment" do Python: `python -m venv env `
 - Para ativar o "Virtual Environment" `.\env\Scripts\Activate.ps1`
 - Para instalar as dependências: `pip install fastapi uvicorn pymongo`

# Referências utilizadas
 - Video de API Python com FastAPI: https://www.youtube.com/watch?v=9vRpj0RbkBg
 - Conectar Python no banco MongoDB: https://community.revelo.com.br/como-acessar-o-mongodb-e-gerenciar-dados-com-python/