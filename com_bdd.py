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

# Exécutez une requête SQL pour récupérer des données de chaque table
tables = ['adresse', 'camera', 'controle_fuite', 'equipement_industriel', 'langue',
          'mission', 'numero_mission', 'resident', 'scan_code_barre', 'site', 'utilisateur', 'utilise']

for table in tables:
    print(f"\nContenu de la table '{table}':")

    # Exécutez une requête SQL pour récupérer tous les éléments de la table
    cursor.execute(f"SELECT * FROM {table}")

    # Récupérez toutes les lignes résultantes
    rows = cursor.fetchall()

    # Affichez les résultats
    for row in rows:
        print(row)

# Fermez le curseur et la connexion
cursor.close()
mydb.close()
