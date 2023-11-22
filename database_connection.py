import mysql.connector as mysql
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.host = "45.154.99.10"
        self.database = "tasko"
        self.user = "admin"
        self.password = "48wGK#t0:ZOx9c"
        self.connection = self.connect()
        self.cursor = self.connection.cursor() if self.connection else None

    def connect(self):
        try:
            connection = mysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                connect_timeout=100,
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL Database connection closed")

    def execute_query(self, query, parameters=None):
        if self.connection is None or self.cursor is None:
            print("Database connection or cursor is not initialized.")
            return None
        try:
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            result = []
            if self.cursor.with_rows:  # Check if there are rows available to fetch
                result = self.cursor.fetchall()
            while self.cursor.nextset():  # Loop to handle multi-statement queries
                pass  # You can also fetch results of subsequent statements if necessary
            return result
        except Error as e:
            print(f"Something went wrong: {e}")
            return None

class main:  # We create a class main
    def __init__(self):
        self.db = (
            DatabaseConnection()
        )  # We create an instance of the class DatabaseConnection
        self.connection = self.db.connect()  # We connect to the database


if __name__ == "__main__":  # We call the main function
    main()
