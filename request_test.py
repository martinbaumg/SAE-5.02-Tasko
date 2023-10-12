import database_connection
from requests_list import RequestList  # Correct the import statement for RequestList

# This program is used to test parsing arguments from the command line to the database_connection.py

# We connect to the database
db = database_connection.DatabaseConnection()
db.connect()  # Connect to the database

# Specify the subtask information
task_name = "New Task"
task_description = "Description of the task"
state_id = 1  # Replace with the actual state_id
flag_id = 1  # Replace with the actual flag_id
user_id = 1  # Replace with the actual user_id
priority_id = 1  # Replace with the actual priority_id
due_date = "2021-01-01"  # Replace with the actual due_date

# Specify the task_id to which you want to link the subtask
project_id = 1  # Replace with the actual task_id

# Create a cursor
cursor = db.connection.cursor()

try:
    # Call the stored procedure to insert the subtask and retrieve the subtask_id
    cursor.callproc(
        "AddTaskAndReturnID",
        (
            task_name,
            task_description,
            state_id,
            flag_id,
            user_id,
            priority_id,
            due_date,
        ),
    )

    # Fetch the subtask_id from the procedure result
    cursor.execute("SELECT @task_id;")
    result = cursor.fetchone()

    if result is not None:
        task_id = result[0]
    else:
        raise Exception("Failed to retrieve task_id from the procedure")

    # Insert a record into TASK_SUBTASK to link the subtask to the task
    link_query = "INSERT INTO PROJECT_TASK (project_id, task_id) VALUES (%s, %s);"
    link_data = (project_id, task_id)

    # Execute the link query
    cursor.execute(link_query, link_data)

    db.connection.commit()  # Commit the changes to the database

except Exception as e:
    print(f"An error occurred: {e}")

db.disconnect()  # Disconnect from the database

"""
# Specify the username you want to query
username = "Totor"  # Change this to the desired username
task_id = 1  # Change this to the desired task_id
subtask_id = 1  # Change this to the desired subtask_id
flag_id = 1  # Change this to the desired flag_id

# Create a query using the get_user method from RequestList
#query = RequestList.get_user(username)
query = RequestList.get_flag(flag_id)

# Execute the query using the execute_query method
db.execute_query(query)

db.connection.commit()  # Commit the changes to the database

db.disconnect()  # Disconnect from the database
"""


### This part is made to add a subtask and link it to a task ###
""" 
# Specify the subtask information
subtask_name = "New Subtask"
subtask_description = "Description of the subtask"
state_id = 1  # Replace with the actual state_id
flag_id = 1  # Replace with the actual flag_id
user_id = 1  # Replace with the actual user_id
priority_id = 1  # Replace with the actual priority_id
due_date = "2021-01-01"  # Replace with the actual due_date

# Specify the task_id to which you want to link the subtask
task_id = 1  # Replace with the actual task_id

# Create a cursor
cursor = db.connection.cursor()

try:
    # Call the stored procedure to insert the subtask and retrieve the subtask_id
    cursor.callproc("AddSubtaskAndReturnID", (subtask_name, subtask_description, state_id, flag_id, user_id, priority_id, due_date))

    # Fetch the subtask_id from the procedure result
    cursor.execute("SELECT @subtask_id;")
    result = cursor.fetchone()

    if result is not None:
        subtask_id = result[0]
    else:
        raise Exception("Failed to retrieve subtask_id from the procedure")

    # Insert a record into TASK_SUBTASK to link the subtask to the task
    link_query = "INSERT INTO TASK_SUBTASK (task_id, subtask_id) VALUES (%s, %s);"
    link_data = (task_id, subtask_id)

    # Execute the link query
    cursor.execute(link_query, link_data)

    db.connection.commit()  # Commit the changes to the database

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and disconnect from the database
    cursor.close()
    db.disconnect()
"""
### ------------ ###
