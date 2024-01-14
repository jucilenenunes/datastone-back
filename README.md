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

# Como rodar a aplicação
 - Executar o comando: `python main.py`
 - Acessar a URL: http://127.0.0.1:8181
 - Usando FastAPI já em habilitada a documentação da API com Swagger nessa URL: http://127.0.0.1:8181/docs

# Referências utilizadas
 - Videos de API Python com FastAPI: 
   + [FastAPI](https://www.youtube.com/watch?v=9vRpj0RbkBg)
   + [FastAPI+MongoDB](https://www.youtube.com/watch?)v=QkGqjPFIGCA
   + [Conectar Python no banco MongoDB](https://community.revelo.com.br/como-acessar-o-mongodb-e-gerenciar-dados-com-python/)

# Considerações finais
 - Esse foi meu primeiro contato com Python eu não posso afirmar que entendi tudo que fiz, mas posso afirmar que foi um processo prazeroso e que a partir de agora eu tenho certeza que quero também aprender Python e me desenvolver, eu usei os vídeos acima e pesquisas na internet como referencia.
 - Para ter certeza do funcionamento de toda a API eu criei e alimentei uma collection no meu Postman, depois exportei essa collection e inclui na raiz deste repositório o nome do arquivo é "datastone-by-jucilene.postman_collection.json" para que possam importar e testar também.

 # Agradecimentos
 Muito obrigado pela oportunidade de demonstrar meus conhecimentos e de me desevoler. Gratidão!!