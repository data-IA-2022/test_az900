from flask import Flask, jsonify
import psycopg2

# Configuration de la base de données
db_host = 'departementbdd.postgres.database.azure.com'
db_name = 'postgres'
db_user = 'BDDadmin'
db_password = 'pass987456321;,'
db_table = 'departement'

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définit une route pour le point d'API /test
@app.route('/test')
def test():
    # Établir une connexion à la base de données
    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()

    # Exécuter la requête pour récupérer les éléments de la table
    cursor.execute(f'SELECT * FROM {db_table}')
    results = cursor.fetchall()
    #print (results)

    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()

    # Convertir les résultats en une liste de dictionnaires
    data = []
    for result in results:
        #print(result[:3])
        dept, insee, cheflieu = result[:3]
        data.append({
            'DEPT': dept,
            'INSEE': insee,
            'CHEFLIEU': cheflieu
        })

    # Renvoyer les données en tant que réponse JSON
    return jsonify(data)

# Point d'entrée principal de l'application
if __name__ == '__main__':
    app.run()
