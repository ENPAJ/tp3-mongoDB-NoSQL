from pymongo import MongoClient

client = MongoClient("mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority")
db = client.bank
accounts_collection = db.accounts

# Mise à jour : ajout de 200 à tous les soldes
result = accounts_collection.update_many({}, {"$inc": {"balance": 200}})

print(f"{result.modified_count} comptes mis à jour avec +200 $")
#Ajout de 50 $ à tout le monde
select_accounts = { "account_type": "Checking" }

add_transfer = { "$push": { "transfers_complete": "TR413308000" }, "$inc": { "balance": 50 } }

result = accounts_collection.update_many(select_accounts, add_transfer)

print(f"{result.modified_count} comptes chèques mis à jour avec +50 $")

