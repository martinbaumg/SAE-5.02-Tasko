import pytest
import database_connection
from requests_list import RequestList  # Correct the import statement for RequestList


@pytest.fixture(scope="module")
def db_connection():
    # Create a DatabaseConnection instance and connect to the database
    db = database_connection.DatabaseConnection()
    db.connect()

    yield db  # Provide the db connection as a fixture

    # Teardown code: disconnect from the database after the test is done
    db.disconnect()


# Use the db_connection fixture in your test functions
def test_get_user(db_connection):
    # Specify the username you want to query
    username = "Totor"  # Change this to the desired username

    # Create a query using the get_user method from RequestList
    query = RequestList.get_user(username)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_task method from RequestList
    query = RequestList.get_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_all_tasks(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_task method from RequestList
    query = RequestList.get_all_tasks()

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_task_name(db_connection):
    # Specify the task_id you want to query
    task_name = "testtask"  # Change this to the desired task_id

    # Create a query using the get_task method from RequestList
    query = RequestList.get_task_name(task_name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_subtask method from RequestList
    query = RequestList.get_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_subtask_name(db_connection):
    # Specify the subtask_id you want to query
    subtask_name = "subtasktest"  # Change this to the desired subtask_id

    # Create a query using the get_subtask method from RequestList
    query = RequestList.get_subtask_name(subtask_name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_flag(db_connection):
    # Specify the flag_id you want to query
    flag_id = 1  # Change this to the desired flag_id

    # Create a query using the get_flag method from RequestList
    query = RequestList.get_flag(flag_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_priority(db_connection):
    # Specify the priority_id you want to query
    priority_id = 1  # Change this to the desired priority_id

    # Create a query using the get_priority method from RequestList
    query = RequestList.get_priority(priority_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_state(db_connection):
    # Specify the state_id you want to query
    state_id = 1  # Change this to the desired state_id

    # Create a query using the get_state method from RequestList
    query = RequestList.get_state(state_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_task_due_date(db_connection):
    # Specify the state_id you want to query
    task_id = 20  # Change this to the desired state_id

    # Create a query using the get_state method from RequestList
    query = RequestList.get_task_due_date(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_subtask_due_date(db_connection):
    # Specify the state_id you want to query
    subtask_id = 20  # Change this to the desired state_id

    # Create a query using the get_state method from RequestList
    query = RequestList.get_subtask_due_date(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_project(db_connection):
    # Specify the project_id you want to query
    project_id = 1  # Change this to the desired project_id

    # Create a query using the get_project method from RequestList
    query = RequestList.get_project(project_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_user_project(db_connection):
    # Specify the user_id you want to query
    user_id = 1  # Change this to the desired user_id

    # Create a query using the get_user_project method from RequestList
    query = RequestList.get_user_project(user_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_project_task(db_connection):
    # Specify the project_id you want to query
    project_id = 1  # Change this to the desired project_id

    # Create a query using the get_project_task method from RequestList
    query = RequestList.get_project_task(project_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_user(db_connection):
    # Specify the user information
    mail = "john@pytest.com"
    password = "password"
    name = "John"
    rights_id = 1  # Replace with the actual rights_id

    # Create a query using the add_user method from RequestList
    query = RequestList.add_user(mail, password, name, rights_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_task(db_connection):
    # Specify the task information
    name = "New Task PyTest"
    description = "Description of the task PyTest"
    priority_id = 1  # Replace with the actual priority_id
    flag_id = 1  # Replace with the actual flag_id
    user_id = 1  # Replace with the actual user_id
    state_id = 1  # Replace with the actual state_id
    subtask_id = 1  # Replace with the actual subtask_id
    due_date = "2021-01-01"  # Replace with the actual due_date

    # Create a query using the add_task method from RequestList
    query = RequestList.add_task(
        name, description, priority_id, flag_id, user_id, state_id, subtask_id, due_date
    )

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_subtask(db_connection):
    db = database_connection.DatabaseConnection()
    db.connect()  # Connect to the database
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
        cursor.callproc(
            "AddSubtaskAndReturnID",
            (
                subtask_name,
                subtask_description,
                state_id,
                flag_id,
                user_id,
                priority_id,
                due_date,
            ),
        )

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

    db.disconnect()  # Disconnect from the database


def test_add_project(db_connection):
    # Specify the project information
    name = "New Project"
    description = "Description of the project"
    user_id = 1  # Replace with the actual user_id

    # Create a query using the add_project method from RequestList
    query = RequestList.add_project(name, description, user_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_flag(db_connection):
    # Specify the flag information
    name = "New Flag"
    color = "#AAAAAA"

    # Create a query using the add_flag method from RequestList
    query = RequestList.add_flag(name, color)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_priority(db_connection):
    # Specify the priority information
    name = "New Priority"

    # Create a query using the add_priority method from RequestList
    query = RequestList.add_priority(name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_state(db_connection):
    # Specify the state information
    name = "New State"

    # Create a query using the add_state method from RequestList
    query = RequestList.add_state(name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_user_to_task(db_connection):
    # Specify the user_id and task_id you want to link
    user_id = 1  # Replace with the actual user_id
    task_id = 1  # Replace with the actual task_id

    # Create a query using the add_user_to_task method from RequestList
    query = RequestList.add_user_to_task(user_id, task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_user_to_subtask(db_connection):
    # Specify the user_id and subtask_id you want to link
    user_id = 1  # Replace with the actual user_id
    subtask_id = 1  # Replace with the actual subtask_id

    # Create a query using the add_user_to_subtask method from RequestList
    query = RequestList.add_user_to_subtask(user_id, subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_add_subtask_to_task(db_connection):
    # Specify the subtask_id and task_id you want to link
    subtask_id = 1  # Replace with the actual subtask_id
    task_id = 1  # Replace with the actual task_id

    # Create a query using the add_subtask_to_task method from RequestList
    query = RequestList.add_subtask_to_task(subtask_id, task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_user(db_connection):
    # Specify the user information
    id = 1  # Replace with the actual id
    mail = "testpytest@totor.com"
    password = "passwordupdated"
    name = "totorupdated"
    rights_id = 1  # Replace with the actual rights_id

    # Create a query using the update_user method from RequestList
    query = RequestList.update_user(id, mail, password, name, rights_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_project(db_connection):
    # Specify the project information
    id = 1  # Replace with the actual id
    name = "New Project Updated"
    description = "Description of the project Updated"
    user_id = 1  # Replace with the actual user_id

    # Create a query using the update_project method from RequestList
    query = RequestList.update_project(id, name, description, user_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_task(db_connection):
    # Specify the task information
    id = 4  # Replace with the actual id
    name = "New Task PyTest Updated"
    description = "Description of the task PyTest Updated"
    priority_id = 1  # Replace with the actual priority_id
    flag_id = 1  # Replace with the actual flag_id
    user_id = 1  # Replace with the actual user_id
    state_id = 1  # Replace with the actual state_id
    subtask_id = 1  # Replace with the actual subtask_id

    # Create a query using the update_task method from RequestList
    query = RequestList.update_task(
        id, name, description, priority_id, flag_id, user_id, state_id, subtask_id
    )

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_subtask(db_connection):
    # Specify the subtask information
    id = 7  # Replace with the actual id
    name = "New Subtask Updated"
    description = "Description of the subtask Updated"
    priority_id = 1  # Replace with the actual priority_id
    flag_id = 1  # Replace with the actual flag_id
    user_id = 1  # Replace with the actual user_id
    state_id = 1  # Replace with the actual state_id

    # Create a query using the update_subtask method from RequestList
    query = RequestList.update_subtask(
        id, name, description, priority_id, flag_id, user_id, state_id
    )

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_flag(db_connection):
    # Specify the flag information
    id = 4  # Replace with the actual id
    name = "New Flag Updated"
    color = "#BBBBBB"

    # Create a query using the update_flag method from RequestList
    query = RequestList.update_flag(id, name, color)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_priority(db_connection):
    # Specify the priority information
    id = 6  # Replace with the actual id
    name = "New Priority Updated"

    # Create a query using the update_priority method from RequestList
    query = RequestList.update_priority(id, name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_state(db_connection):
    # Specify the state information
    id = 6  # Replace with the actual id
    name = "New State Updated"

    # Create a query using the update_state method from RequestList
    query = RequestList.update_state(id, name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_date_task(db_connection):
    # Specify the state information
    id = 6  # Replace with the actual id
    date = "2023-01-01"

    # Create a query using the update_state method from RequestList
    query = RequestList.update_date_task(id, date)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_date_subtask(db_connection):
    # Specify the state information
    id = 6  # Replace with the actual id
    date = "2023-01-01"

    # Create a query using the update_state method from RequestList
    query = RequestList.update_date_subtask(id, date)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_user_to_task(db_connection):
    # Specify the user_id and task_id you want to link
    user_id = 7  # Replace with the actual user_id
    task_id = 1  # Replace with the actual task_id

    # Create a query using the update_user_to_task method from RequestList
    query = RequestList.update_user_to_task(user_id, task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_user_to_subtask(db_connection):
    # Specify the user_id and subtask_id you want to link
    user_id = 7  # Replace with the actual user_id
    subtask_id = 1  # Replace with the actual subtask_id

    # Create a query using the update_user_to_subtask method from RequestList
    query = RequestList.update_user_to_subtask(user_id, subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_update_task_to_subtask(db_connection):
    # Specify the task_id and subtask_id you want to link
    task_id = 1  # Replace with the actual task_id
    subtask_id = 18  # Replace with the actual subtask_id

    # Create a query using the update_task_to_subtask method from RequestList
    query = RequestList.update_task_to_subtask(task_id, subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def get_user_in_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_user_in_task method from RequestList
    query = RequestList.get_user_in_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def get_user_in_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_user_in_subtask method from RequestList
    query = RequestList.get_user_in_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_subtask_in_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_subtask_in_task method from RequestList
    query = RequestList.get_subtask_in_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_priority_in_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_priority_in_task method from RequestList
    query = RequestList.get_priority_in_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_flag_in_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_flag_in_task method from RequestList
    query = RequestList.get_flag_in_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_state_in_task(db_connection):
    # Specify the task_id you want to query
    task_id = 1  # Change this to the desired task_id

    # Create a query using the get_state_in_task method from RequestList
    query = RequestList.get_state_in_task(task_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_priority_in_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_priority_in_subtask method from RequestList
    query = RequestList.get_priority_in_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_flag_in_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_flag_in_subtask method from RequestList
    query = RequestList.get_flag_in_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_state_in_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_state_in_subtask method from RequestList
    query = RequestList.get_state_in_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_user_in_subtask(db_connection):
    # Specify the subtask_id you want to query
    subtask_id = 1  # Change this to the desired subtask_id

    # Create a query using the get_user_in_subtask method from RequestList
    query = RequestList.get_user_in_subtask(subtask_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_get_user_in_project(db_connection):
    # Specify the project_id you want to query
    project_id = 1  # Change this to the desired project_id

    # Create a query using the get_user_in_project method from RequestList
    query = RequestList.get_user_in_project(project_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_user(db_connection):
    # Specify the user information
    name = "louis"  # Replace with the actual name

    # Create a query using the search_user method from RequestList
    query = RequestList.search_user(name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_task(db_connection):
    # Specify the task information
    name = "testtask"  # Replace with the actual name

    # Create a query using the search_task method from RequestList
    query = RequestList.search_task(name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_subtask(db_connection):
    # Specify the subtask information
    name = "subtasktest"  # Replace with the actual name

    # Create a query using the search_subtask method from RequestList
    query = RequestList.search_subtask(name)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_task_by_name_and_state(db_connection):
    # Search for a task by name and state
    task_name = "testtask"  # Replace with the actual name
    state_id = 1  # Replace with the actual state_id

    # Create a query using the search_task_by_name_and_state method from RequestList
    query = RequestList.search_task_by_name_and_state(task_name, state_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_seartch_task_by_priority_and_user(db_connection):
    # Search for a task by priority and user
    priority_id = 1  # Replace with the actual priority_id
    user_id = 1  # Replace with the actual user_id

    # Create a query using the search_task_by_priority_and_user method from RequestList
    query = RequestList.search_task_by_priority_and_user(priority_id, user_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_task_by_flag_and_due_date(db_connection):
    # Search for a task by flag and due date
    flag_id = 1  # Replace with the actual flag_id
    due_date = "2021-01-01"  # Replace with the actual due_date

    # Create a query using the search_task_by_flag_and_due_date method from RequestList
    query = RequestList.search_task_by_flag_and_due_date(flag_id, due_date)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_subtask_by_name_and_user(db_connection):
    # Search for a subtask by name and user
    subtask_name = "subtasktest"  # Replace with the actual name
    user_id = 1  # Replace with the actual user_id

    # Create a query using the search_subtask_by_name_and_user method from RequestList
    query = RequestList.search_subtask_by_name_and_user(subtask_name, user_id)

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def test_search_project_by_name_and_description(db_connection):
    # Search for a project by name and description
    project_name = "testproject"  # Replace with the actual name
    project_description = (
        "Description of the project"  # Replace with the actual description
    )

    # Create a query using the search_project_by_name_and_description method from RequestList
    query = RequestList.search_project_by_name_and_description(
        project_name, project_description
    )

    # Execute the query using the execute_query method
    db_connection.execute_query(query)

    db_connection.connection.commit()  # Commit the changes to the database


def main():
    db = database_connection.DatabaseConnection()
    db.connect()  # Connect to the database

    yield db

    db.disconnect()  # Disconnect from the database
