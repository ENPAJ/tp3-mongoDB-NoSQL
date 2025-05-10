from pymongo import MongoClient
from datetime import datetime
from bson.decimal128 import Decimal128

# Connexion MongoDB
client = MongoClient("mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority")

# Callback générique
def callback(session, transfer_id=None, account_id_receiver=None, account_id_sender=None, transfer_amount=None):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": Decimal128(str(transfer_amount)),
        "timestamp": datetime.now()
    }

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {"$inc": {"balance": -transfer_amount}, "$push": {"transfers_complete": transfer_id}},
        session=session
    )

    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {"$inc": {"balance": transfer_amount}, "$push": {"transfers_complete": transfer_id}},
        session=session
    )

    transfers_collection.insert_one(transfer, session=session)
    print(f"Transaction {transfer_id} effectuée")


def transaction1(s):
    callback(
        s,
        transfer_id="TR100000001",
        account_id_sender="MDB123456789",
        account_id_receiver="MDB987654321",
        transfer_amount=250
    )


def transaction2(s):
    callback(
        s,
        transfer_id="TR100000002",
        account_id_sender="MDB111222333",
        account_id_receiver="MDB444555666",
        transfer_amount=400
    )

# Lancer les deux transactions
with client.start_session() as session:
    session.with_transaction(transaction1)

with client.start_session() as session:
    session.with_transaction(transaction2)

client.close()
