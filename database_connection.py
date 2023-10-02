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
            print('MySQL Database connection successful')
        except Error as e:
            print(f'The error "{e}" occurred')
    
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print('MySQL Database connection closed')

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print('Query executed successfully')
        except Error as e:
            print(f'The error "{e}" occurred')

class main:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()
        self.db.disconnect()