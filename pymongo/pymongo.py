import pymongo
import os
import pprint

mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
con_string = f"""mongodb+srv://{mongo_user}:{mongo_password}@ \
clustertestemongo.obyb15n.mongodb.net/? \
retryWrites=true&w=majority"""
print(con_string)
client = pymongo.MongoClient(con_string)
db = client.python_dio_mongo
collection = db.bank
# collection.delete_many({}) - deletando todos os documentos
clientes = [
    {
        "nome": "João",
        "cpf": "333985",
        "endereco": "Rua da Paz",
        "conta": {
            "tipo": "Corrente",
            "agencia": "0001",
            "num": "2"
        }
    },
    {
        "nome": "Camila",
        "cpf": "117723",
        "endereco": "Rua da Amizade",
        "conta": {
            "tipo": "Corrente",
            "agencia": "0001",
            "num": "9"
        }
    },
    {
        "nome": "Gabriel",
        "cpf": "717173",
        "endereco": "Rua da Oportunidade",
        "conta": {
            "tipo": "Corrente",
            "agencia": "0001",
            "num": "15"
        }
    },
]

cliente = collection.insert_many(clientes)

print("### TODOS OS CLIENTES ###")
for cliente in collection.find():
    pprint.pprint(cliente)

print("### APENAS O CLIENTE DE NOME GABRIEL ###")
for cliente in collection.find({"nome": "Gabriel"}):
    pprint.pprint(cliente)
