import bcrypt
from database_connection import DatabaseConnection

# this file contains the list of requests that are sent to the server
# they are stored as objects


class RequestList:
    # GETTER
    # The getter are used to get an element from the database
    @staticmethod
    def get_user(username):  # We define a method to get a user
        return f"SELECT * FROM USER WHERE name = '{username}'"

    @staticmethod
    def get_task(task_id):  # We define a method to get a task
        return f"SELECT * FROM TASK WHERE id = '{task_id}'"

    @staticmethod
    def get_all_tasks():  # We define a method to get all tasks
        return f"SELECT * FROM TASK"

    @staticmethod
    def get_task_name(task_name):  # We define a method to get a task
        return f"SELECT * FROM TASK WHERE name = '{task_name}'"

    @staticmethod
    def get_subtask(subtask_id):  # We define a method to get a subtask
        return f"SELECT * FROM SUBTASK WHERE id = '{subtask_id}'"

    @staticmethod
    def get_subtask_name(subtask_name):
        return f"SELECT * FROM SUBTASK WHERE name = '{subtask_name}'"

    @staticmethod
    def get_flag(flag_id):  # We define a method to get a flag
        return f"SELECT * FROM FLAG WHERE id = '{flag_id}'"

    @staticmethod
    def get_priority(priority_id):  # We define a method to get a priority
        return f"SELECT * FROM PRIORITY WHERE id = '{priority_id}'"

    @staticmethod
    def get_state(state_id):  # We define a method to get a state
        return f"SELECT * FROM STATE WHERE id = '{state_id}'"

    @staticmethod
    def get_task_due_date(task_id):  # We define a method to get a date in a task
        return f"SELECT due_date FROM TASK WHERE id = '{task_id}'"

    @staticmethod
    def get_subtask_due_date(
        subtask_id,
    ):  # We define a method to get a date in a subtask
        return f"SELECT due_date FROM SUBTASK WHERE id = '{subtask_id}'"

    @staticmethod
    def get_project(project_id):  # We define a method to get a project
        return f"SELECT * FROM PROJECT WHERE id = '{project_id}'"

    @staticmethod
    def get_user_project(user_id):  # We define a method to get a project in a user
        return f"SELECT * FROM PROJECT_USER WHERE user_id = '{user_id}'"

    @staticmethod
    def get_project_task(project_id):  # We define a method to get a task in a project
        return f"SELECT * FROM PROJECT_TASK WHERE project_id = '{project_id}'"

    # SETTER
    # The setter are used to add a new element to the database
    @staticmethod
    def add_user_secure(mail, password, name, rights_id):
        # Générer un sel
        salt = bcrypt.gensalt()

        # Hacher le mot de passe avec le sel
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

        # Convertir le sel et le mot de passe haché en chaînes de caractères
        salt_str = salt.decode("utf-8")
        hashed_password_str = hashed_password.decode("utf-8")

        # Utiliser des paramètres de requête pour éviter les attaques par injection SQL
        query = "INSERT INTO USER (mail, password, name, rights_id, salt) VALUES (%s, %s, %s, %s, %s)"

        # Passer les valeurs en tant que tuple pour les paramètres de requête
        values = (mail, hashed_password_str, name, rights_id, salt_str)

        return query, values

    @staticmethod
    def add_task(
        name, description, priority_id, flag_id, user_id, state_id, due_date, project_id
    ):  # We define a method to add a task
        query = """
                INSERT INTO TASK (name, description, priority_id, flag_id, user_id, state_id, due_date, project_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        data = (
            name,
            description,
            priority_id,
            flag_id,
            user_id,
            state_id,
            due_date,
            project_id,
        )

        # Include a placeholder for the newly inserted task's ID
        query += "SET @task_id = LAST_INSERT_ID();"

        return query, data

    @staticmethod
    def add_subtask(
        name, description, state_id, flag_id, user_id, priority_id, due_date
    ):  # We define a method to add a subtask (and link it later to a task)
        query = """
            INSERT INTO SUBTASK (name, description, state_id, flag_id, user_id, priority_id, due_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        data = (name, description, state_id, flag_id, user_id, priority_id, due_date)

        # Include a placeholder for the newly inserted subtask's ID
        query += "SET @subtask_id = LAST_INSERT_ID();"

        return query, data

    @staticmethod
    def add_project(name, description, user_id):  # We define a method to add a project
        return f"INSERT INTO PROJECT (name, description, user_id) VALUES ('{name}', '{description}', '{user_id}')"

    @staticmethod
    def add_flag(name, color):  # We define a method to add a flag
        return f"INSERT INTO FLAG (name, color) VALUES ('{name}', '{color}')"

    @staticmethod
    def add_priority(name):  # We define a method to add a priority
        return f"INSERT INTO PRIORITY (name) VALUES ('{name}')"

    @staticmethod
    def add_state(name):  # We define a method to add a state
        return f"INSERT INTO STATE (name) VALUES ('{name}')"

    @staticmethod
    def add_user_to_task(
        user_id, task_id
    ):  # We define a method to add a user to a task
        return f"INSERT INTO TASK_USER (user_id, task_id) VALUES ('{user_id}', '{task_id}')"

    @staticmethod
    def add_user_to_subtask(
        user_id, subtask_id
    ):  # We define a method to add a user to a subtask
        return f"INSERT INTO SUBTASK_USER (user_id, subtask_id) VALUES ('{user_id}', '{subtask_id}')"

    @staticmethod
    def add_subtask_to_task(
        subtask_id, task_id
    ):  # We define a method to add a subtask to a task
        return f"INSERT INTO TASK_SUBTASK (subtask_id, task_id) VALUES ('{subtask_id}', '{task_id}')"

    # UPDATER
    # The updater are used to update an element in the database
    @staticmethod
    def update_user(
        id, mail, password, name, rights_id
    ):  # We define a method to update a user
        return f"UPDATE USER SET mail = '{mail}', password = '{password}', name = '{name}', rights_id = '{rights_id}' WHERE id = '{id}'"

    @staticmethod
    def update_project(
        id, name, description, user_id
    ):  # We define a method to update a project
        return f"UPDATE PROJECT SET name = '{name}', description = '{description}', user_id = '{user_id}' WHERE id = '{id}'"

    @staticmethod
    def update_task(
        id, name, description, priority_id, flag_id, user_id, state_id, subtask_id
    ):  # We define a method to update a task
        return f"UPDATE TASK SET name = '{name}', description = '{description}', priority_id = '{priority_id}', flag_id = '{flag_id}', user_id = '{user_id}', state_id = '{state_id}', subtask_id = '{subtask_id}' WHERE id = '{id}'"

    @staticmethod
    def update_subtask(
        id, name, description, priority_id, flag_id, user_id, state_id
    ):  # We define a method to update a subtask
        return f"UPDATE SUBTASK SET name = '{name}', description = '{description}', priority_id = '{priority_id}', flag_id = '{flag_id}', user_id = '{user_id}', state_id = '{state_id}' WHERE id = '{id}'"

    @staticmethod
    def update_flag(id, name, color):  # We define a method to update a flag
        return f"UPDATE FLAG SET name = '{name}', color = '{color}' WHERE id = '{id}'"

    @staticmethod
    def update_priority(id, name):  # We define a method to update a priority
        return f"UPDATE PRIORITY SET name = '{name}' WHERE id = '{id}'"

    @staticmethod
    def update_state(id, name):  # We define a method to update a state
        return f"UPDATE STATE SET name = '{name}' WHERE id = '{id}'"

    @staticmethod
    def update_date_task(id, due_date):  # We define a method to update a date in a task
        return f"UPDATE TASK SET due_date = '{due_date}' WHERE id = '{id}'"

    @staticmethod
    def update_date_subtask(
        id, due_date
    ):  # We define a method to update a date in a subtask
        return f"UPDATE SUBTASK SET due_date = '{due_date}' WHERE id = '{id}'"

    @staticmethod
    def update_user_to_task(
        user_id, task_id
    ):  # We define a method to update a user in a task
        return f"UPDATE TASK_USER SET user_id = '{user_id}' WHERE task_id = '{task_id}'"

    @staticmethod
    def update_user_to_subtask(
        user_id, subtask_id
    ):  # We define a method to update a user in a subtask
        return f"UPDATE SUBTASK_USER SET user_id = '{user_id}' WHERE subtask_id = '{subtask_id}'"

    @staticmethod
    def update_task_to_subtask(
        task_id, subtask_id
    ):  # We define a method to update a task in a subtask
        return f"UPDATE TASK_SUBTASK SET task_id = '{task_id}' WHERE subtask_id = '{subtask_id}'"

    # DELETER
    # The deleter are used to delete an element from the database
    @staticmethod
    def delete_user(id):  # We define a method to delete a user
        return f"DELETE FROM USER WHERE id = '{id}'"

    @staticmethod
    def delete_task(id):  # We define a method to delete a task
        return f"DELETE FROM TASK WHERE id = '{id}'"

    @staticmethod
    def delete_subtask(id):  # We define a method to delete a subtask
        return f"DELETE FROM SUBTASK WHERE id = '{id}'"

    @staticmethod
    def delete_flag(id):  # We define a method to delete a flag
        return f"DELETE FROM FLAG WHERE id = '{id}'"

    @staticmethod
    def delete_priority(id):  # We define a method to delete a priority
        return f"DELETE FROM PRIORITY WHERE id = '{id}'"

    @staticmethod
    def delete_state(id):  # We define a method to delete a state
        return f"DELETE FROM STATE WHERE id = '{id}'"

    # REQUESTS
    # All of the specific requests we need are stored here
    @staticmethod
    def get_user_in_task(task_id):  # We define a method to get the user in a task
        return f"SELECT USER.id, USER.name FROM USER INNER JOIN TASK ON USER.id = TASK.user_id WHERE TASK.id = '{task_id}'"

    @staticmethod
    def get_user_in_subtask(
        subtask_id,
    ):  # We define a method to get the user in a subtask
        return f"SELECT USER.id, USER.name FROM USER INNER JOIN SUBTASK ON USER.id = SUBTASK.user_id WHERE SUBTASK.id = '{subtask_id}'"

    @staticmethod
    def get_subtask_in_task(task_id):  # We define a method to get the subtask in a task
        return f"SELECT SUBTASK.id, SUBTASK.name FROM SUBTASK INNER JOIN TASK ON SUBTASK.id = TASK.subtask_id WHERE TASK.id = '{task_id}'"

    @staticmethod
    def get_priority_in_task(
        task_id,
    ):  # We define a method to get the priority in a task
        return f"SELECT PRIORITY.id, PRIORITY.name FROM PRIORITY INNER JOIN TASK ON PRIORITY.id = TASK.priority_id WHERE TASK.id = '{task_id}'"

    @staticmethod
    def get_flag_in_task(task_id):  # We define a method to get the flag in a task
        return f"SELECT FLAG.id, FLAG.name FROM FLAG INNER JOIN TASK ON FLAG.id = TASK.flag_id WHERE TASK.id = '{task_id}'"

    @staticmethod
    def get_state_in_task(task_id):  # We define a method to get the state in a task
        return f"SELECT STATE.id, STATE.name FROM STATE INNER JOIN TASK ON STATE.id = TASK.state_id WHERE TASK.id = '{task_id}'"

    @staticmethod
    def get_priority_in_subtask(
        subtask_id,
    ):  # We define a method to get the priority in a subtask
        return f"SELECT PRIORITY.id, PRIORITY.name FROM PRIORITY INNER JOIN SUBTASK ON PRIORITY.id = SUBTASK.priority_id WHERE SUBTASK.id = '{subtask_id}'"

    @staticmethod
    def get_flag_in_subtask(
        subtask_id,
    ):  # We define a method to get the flag in a subtask
        return f"SELECT FLAG.id, FLAG.name FROM FLAG INNER JOIN SUBTASK ON FLAG.id = SUBTASK.flag_id WHERE SUBTASK.id = '{subtask_id}'"

    @staticmethod
    def get_state_in_subtask(
        subtask_id,
    ):  # We define a method to get the state in a subtask
        return f"SELECT STATE.id, STATE.name FROM STATE INNER JOIN SUBTASK ON STATE.id = SUBTASK.state_id WHERE SUBTASK.id = '{subtask_id}'"

    @staticmethod
    def get_password_secure(username, mail): # We define a method to get the password and the salt of a user
        return f"SELECT password, salt FROM USER WHERE name = '{username}' AND mail = '{mail}'"

    @staticmethod
    def get_user_in_project(project_id): # We define a method to get the user in a project
        return f"SELECT USER.id, USER.name FROM USER INNER JOIN PROJECT_USER ON USER.id = PROJECT_USER.user_id WHERE PROJECT_USER.project_id = '{project_id}'"

    # SEARCH
    # All of the search requests we need are stored here
    @staticmethod
    def search_user(username):  # We define a method to search a user
        return f"SELECT * FROM USER WHERE name LIKE '%{username}%'"

    @staticmethod
    def search_project(projectname): # We define a method to search a project
        return f"SELECT * FROM PROJECT WHERE name LIKE '%{projectname}%'"

    @staticmethod
    def search_task(asker_id):  # We define a method to search a task
        return f"SELECT TASK.name FROM TASK WHERE TASK.id IN (SELECT task_id FROM TASK_USER WHERE user_id = '{asker_id}');"

    @staticmethod
    def search_subtask(subtaskname):  # We define a method to search a subtask
        return f"SELECT * FROM SUBTASK WHERE name LIKE '%{subtaskname}%'"

    @staticmethod
    def search_flag(flagname):  # We define a method to search a flag
        return f"SELECT * FROM FLAG WHERE name LIKE '%{flagname}%'"
    
    @staticmethod
    def search_priority(priorityname): # We define a method to search a priority
        return f"SELECT * FROM PRIORITY WHERE name LIKE '%{priorityname}%'"
    
    @staticmethod
    def search_state(statename): # We define a method to search a state
        return f"SELECT * FROM STATE WHERE name LIKE '%{statename}%'"

    @staticmethod
    def search_task_by_name_and_state(
        task_name, state_id
    ):  # We define a method to search a task by name and state
        return f"SELECT * FROM TASK WHERE name LIKE '%{task_name}%' AND state_id = '{state_id}'"

    @staticmethod
    def search_task_by_priority_and_user(
        priority_id, user_id
    ):  # We define a method to search a task by priority and user
        return f"SELECT * FROM TASK WHERE priority_id = '{priority_id}' AND user_id = '{user_id}'"

    @staticmethod
    def search_task_by_flag_and_due_date(
        flag_id, due_date
    ):  # We define a method to search a task by flag and due date
        return f"SELECT * FROM TASK WHERE flag_id = '{flag_id}' AND due_date = '{due_date}'"

    @staticmethod
    def search_subtask_by_name_and_user(
        subtask_name, user_id
    ):  # We define a method to search a subtask by name and user
        return f"SELECT * FROM SUBTASK WHERE name LIKE '%{subtask_name}%' AND user_id = '{user_id}'"

    @staticmethod
    def search_project_by_name_and_description(
        project_name, project_description
    ):  # We define a method to search a project by name and description
        return f"SELECT * FROM PROJECT WHERE name LIKE '%{project_name}%' AND description LIKE '%{project_description}%'"
