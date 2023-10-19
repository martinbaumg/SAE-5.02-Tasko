import database_connection
from requests_list import RequestList
import bcrypt

try:
    # Se connecter à la base de données
    db = database_connection.DatabaseConnection()
    db.connect()

    # Spécifier les informations de l'utilisateur
    username = "John"
    password = "password"

    # Créer une requête de vérification du mot de passe en utilisant la méthode check_password_match de RequestList
    query, values = RequestList.check_password_match(username)

    # Afficher la requête SQL générée pour déboguer
    print("Query:", query)

    # Exécuter la requête en utilisant la méthode execute_query de la base de données
    db.execute_query(query, values)

    # Extraire les données de la requête
    result = db.cursor.fetchone()

    # Vérifier si des données ont été extraites
    if result:
        stored_salt, stored_hashed_password = result
        hashed_input_password = bcrypt.hashpw(password.encode("utf-8"), stored_salt)

        if hashed_input_password.decode("utf-8") == stored_hashed_password:
            print("Mot de passe correct.")
        else:
            print("Mot de passe incorrect.")
    else:
        print("Mot de passe incorrect (pas de données extraites).")

    # Valider les modifications dans la base de données
    db.disconnect()

# Gérer les erreurs
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
