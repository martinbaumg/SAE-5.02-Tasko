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

    def execute_query(self, query, values):
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()  # Commit the transaction
            return cursor.rowcount > 0  # Return True if rows are affected
        except Exception as e:
            print(f"Query execution error: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


class main:  # We create a class main
    def __init__(self):
        self.db = (
            DatabaseConnection()
        )  # We create an instance of the class DatabaseConnection
        self.connection = self.db.connect()  # We connect to the database


if __name__ == "__main__":  # We call the main function
    main()
