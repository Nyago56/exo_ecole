from app.ServWeb import app
from flask import render_template
from app.Bdd.bdd_recup import IF_bdd

@app.route('/afficher_donnees')
def afficher_donnees():
    bdd_instance = IF_bdd()
    if bdd_instance.connect('172.19.0.1', 'votre_utilisateur', 'votre_mot_de_passe', 'votre_base_de_donnees'):
        data_from_table = bdd_instance.get_data_from_table('votre_table')
        return render_template('afficher_donnees.html', data=data_from_table)
    else:
        return "Erreur de connexion à la base de données."
@app.route('/') #decorators
@app.route('/index')
def index():
    strResult = 'Hello Bruz'
    return strResult