import pymongo
import os

mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
con_string = f"""mongodb+srv://{mongo_user}:{mongo_password}@ \
clustertestemongo.obyb15n.mongodb.net/? \
retryWrites=true&w=majority"""
print(con_string)
client = pymongo.MongoClient(con_string)
db = client.python_dio_mongo
collection = db.bank
cliente = {
    "nome": "Luana",
    "cpf": "222910",
    "endereco": "Rua da Saúde",
    "conta": {
        "tipo": "Corrente",
        "agencia": "0001",
        "num": "4"
    }
}

cliente = collection.insert_one(cliente)
print(cliente.inserted_id)
