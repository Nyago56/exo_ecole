from app.ServWeb import app
from app.Bdd.bdd_recup import IF_bdd
from flask import render_template, request, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Traitez ici le formulaire de connexion
        # Vous pouvez accéder aux données du formulaire avec request.form
        username = request.form.get('username')
        password = request.form.get('password')

        # Ajoutez ici la logique de vérification des identifiants, par exemple en utilisant votre base de données

        # Redirigez l'utilisateur vers une autre page après la connexion réussie
        return redirect(url_for('connexion'))

    return render_template('login.html')

# Ajoutez cette route pour la page d'accueil
@app.route('/')
def accueil():
    return render_template('page_accueil.html')
# Ajoutez cette route pour la page d'accueil
@app.route('/connexion')
def connexion():
    return render_template('Connxion_ok.html')