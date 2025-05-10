from pymongo import MongoClient
from datetime import datetime, timezone

MONGODB_URI = "mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)

db = client.bank
account_collection = db.accounts

new_document = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.now(timezone.utc),
}

result = account_collection.insert_one(new_document)
document_id = result.inserted_id
print("_id of inserted document: {document_id}")

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    }
]

result = account_collection.insert_many(new_accounts)
document_ids = result.inserted_ids
print("# of  documents inserted: " + str(len(document_ids)))
print("_id of inserted document: {document_ids}")
