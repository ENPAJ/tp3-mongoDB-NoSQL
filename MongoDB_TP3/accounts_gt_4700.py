from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority")

db = client.bank
accounts_collection = db.accounts

documents_to_find = {"balance": {"$gt": 4700}}
cursor = accounts_collection.find(documents_to_find)

found = False
for doc in cursor:
   pprint(doc)
found = True

if not found:
    print("Aucun compte trouvé avec un solde supérieur à 4700 $.")
