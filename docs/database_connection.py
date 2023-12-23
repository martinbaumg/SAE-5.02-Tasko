import mysql.connector as mysql
from mysql.connector import Error

class DatabaseConnection:
    """
    This class manages the connection to a MySQL database.
    
    Attributes:
        host (str): The database host.
        database (str): The database name.
        user (str): The database user.
        password (str): The database password.
        connection: The database connection object.
        cursor: The cursor object for executing SQL queries.
    """

    def __init__(self):
        """
        Initializes an instance of the DatabaseConnection class.
        """
        self.host = '45.154.99.10'
        self.database = 'tasko'
        self.user = 'admin'
        self.password = '48wGK#t0:ZOx9c'
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establishes a connection to the MySQL database.

        Returns:
            object: The database connection object.

        Raises:
            Error: If there is an error in the connection.
        """
        try:
            self.connection = mysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print('Connected to MySQL database')
                self.cursor = self.connection.cursor()
                return self.connection
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')

    def disconnect(self):
        """
        Closes the connection to the MySQL database.
        """
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print('MySQL Database connection closed')

    def execute_query(self, query, data=None):
        """
        Executes an SQL query on the database.

        Args:
            query (str): The SQL query to execute.
            data: The data to use in the query (optional).

        Returns:
            list: The result of the SQL query.

        Raises:
            Error: If there is an error in executing the query.
        """
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(f'Query: {query}')
            print(f'Result: {result}')
            print()
        except Error as e:
            print(f'The error "{e}" occurred')

if __name__ == '__main__':
    main()
