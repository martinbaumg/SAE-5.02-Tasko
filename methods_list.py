import stat
from requests_list import RequestList
import bcrypt
from database_connection import DatabaseConnection

class MethodList:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_user(self, username):
        query = RequestList.get_user(username)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    # Méthode pour ajouter un utilisateur de manière sécurisée
    def add_user_secure(self, mail, password, name, rights_id):
        # Obtenez la requête et les valeurs à partir de RequestList
        query, values = RequestList.add_user_secure(mail, password, name, rights_id)
        # Exécutez la requête en utilisant l'objet de connexion à la base de données
        self.db.execute_query(query, values)

    # Méthode pour obtenir toutes les tâches
    def get_all_tasks(self):
        query = RequestList.get_all_tasks()
        result = self.db.execute_query(query)
        for row in result:
            print(row)

    # Continuez à ajouter d'autres méthodes de cette manière...
