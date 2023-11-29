from app.ServWeb import app
from app.Bdd.bdd_recup import IF_bdd
from flask import render_template, request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def login():
    # Créez une nouvelle instance de IF_bdd pour chaque requête
    bdd_instance = IF_bdd()
    
    auth_result = None
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if bdd_instance.connect('172.19.0.1', 'root', 'uimm', 'data_indus'):
            if bdd_instance.verify_user_credentials(username, password):
                auth_result = "OK"
                return redirect(url_for('accueil'))
            else:
                error_message = "Nom d'utilisateur ou mot de passe incorrect."
        else:
            error_message = "Erreur de connexion à la base de données."

    return render_template('login.html', auth_result=auth_result, error_message=error_message)


# Ajoutez cette route pour la page d'accueil
@app.route('/accueil')
def accueil():
    return render_template('page_accueil.html')

# Ajoutez cette route pour la page de choix
@app.route('/choix')
def choix():
    return render_template('choix.html')

# Ajoutez cette route pour la page de graph
@app.route('/graph')
def graph():
    donnee_data = IF_bdd.get_data_from_donnee()
    return render_template('graph.html', data=donnee_data)

# Ajoutez cette route pour la page de connexion réussie
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    return render_template('Connxion_ok.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
