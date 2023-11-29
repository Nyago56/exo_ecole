# model.py
from peewee import *

class Artiste(Model):
    nom = CharField(max_length=150)
    prenom = CharField(max_length=150, null=True)
    email = CharField(100)
    id_adresse = IntegerField()
    id_instrument = IntegerField(null=True)
    id_orchestre = IntegerField(null=True)

    class Meta:
        table_name = 'artiste'
