import database_connection

# This program is used to test parsing arguments from the command line to the database_connection.py

# We connect to the database
db = database_connection.DatabaseConnection()
"""Class to connect to the database and execute queries.

Args:
    mail (str): The user's email address.
    password (str): The user's password.
    name (str): The user's name.
    rights_id (int): The user's rights ID.
"""
db.connect()  # Connect to the database

# Arguments
mail = str(input("Enter your mail: "))
password = str(input("Enter your password: "))
name = str(input("Enter your name: "))
rights_id = int(input("Enter your rights_id: "))

# Define the SQL query with placeholders using %s
"""
To create a user, we use this SQL query:
INSERT INTO USER (mail, password, name, rights_id) VALUES (%s, %s, %s, %s)
"""
add_user_create = ("INSERT INTO USER (mail, password, name, rights_id) VALUES (%s, %s, %s, %s)")

# Create a tuple with the parameter values
data_user_create = (mail, password, name, rights_id)

db.execute_query(add_user_create, data_user_create)  # Execute the query with parameter values

db.connection.commit()  # Commit the changes to the database

db.disconnect()  # Disconnect from the database
