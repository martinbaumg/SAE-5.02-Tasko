# this file contains the list of requests that are sent to the server
# they are stored as objects 

class RequestList:
    # GETTER
    # The getter are used to get an element from the database
    @staticmethod
    def get_user(username): # We define a method to get a user
        return f"SELECT * FROM USER WHERE name = '{username}'"  
    
    @staticmethod
    def get_task(task_id): # We define a method to get a task
        return f"SELECT * FROM TASK WHERE id = '{task_id}'"

    @staticmethod
    def get_subtask(subtask_id): # We define a method to get a subtask
        return f"SELECT * FROM SUBTASK WHERE id = '{subtask_id}'"
    
    @staticmethod
    def get_flag(flag_id): # We define a method to get a flag
        return f"SELECT * FROM FLAG WHERE id = '{flag_id}'"
    
    @staticmethod
    def get_priority(priority_id): # We define a method to get a priority
        return f"SELECT * FROM PRIORITY WHERE id = '{priority_id}'"
    
    @staticmethod
    def get_state(state_id): # We define a method to get a state
        return f"SELECT * FROM STATE WHERE id = '{state_id}'"
    
    # SETTER
    # The setter are used to add a new element to the database
    @staticmethod
    def add_user(mail, password, name, rights_id): # We define a method to add a user
        return f"INSERT INTO USER (mail, password, name, rights_id) VALUES ('{mail}', '{password}', '{name}', '{rights_id}')"
    
    @staticmethod
    def add_task(name, description, priority_id, flag_id, user_id, state_id, subtask_id): # We define a method to add a task
        return f"INSERT INTO TASK (name, description, priority_id, flag_id, user_id, state_id, subtask_id) VALUES ('{name}', '{description}', '{priority_id}', '{flag_id}', '{user_id}', '{state_id}', '{subtask_id}')"
    
    @staticmethod
    def add_subtask(name, description, state_id, flag_id, user_id, priority_id): # We define a method to add a subtask (and link it later to a task)
        query = """
            INSERT INTO SUBTASK (name, description, state_id, flag_id, user_id, priority_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        data = (name, description, state_id, flag_id, user_id, priority_id)

        # Include a placeholder for the newly inserted subtask's ID
        query += "SET @subtask_id = LAST_INSERT_ID();"
        
        return query, data

    @staticmethod
    def add_flag(name, color): # We define a method to add a flag
        return f"INSERT INTO FLAG (name, color) VALUES ('{name}', '{color}')"
    
    @staticmethod
    def add_priority(name): # We define a method to add a priority
        return f"INSERT INTO PRIORITY (name) VALUES ('{name}')"
    
    @staticmethod
    def add_state(name): # We define a method to add a state
        return f"INSERT INTO STATE (name VALUES ('{name}')"
    
    @staticmethod
    def add_user_to_task(user_id, task_id): # We define a method to add a user to a task
        return f"INSERT INTO TASK_USER (user_id, task_id) VALUES ('{user_id}', '{task_id}')"
    
    @staticmethod
    def add_user_to_subtask(user_id, subtask_id): # We define a method to add a user to a subtask
        return f"INSERT INTO SUBTASK_USER (user_id, subtask_id) VALUES ('{user_id}', '{subtask_id}')"
    
    @staticmethod
    def add_subtask_to_task(subtask_id, task_id): # We define a method to add a subtask to a task
        return f"INSERT INTO TASK_SUBTASK (subtask_id, task_id) VALUES ('{subtask_id}', '{task_id}')"
    
    # UPDATER
    # The updater are used to update an element in the database
    @staticmethod
    def update_user(id, mail, password, name, rights_id): # We define a method to update a user
        return f"UPDATE USER SET mail = '{mail}', password = '{password}', name = '{name}', rights_id = '{rights_id}' WHERE id = '{id}'"
    
    @staticmethod
    def update_task(id, name, description, priority_id, flag_id, user_id, state_id, subtask_id): # We define a method to update a task
        return f"UPDATE TASK SET name = '{name}', description = '{description}', priority_id = '{priority_id}', flag_id = '{flag_id}', user_id = '{user_id}', state_id = '{state_id}', subtask_id = '{subtask_id}' WHERE id = '{id}'"
    
    @staticmethod
    def update_subtask(id, name, description, priority_id, flag_id, user_id, state_id): # We define a method to update a subtask
        return f"UPDATE SUBTASK SET name = '{name}', description = '{description}', priority_id = '{priority_id}', flag_id = '{flag_id}', user_id = '{user_id}', state_id = '{state_id}' WHERE id = '{id}'"
    
    @staticmethod
    def update_flag(id, name, color): # We define a method to update a flag
        return f"UPDATE FLAG SET name = '{name}', color = '{color}' WHERE id = '{id}'"
    
    @staticmethod
    def update_priority(id, name): # We define a method to update a priority
        return f"UPDATE PRIORITY SET name = '{name}' WHERE id = '{id}'"
    
    @staticmethod
    def update_state(id, name): # We define a method to update a state
        return f"UPDATE STATE SET name = '{name}' WHERE id = '{id}'"
    
    @staticmethod
    def update_user_to_task(user_id, task_id): # We define a method to update a user in a task
        return f"UPDATE TASK_USER SET user_id = '{user_id}' WHERE task_id = '{task_id}'"
    
    @staticmethod
    def update_user_to_subtask(user_id, subtask_id): # We define a method to update a user in a subtask
        return f"UPDATE SUBTASK_USER SET user_id = '{user_id}' WHERE subtask_id = '{subtask_id}'"
    
    @staticmethod
    def update_task_to_subtask(task_id, subtask_id): # We define a method to update a task in a subtask
        return f"UPDATE TASK_SUBTASK SET task_id = '{task_id}' WHERE subtask_id = '{subtask_id}'"
    
    # DELETER
    # The deleter are used to delete an element from the database
    @staticmethod
    def delete_user(id): # We define a method to delete a user
        return f"DELETE FROM USER WHERE id = '{id}'"
    
    @staticmethod
    def delete_task(id): # We define a method to delete a task
        return f"DELETE FROM TASK WHERE id = '{id}'"
    
    @staticmethod
    def delete_subtask(id): # We define a method to delete a subtask
        return f"DELETE FROM SUBTASK WHERE id = '{id}'"
    
    @staticmethod
    def delete_flag(id): # We define a method to delete a flag
        return f"DELETE FROM FLAG WHERE id = '{id}'"
    
    @staticmethod
    def delete_priority(id): # We define a method to delete a priority
        return f"DELETE FROM PRIORITY WHERE id = '{id}'"
    
    @staticmethod
    def delete_state(id): # We define a method to delete a state
        return f"DELETE FROM STATE WHERE id = '{id}'"
    
    # REQUESTS
    # All of the specific requests we need are stored here
    @staticmethod
    def get_user_in_task(task_id): # We define a method to get the user in a task
        return f"SELECT USER.id, USER.name FROM USER INNER JOIN TASK ON USER.id = TASK.user_id WHERE TASK.id = '{task_id}'"
    
    @staticmethod
    def get_user_in_subtask(subtask_id): # We define a method to get the user in a subtask
        return f"SELECT USER.id, USER.name FROM USER INNER JOIN SUBTASK ON USER.id = SUBTASK.user_id WHERE SUBTASK.id = '{subtask_id}'"
    
    @staticmethod
    def get_subtask_in_task(task_id): # We define a method to get the subtask in a task
        return f"SELECT SUBTASK.id, SUBTASK.name FROM SUBTASK INNER JOIN TASK ON SUBTASK.id = TASK.subtask_id WHERE TASK.id = '{task_id}'"
    
    @staticmethod
    def get_priority_in_task(task_id): # We define a method to get the priority in a task
        return f"SELECT PRIORITY.id, PRIORITY.name FROM PRIORITY INNER JOIN TASK ON PRIORITY.id = TASK.priority_id WHERE TASK.id = '{task_id}'"
    
    @staticmethod
    def get_flag_in_task(task_id): # We define a method to get the flag in a task
        return f"SELECT FLAG.id, FLAG.name FROM FLAG INNER JOIN TASK ON FLAG.id = TASK.flag_id WHERE TASK.id = '{task_id}'"
    
    @staticmethod
    def get_state_in_task(task_id):
        return f"SELECT STATE.id, STATE.name FROM STATE INNER JOIN TASK ON STATE.id = TASK.state_id WHERE TASK.id = '{task_id}'"
    
    @staticmethod
    def get_priority_in_subtask(subtask_id): # We define a method to get the priority in a subtask
        return f"SELECT PRIORITY.id, PRIORITY.name FROM PRIORITY INNER JOIN SUBTASK ON PRIORITY.id = SUBTASK.priority_id WHERE SUBTASK.id = '{subtask_id}'"
    
    @staticmethod
    def get_flag_in_subtask(subtask_id): # We define a method to get the flag in a subtask
        return f"SELECT FLAG.id, FLAG.name FROM FLAG INNER JOIN SUBTASK ON FLAG.id = SUBTASK.flag_id WHERE SUBTASK.id = '{subtask_id}'"
    
    @staticmethod
    def get_state_in_subtask(subtask_id): # We define a method to get the state in a subtask
        return f"SELECT STATE.id, STATE.name FROM STATE INNER JOIN SUBTASK ON STATE.id = SUBTASK.state_id WHERE SUBTASK.id = '{subtask_id}'"
    
    @staticmethod
    def check_password_match(username, password):
        return f"SELECT * FROM USER WHERE name = '{username}' AND password = '{password}'"
