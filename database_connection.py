import mysql.connector as mysql
from mysql.connector import Error


class DatabaseConnection:  # We create a class DatabaseConnection
    def __init__(self):
        self.host = "45.154.99.10"
        self.database = "tasko"
        self.user = "admin"
        self.password = "48wGK#t0:ZOx9c"
        self.connection = None
        self.cursor = None  # Add a cursor attribute

    def connect(self):  # We connect to the database
        try:
            self.connection = mysql.connect(  # Connect to the database
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                connect_timeout=100,
            )
            if (
                self.connection.is_connected()
            ):  # If the connection is established, we print a message
                print("Connected to MySQL database")
                self.cursor = self.connection.cursor()  # Create a cursor
                return self.connection
        except (
            Error
        ) as e:  # If the connection is not established, we print an error message
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):  # We disconnect from the database
        if self.connection.is_connected():
            self.cursor.close()  # Close the cursor
            self.connection.close()
            print("MySQL Database connection closed")

    def execute_query(self, query, data=None):  # We define a method to execute a query
        try:
            if data:
                self.cursor.execute(
                    query, data
                )  # Execute the query with parameter values
            else:
                self.cursor.execute(query)  # Execute the query without parameters
            result = self.cursor.fetchall()
            print(f"Query: {query}")
            print(f"Result: {result}")
            print()
        except Error as e:  # If the query is not executed, we print an error message
            print(f'The error "{e}" occurred')


class main:  # We create a class main
    def __init__(self):
        self.db = (
            DatabaseConnection()
        )  # We create an instance of the class DatabaseConnection
        self.connection = self.db.connect()  # We connect to the database

        # self.db.execute_query('SELECT SUBTASK.name, USER.name FROM SUBTASK_USER INNER JOIN SUBTASK ON SUBTASK_USER.subtask_id = SUBTASK.id INNER JOIN USER ON SUBTASK_USER.user_id = USER.id;') # Request for users affected to a subtask
        # self.db.execute_query('SELECT TASK.name, SUBTASK.name FROM SUBTASK_USER INNER JOIN SUBTASK ON SUBTASK_USER.subtask_id = SUBTASK.id INNER JOIN TASK_SUBTASK ON SUBTASK.id = TASK_SUBTASK.subtask_id INNER JOIN TASK ON TASK_SUBTASK.task_id = TASK.id;') # Request for subtasks affected to a task
        # self.db.execute_query('SELECT TASK.name, USER.name FROM TASK_USER INNER JOIN TASK ON TASK_USER.task_id = TASK.id INNER JOIN USER ON TASK_USER.user_id = USER.id;') # Request for users affected to a task

        # self.db.execute_query('INSERT INTO USER (mail, password, name, rights_id) VALUES ("micha@test.com", "micha", "micha",2)') # Adding a user to the database
        # self.db.execute_query('INSERT INTO TASK (name, description, priority_id, flag_id, user_id, state_id, subtask_id) VALUES ("testviapython", "descriptionviapython", 1, 1, 1, 1, 1)') # Adding a task to the database
        # self.db.execute_query('INSERT INTO FLAG (name, color) VALUES ("testviapython", "#000000")') # Adding a flag to the database

        # self.connection.commit() # We commit the changes to the database

        self.db.disconnect()  # We disconnect from the database


if __name__ == "__main__":  # We call the main function
    main()
