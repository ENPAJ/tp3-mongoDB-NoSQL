from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint

# Connexion MongoDB
client = MongoClient("mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority")

# Base et collection
db = client.bank
accounts_collection = db.accounts

# Recherche par ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}
result = accounts_collection.find_one(document_to_find)

if result:
    pprint("Document trouvé :", result)
else:
    pprint("Aucun document trouvé avec cet ObjectId.")
