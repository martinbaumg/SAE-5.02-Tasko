import mysql.connector as mysql # On importe le module mysql.connector
from mysql.connector import Error # On importe le module Error

class DatabaseConnection: # On créé une classe DatabaseConnection
    def __init__(self): # On créé une méthode __init__ qui sera appelée à chaque fois qu'on créé une instance de DatabaseConnection
        self.host = '45.154.99.10'
        self.database = 'tasko'
        self.user = 'admin'
        self.password = '48wGK#t0:ZOx9c'
        self.connection = None
    
    def connect(self): # On créé une méthode connect qui va nous permettre de nous connecter à la BDD
        try:
            self.connection = mysql.connect( # On se connecte à la BDD
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected(): # Si on est connecté à la BDD, on affiche un message
                print('Connected to MySQL database')
                return self.connection
        except Error as e: # Si on a une erreur, on l'affiche
            print(f'Error while connecting to MySQL: {e}')
    
    def disconnect(self): # On créé une méthode disconnect qui va nous permettre de nous déconnecter de la BDD
        if self.connection.is_connected():
            self.connection.close()
            print('MySQL Database connection closed')

    def execute_query(self, query): # On créé une méthode execute_query qui va nous permettre d'exécuter une requête SQL
        try:
            cursor = self.connection.cursor() # On créé un curseur
            cursor.execute(query) # On exécute la requête
            result = cursor.fetchall() # On récupère le résultat de la requête
            print(f'Query: {query}') # On affiche la requête
            print(f'Result: {result}') # On affiche le résultat
            print() # On affiche un saut de ligne
        except Error as e: # Si on a une erreur, on l'affiche
            print(f'The error "{e}" occurred')

class main: # On créé une classe main
    def __init__(self):
        self.db = DatabaseConnection() # On créé une instance de DatabaseConnection
        self.connection = self.db.connect() # On se connecte à la BDD


        #self.db.execute_query('SELECT SUBTASK.name, USER.name FROM SUBTASK_USER INNER JOIN SUBTASK ON SUBTASK_USER.subtask_id = SUBTASK.id INNER JOIN USER ON SUBTASK_USER.user_id = USER.id;') # Requête pour les utilisateurs affectés à une sous-tâche
        #self.db.execute_query('SELECT TASK.name, SUBTASK.name FROM SUBTASK_USER INNER JOIN SUBTASK ON SUBTASK_USER.subtask_id = SUBTASK.id INNER JOIN TASK_SUBTASK ON SUBTASK.id = TASK_SUBTASK.subtask_id INNER JOIN TASK ON TASK_SUBTASK.task_id = TASK.id;') # Requête pour les sous-tâches affectées à une tâche
        #self.db.execute_query('SELECT TASK.name, USER.name FROM TASK_USER INNER JOIN TASK ON TASK_USER.task_id = TASK.id INNER JOIN USER ON TASK_USER.user_id = USER.id;') # Requête pour les utilisateurs affectés à une tâche
        

        #self.db.execute_query('INSERT INTO USER (mail, password, name, rights_id) VALUES ("micha@test.com", "micha", "micha",2)') # Ajout d'un utilisateur à la BDD
        #self.db.execute_query('INSERT INTO TASK (name, description, priority_id, flag_id, user_id, state_id, subtask_id) VALUES ("testviapython", "descriptionviapython", 1, 1, 1, 1, 1)') # Ajout d'une tâche à la BDD
        #self.db.execute_query('INSERT INTO FLAG (name, color) VALUES ("testviapython", "#000000")') # Ajout d'un flag à la BDD

        #self.connection.commit() # On applique les changements à la BDD

        self.db.disconnect() # On se déconnecte de la BDD

if __name__ == '__main__': # Si on lance le fichier database_connection.py, on exécute la méthode main
    main()