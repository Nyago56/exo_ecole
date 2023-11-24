from app.ServWeb import app
from flask import render_template
from app.Bdd.bdd_recup import IF_bdd

#--------------------------------------------------------------------------------------------------

@app.route('/afficher_donnees')
def afficher_donnees():
    bdd_instance = IF_bdd()
    if bdd_instance.connect('172.19.0.1', 'root', 'uimm', 'data_indus'):
        columns, data_from_table = bdd_instance.get_data_from_table('mission')
        return render_template('mission.html', columns=columns, data=data_from_table)
    else:
        return "Erreur de connexion à la base de données."

#--------------------------------------------------------------------------------------------------

@app.route('/') #decorators
def accueil():
    return render_template('page_accueil.html')

#--------------------------------------------------------------------------------------------------

@app.route('/login')
def index():
     return render_template('login.html')