import mysql.connector
mydb = None
tables = None
cursor = None
#=======================================================================================================================
def init():
    global mydb
    global tables
    global cursor
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
#-----------------------------------------------------------------------------------------------------------------------
def gettable(table):
        
    print(f"\nContenu de la table '{table}':")
    # Exécutez une requête SQL pour récupérer tous les éléments de la table
    cursor.execute(f"SELECT * FROM {table}")
    # Récupérez toutes les lignes résultantes
    rows = cursor.fetchall()
    # Affichez les résultats
    for row in rows:
        print(row)
#-----------------------------------------------------------------------------------------------------------------------
def gettables():
    for table in tables:
        gettable(table)
#-----------------------------------------------------------------------------------------------------------------------
def close():
    # Fermez le curseur et la connexion
    cursor.close()
    mydb.close()
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

if __name__=="__main__":
    #init()
    #gettables()
    #gettable('mission')
    #close()

    bdd = IF_bdd()

    #demande à l'utilisateur de rentrer un nom d'utilisateur
    user_name = input("Entrez votre nom d'utilisateur : ")

    #demande à l'utilisateur de rentrer un mdp
    password = input("Veuillez entrer votre mdp : ")
    
    #vérification que les codes rentrés sont bon
    if bdd.connect('172.19.0.1',user_name,password,'data_indus'): 
       bdd.gettable('site')