import mysql.connector as mysql
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.host = '45.154.99.10'
        self.database = 'tasko'
        self.user = 'admin'
        self.password = '48wGK#t0:ZOx9c'
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')
    
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print('MySQL Database connection closed')

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            print(f'Query: {query}')
            print(f'Result: {result}')
            print()
        except Error as e:
            print(f'The error "{e}" occurred')
    

    

class main:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()
        #self.db.execute_query('SELECT * FROM USER')
        #self.db.execute_query('SELECT * FROM TASK')
        #self.db.execute_query('SELECT * FROM SUBTASK')
        self.db.execute_query('SELECT * FROM USER')
        self.db.execute_query('INSERT INTO USER (mail, password, name, rights_id) VALUES ("test@test.com", "testpassword", "testname",2)')
        self.db.execute_query('SELECT * FROM USER')
        #self.db.execute_query('INSERT INTO FLAG (name, color) VALUES ("testflagviapython", "#000000")')
        #self.db.execute_query('SELECT * FROM FLAG')
        self.db.disconnect()

def add_task(task_text, info_task):
        conn = mysql.connect("database_connection.py")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TASK (task_name, task_text) VALUES (?, ?)", (task_text, info_task))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    main()