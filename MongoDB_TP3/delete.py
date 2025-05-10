from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority")
db = client.bank
accounts_collection = db.accounts

# 1
result = accounts_collection.delete_one({ "_id": ObjectId("62d6e04ecab6d8e130497485") })

print(f"{result.deleted_count} document supprimé.")

# 2
filter_low_balance = { "balance": { "$lt": 500 } }

result = accounts_collection.delete_many(filter_low_balance)

print(f"{result.deleted_count} comptes supprimés avec un solde < 500 $.")
