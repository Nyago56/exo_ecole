import mysql.connector

print("Connexion à la base de données")

# Remplacez les valeurs suivantes par les informations spécifiques à votre configuration
host = '172.19.0.1'
user = 'root'
password = 'uimm'
database = 'data_indus'

# Créez la connexion
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Créez un curseur
cursor = mydb.cursor()

# Exécutez une requête SQL pour récupérer des données (dans cet exemple, on récupère les noms des tables)
cursor.execute("SHOW TABLES")

# Récupérez toutes les lignes résultantes
tables = cursor.fetchall()

# Affichez les résultats
for table in tables:
    print(table)

# Fermez le curseur et la connexion
cursor.close()
mydb.close()
