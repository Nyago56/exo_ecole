import mysql.connector

#=============================================================================================================

class IF_bdd:

#-------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.mydb = None
        self.cursor = None

#-------------------------------------------------------------------------------------------------------------

    def __del__(self):
        if self.mydb is not None:
            self.mydb.close()
            print("IF_BDD : Fermeture bdd")

#-------------------------------------------------------------------------------------------------------------

    def connect(self, adrs, user, mdp, bdd_name):
        try:
            self.mydb = mysql.connector.connect(
                host=adrs,
                user=user,
                password=mdp,
                database=bdd_name
            )
        except Exception as Exc:
            print(repr(Exc))

        if self.mydb is not None:
            self.cursor = self.mydb.cursor()
            return True
        else:
            return False
        
#-------------------------------------------------------------------------------------------------------------

    def get_data_from_table(self, table):
        if self.mydb is not None:
            # Execute a query to get the column names
            self.cursor.execute(f"DESCRIBE {table}")
            columns = [column[0] for column in self.cursor.fetchall()]

            # Execute a query to get the data from the table
            self.cursor.execute(f"SELECT * FROM {table}")
            rows = self.cursor.fetchall()

            return columns, rows
        else:
            return [], []
    
#-------------------------------------------------------------------------------------------------------------

    def verify_user_credentials(self, username, password):
        if self.mydb is not None:
            query = "SELECT * FROM utilisateur WHERE nom_utilisateur = %s AND mdp = %s"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            return result is not None
        else:
            return False
        
#-------------------------------------------------------------------------------------------------------------

    def get_data_from_donnee(self):
        if self.mydb is not None:
            self.cursor.execute("SELECT Valeur FROM Donnee")
            data = self.cursor.fetchall()
            valeurs = [int(row[0]) for row in data]
            return valeurs
        else:
            return []
        
#-------------------------------------------------------------------------------------------------------------
#=============================================================================================================

if __name__ == "__main__":
    bdd_instance = IF_bdd()
    if bdd_instance.connect('172.19.0.1', 'root', 'uimm', 'data_indus'):
        columns, data_from_table = bdd_instance.get_data_from_table('utilisateur')
        tere = bdd_instance.verify_user_credentials('user1', 'pass1')
        print("Columns:", columns)
        print("Data:", data_from_table)
        print("truc dans var : ",tere)
    else:
        print("Erreur de connexion à la base de données.")
