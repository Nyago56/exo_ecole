import mysql.connector
#=======================================================================================================================
class IF_bdd:
    "Classe object d'interface bdd sql"
    def __init__(self):

        self.mydb = None
        self.tables = None
        self.cursor = None

        print("IF_BDD : Connexion à la base de données")
        

         # Exécutez une requête SQL pour récupérer des données de chaque table
        self.tables = ['adresse', 'camera', 'controle_fuite', 'equipement_industriel', 'langue',
                'mission', 'numero_mission', 'resident', 'scan_code_barre', 'site', 'utilisateur', 'utilise']
    
    def __del__(self):
        if (self.mydb != None) :
            #self.cursor.close()
            self.mydb.close()
            print("IF_BDD : Fermeture bdd")
    def connect(self,adrs,user,mdp,bdd_name):
        try:
            # Créez la connexion
            self.mydb = mysql.connector.connect(
                host=adrs,
                user=user,
                password=mdp,
                database=bdd_name
            )

        except Exception as Exc:
            print(repr(Exc))
        if (self.mydb != None) :
            # Créez un curseur
            self.cursor = self.mydb.cursor()
            return True
        else :
            return False
        
    def gettable(self,table):
        if (self.mydb != None) :   
            print(f"\nContenu de la table '{table}':")

            # Exécutez une requête SQL pour récupérer tous les éléments de la table
            self.cursor.execute(f"SELECT * FROM {table}")

            # Récupérez toutes les lignes résultantes
            rows = self.cursor.fetchall()

            # Affichez les résultats
            for row in rows:
                print(row)
#=======================================================================================================================