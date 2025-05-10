import os

MONGO_URI = "mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net"


accounts_path = "accounts.bson"
transfers_path = "transfers.bson"

os.system(f'bsondump {accounts_path} --outFile accounts.json')
os.system(f'bsondump {transfers_path} --outFile transfers.json')

os.system(f'mongoimport --uri "{MONGO_URI}" --db bank --collection accounts --file {accounts_path} --type json')
os.system(f'mongoimport --uri "{MONGO_URI}" --db bank --collection transfers --file {transfers_path} --type json')
