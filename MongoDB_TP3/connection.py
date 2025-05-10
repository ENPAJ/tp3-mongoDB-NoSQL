from pymongo import MongoClient


MONGODB_URI = "mongodb+srv://darky33:iSEx5thoR0fhV3BJ@cluster0.levridj.mongodb.net/?retryWrites=true&w=majority"

# Création du client MongoDB
client = MongoClient(MONGODB_URI)

# Vérification de la connexion
try:
    # La commande 'ping' vérifie si le serveur est accessible
    client.admin.command("ping")
    print("Connexion à MongoDB réussie !")
    databases = client.list_database_names()
    #print(databases)
    for db_name in databases:
        print("-", db_name)
except Exception as e:
    print("Erreur de connexion :", e)
