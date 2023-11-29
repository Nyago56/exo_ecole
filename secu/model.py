from peewee import Model, AutoField, CharField, IntegerField

class Artiste(Model):
    id_artiste = AutoField()
    nom = CharField(max_length=150)
    prenom = CharField(max_length=150, null=True)
    email = CharField(max_length=100)  # Correction : fixer la longueur maximale du champ
    id_adresse = IntegerField()
    id_instrument = IntegerField(null=True)
    id_orchestre = IntegerField(null=True)  # Correction : "id_orchestra" -> "id_orchestre"

    class Meta:
        table_name = "artiste"

# Assurez-vous d'avoir une instance de MySQLDatabase appelée `db` quelque part, par exemple dans votre fichier app.py.
# db = MySQLDatabase(database='votre_base_de_donnees', user='votre_utilisateur', password='votre_mot_de_passe', host='votre_host', port=3306)
# Assurez-vous de l'importer correctement dans votre fichier app.py pour que la classe Artiste puisse l'utiliser.
