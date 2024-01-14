from pymongo.mongo_client import MongoClient

uri = "mongodb://root:jupass@localhost:27017/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.datastone

def get_collection(collection_name):
    return db[collection_name]