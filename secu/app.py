from flask import Flask, render_template, request, jsonify
from setting import DB_HOST, DB_DATABASE, DB_PASSWORD, DB_USER
from model import Artiste
from peewee import CharField, Model, MySQLDatabase

app = Flask(__name__)

db = MySQLDatabase(DB_DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=3306)

class Utilisateur(Model):
    Nom_utilisateur = CharField(max_length=255)
    mdp = CharField(max_length=255)
    NivPermission = CharField(max_length=255)

    class Meta:
        database = db
        table_name = 'utilisateur'

def get_user_data():
    # Utilisez Peewee pour exécuter la requête SELECT
    users = Utilisateur.select()
    user_data = [(user.Nom_utilisateur, user.mdp, user.NivPermission) for user in users]
    return user_data

def create_user(username, password, permission):
    # Utilisez Peewee pour créer un nouvel utilisateur
    Utilisateur.create(Nom_utilisateur=username, mdp=password, NivPermission=permission)

@app.route('/artiste/ajout')
def ajout_artiste():
    nom = "Simon"
    prenom = "Leo"
    email = "Simon@leo.com"

    # Utilisez Peewee pour créer un nouvel artiste
    artiste = Artiste.create(nom=nom, prenom=prenom, email=email)

@app.route('/create_user', methods=['POST'])
def handle_create_user():
    data = request.get_json()
    create_user(data['username'], data['password'], data['permission'])
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
