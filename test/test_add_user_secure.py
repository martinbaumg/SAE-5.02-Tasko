import database_connection
from requests_list import RequestList

try:
    # Se connecter à la base de données
    db = database_connection.DatabaseConnection()
    db.connect()

    # Spécifier les informations de l'utilisateur
    mail = "testcheck@example.com"
    password = "password123"
    name = "TestCheck"
    rights_id = 1  # Remplacez par le véritable rights_id

    # Créer une requête d'ajout d'utilisateur en utilisant la méthode add_user_secure de RequestList
    query, values = RequestList.add_user_secure(mail, password, name, rights_id)

    # Afficher la requête SQL générée pour déboguer
    print("Query:", query)

    # Exécuter la requête en utilisant la méthode execute_query de la base de données
    db.execute_query(query, values)

    # Valider les modifications dans la base de données
    db.connection.commit()

    # Déconnecter de la base de données
    db.disconnect()

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
