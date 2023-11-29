import pymysql
from flask import Flask, render_template, request, jsonify
from setting import DB_HOST, DB_DATABASE, DB_PASSWORD, DB_USER

app = Flask(__name__)

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_DATABASE,
}

def get_user_data():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Utilisateur")
    user_data = cursor.fetchall()
    connection.close()
    return user_data

def create_user(username, password, permission):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Utilisateur (Nom_utilisateur, mdp, NivPermission) VALUES (%s, %s, %s)", (username, password, permission))
    connection.commit()
    connection.close()

@app.route('/')
def display_user_table():
    user_data = get_user_data()
    return render_template('page.html', user_data=user_data)

@app.route('/create_user', methods=['POST'])
def handle_create_user():
    data = request.get_json()
    create_user(data['username'], data['password'], data['permission'])
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
