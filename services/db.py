from pymongo.mongo_client import MongoClient

uri = "mongodb://root:jupass@localhost:27017/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.datastone

try:
    client.admin.command('ping')
    print("Estou conectada no BD by Ju! ;-*");
except Exception as e:
    print(e)