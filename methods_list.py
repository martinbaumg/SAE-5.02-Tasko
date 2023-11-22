import stat
from requests_list import RequestList
import bcrypt
from database_connection import DatabaseConnection

class MethodList:
    def __init__(self): # We create an instance of the class DatabaseConnection
        self.db = DatabaseConnection()

    # GETTER
    def get_user(self, username): # We create a method get_user
        query = RequestList.get_user(username)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    def get_task(self, task_id): # We create a method get_task
        query = RequestList.get_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune tâche trouvée ou une erreur s'est produite.")

    def get_all_tasks(self): # We create a method get_all_tasks
        query = RequestList.get_all_tasks()
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune tâche trouvée ou une erreur s'est produite.")

    def get_task_name(self, task_name): # We create a method get_task_name
        query = RequestList.get_task_name(task_name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune tâche trouvée ou une erreur s'est produite.")

    def get_subtasks(self, subtask_id): # We create a method get_subtasks
        query = RequestList.get_subtasks(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune sous-tâche trouvée ou une erreur s'est produite.")

    def get_subtask_name(self, subtask_name): # We create a method get_subtask_name
        query = RequestList.get_subtask_name(subtask_name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune sous-tâche trouvée ou une erreur s'est produite.")

    def get_flag(self, flag_id): # We create a method get_flag
        query = RequestList.get_flag(flag_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun flag trouvé ou une erreur s'est produite.")

    def get_priority(self, priority_id): # We create a method get_priority
        query = RequestList.get_priority(priority_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune priorité trouvée ou une erreur s'est produite.")

    def get_state(self, state_id): # We create a method get_state
        query = RequestList.get_state(state_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun état trouvé ou une erreur s'est produite.")

    def get_task_due_date(self, task_id): # We create a method get_task_due_date
        query = RequestList.get_task_due_date(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune date limite trouvée ou une erreur s'est produite.")

    def get_subtask_due_date(self, subtask_id): # We create a method get_subtask_due_date
        query = RequestList.get_subtask_due_date(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune date limite trouvée ou une erreur s'est produite.")
    
    def get_project(self, project_id): # We create a method get_project
        query = RequestList.get_project(project_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun projet trouvé ou une erreur s'est produite.")

    def get_user_project(self, user_id): # We create a method get_user_project
        query = RequestList.get_user_project(user_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun projet trouvé ou une erreur s'est produite.")

    def get_project_task(self, project_id): # We create a method get_project_task
        query = RequestList.get_project_task(project_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    #SETTER
    def add_user(self, mail, password, name, rights_id):
        query = RequestList.add_user(mail, password, name, rights_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur ajouté avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de l'utilisateur.")

    def add_task(self, name, description, priority_id, state_id, due_date, project_id):
        query = RequestList.add_task(name, description, priority_id, state_id, due_date, project_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Une erreur s'est produite lors de l'ajout de la tâche.")

    def add_subtask(self, name, description, state_id, flag_id, user_id, priority_id, due_date):
        query = RequestList.add_subtask(name, description, state_id, flag_id, user_id, priority_id, due_date)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Une erreur s'est produite lors de l'ajout de la sous-tâche.")

    def add_priority(self, name):
        query = RequestList.add_priority(name)
        result = self.db.execute_query(query)
        if result is not None:
            print("Priorité ajoutée avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de la priorité.")

    def add_state(self, name):
        query = RequestList.add_state(name)
        result = self.db.execute_query(query)
        if result is not None:
            print("État ajouté avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de l'état.")

    def add_user_to_task(self, user_id, task_id):
        query = RequestList.add_user_to_task(user_id, task_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur ajouté avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de l'utilisateur.")

    def add_user_to_subtask(self, user_id, subtask_id):
        query = RequestList.add_user_to_subtask(user_id, subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur ajouté avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de l'utilisateur.")

    def add_subtask_to_task(self, subtask_id, task_id):
        query = RequestList.add_subtask_to_task(subtask_id, task_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Sous-tâche ajoutée avec succès.")
        else:
            print("Une erreur s'est produite lors de l'ajout de la sous-tâche.")

    #UPDATER
    def update_user(self, user_id, mail, password, name, rights_id):
        query = RequestList.update_user(user_id, mail, password, name, rights_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de l'utilisateur.")

    def update_project(self, project_id, name, description, user_id):
        query = RequestList.update_project(project_id, name, description)
        result = self.db.execute_query(query)
        if result is not None:
            print("Projet modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification du projet.")

    def update_task(self, task_id, name, description, priority_id, flag_id, user_id, state_id):
        query = RequestList.update_task(task_id, name, description, priority_id, flag_id, user_id, state_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Tâche modifiée avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de la tâche.")

    def update_subtask(self, subtask_id, name, description, priority_id, flag_id, user_id, state_id):
        query = RequestList.update_subtask(subtask_id, name, description, priority_id, flag_id, user_id, state_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Sous-tâche modifiée avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de la sous-tâche.")

    def update_flag(self, flag_id, name, color):
        query = RequestList.update_flag(flag_id, name, color)
        result = self.db.execute_query(query)
        if result is not None:
            print("Flag modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification du flag.")

    def update_priority(self, priority_id, name):
        query = RequestList.update_priority(priority_id, name)
        result = self.db.execute_query(query)
        if result is not None:
            print("Priorité modifiée avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de la priorité.")

    def update_state(self, state_id, name):
        query = RequestList.update_state(state_id, name)
        result = self.db.execute_query(query)
        if result is not None:
            print("État modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de l'état.")

    def update_date_task(self, task_id, due_date):
        query = RequestList.update_date_task(task_id, due_date)
        result = self.db.execute_query(query)
        if result is not None:
            print("Date modifiée avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de la date.")
    
    def update_date_subtask(self, subtask_id, due_date):
        query = RequestList.update_date_subtask(subtask_id, due_date)
        result = self.db.execute_query(query)
        if result is not None:
            print("Date modifiée avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de la date.")

    def update_user_to_task(self, user_id, task_id):
        query = RequestList.update_user_to_task(user_id, task_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de l'utilisateur.")

    def update_user_to_subtask(self, user_id, subtask_id):
        query = RequestList.update_user_to_subtask(user_id, subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur modifié avec succès.")
        else:
            print("Une erreur s'est produite lors de la modification de l'utilisateur.")

    #DELETER
    def delete_user(self, user_id):
        query = RequestList.delete_user(user_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Utilisateur supprimé avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression de l'utilisateur.")

    def delete_task(self, task_id):
        query = RequestList.delete_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Tâche supprimée avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression de la tâche.")

    def delete_subtask(self, subtask_id):
        query = RequestList.delete_subtask(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Sous-tâche supprimée avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression de la sous-tâche.")

    def delete_flag(self, flag_id):
        query = RequestList.delete_flag(flag_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Flag supprimé avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression du flag.")

    def delete_priority(self, priority_id):
        query = RequestList.delete_priority(priority_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("Priorité supprimée avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression de la priorité.")

    def delete_state(self, state_id):
        query = RequestList.delete_state(state_id)
        result = self.db.execute_query(query)
        if result is not None:
            print("État supprimé avec succès.")
        else:
            print("Une erreur s'est produite lors de la suppression de l'état.")

    #REQUESTS

    def get_user_in_task(self, task_id):
        query = RequestList.get_user_in_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    def get_user_in_subtask(self, subtask_id):
        query = RequestList.get_user_in_subtask(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    def get_subtask_in_task(self, task_id):
        query = RequestList.get_subtask_in_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
            print("Aucune sous-tâche trouvée ou une erreur s'est produite.")

    def get_priority_in_task(self, task_id):
        query = RequestList.get_priority_in_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucune priorité trouvée ou une erreur s'est produite.")

    def get_flag_in_task(self, task_id):
        query = RequestList.get_flag_in_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucun flag trouvé ou une erreur s'est produite.")

    def get_state_in_task(self, task_id):
        query = RequestList.get_state_in_task(task_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucun état trouvé ou une erreur s'est produite.")

    def get_priority_in_subtask(self, subtask_id):
        query = RequestList.get_priority_in_subtask(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucune priorité trouvée ou une erreur s'est produite.")

    def get_flag_in_subtask(self, subtask_id):
        query = RequestList.get_flag_in_subtask(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucun flag trouvé ou une erreur s'est produite.")

    def get_state_in_subtask(self, subtask_id):
        query = RequestList.get_state_in_subtask(subtask_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
        else:
                print("Aucun état trouvé ou une erreur s'est produite.")

    def get_task_in_project(self, project_id):
        query = RequestList.get_task_in_project(project_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    def get_user_in_project(self, project_id):
        query = RequestList.get_user_in_project(project_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    def check_password_secure(self, mail, user_password):
        query = "SELECT password FROM `USER` WHERE mail = %s"
        values = (mail,)

        print(f"Executing query: {query} with values {values}")

        result = self.db.execute_query(query, values)

        if result:
            hashed_password = result[0][0]  # Get the hashed password from the result
            if bcrypt.checkpw(user_password.encode(), hashed_password.encode()):
                print("Le mot de passe est correct.")
            else:
                print("Le mot de passe est incorrect.")
        else:
            print("Aucun utilisateur trouvé avec cet e-mail.")

    #SEARCH
    def search_user(self, name):
        query = RequestList.search_user(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun utilisateur trouvé ou une erreur s'est produite.")

    def search_task(self, name):
        query = RequestList.search_task(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    def search_subtask(self, name):
        query = RequestList.search_subtask(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune sous-tâche trouvée ou une erreur s'est produite.")

    def search_flag(self, name):
        query = RequestList.search_flag(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun flag trouvé ou une erreur s'est produite.")

    def search_priority(self, name):
        query = RequestList.search_priority(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune priorité trouvée ou une erreur s'est produite.")

    def search_state(self, name):
        query = RequestList.search_state(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun état trouvé ou une erreur s'est produite.")

    def search_project(self, name):
        query = RequestList.search_project(name)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun projet trouvé ou une erreur s'est produite.")

    def search_task_by_name_and_state(self, task_name, state_id):
        query = RequestList.search_task_by_name_and_state(task_name, state_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    def serch_task_by_priority_and_user(self, priority_id, user_id):
        query = RequestList.serch_task_by_priority_and_user(priority_id, user_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    def search_task_by_flag_and_due_date(self, flag_id, due_date):
        query = RequestList.search_task_by_flag_and_due_date(flag_id, due_date)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune tâche trouvée ou une erreur s'est produite.")

    def search_subtask_by_name_and_user(self, subtask_name, user_id):
        query = RequestList.search_subtask_by_name_and_user(subtask_name, user_id)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucune sous-tâche trouvée ou une erreur s'est produite.")

    def search_project_by_name_and_description(self, project_name, project_description):
        query = RequestList.search_project_by_name_and_description(project_name, project_description)
        result = self.db.execute_query(query)
        if result is not None:
            for row in result:
                print(row)
            else:
                print("Aucun projet trouvé ou une erreur s'est produite.")