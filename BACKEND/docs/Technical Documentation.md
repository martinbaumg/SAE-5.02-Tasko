
### Introduction

Welcome to the TASKO Technical Documentation ! This resource is designed for developers who want to understand the inner workings of TASKO and have the knowledge to maintain, update, or enhance the project. We'll dive into the codebase, explaining key components, architecture, and best practices. Whether you're a seasoned developer or just starting, this documentation will equip you with the insights you need to work with TASKO effectively.

## Dependencies

- `flet`: A Python library for creating user interfaces.
- `bcrypt`: A library for hashing and checking passwords securely.
- `mysql.connector`: A MySQL driver for connecting and executing queries on the database.

## Getting Started

1. Install the required environment from `tasko_env.yml`.
2. Activate the environment using `conda activate tasko_env`.
3. Run the application with `python main.py`.

---

The `main.py` file is the primary Python script for the Tasko Reminder Application. This application provides users with functionalities to create, edit, delete, and manage tasks. The script uses the Flet package for the user interface, bcrypt for password hashing, and mysql.connector for database interactions.

## User Interface

The application's user interface is built using the `flet` library, which allows for a responsive and interactive experience. It includes text fields, buttons, dialogues, and other UI elements to provide a seamless user experience.

## Overview

The application is structured into several classes and functions, each serving a distinct purpose:

- **DatabaseConnection**: Manages database connections and query executions.
- **ToDo**: Represents the main task management interface.
- **TodoItem**: Represents individual task items in the ToDo interface.
- **RequestList**: Contains static methods for generating SQL queries.
- **MethodList**: Contains methods for executing database operations.
- **LoginPage**: Handles the user login interface.
- **SignupPage**: Manages the user registration interface.
- **Main Function**: Initializes and controls the application flow.

## Detailed Description

### `DatabaseConnection` Class

- **Purpose**: Handles database connectivity and operations.
- **Methods**:
    - `get_connection()`: Establishes and returns a connection to the MySQL database.
    - `execute_query(query, values, return_lastrowid)`: Executes a given SQL query with values.
    - `execute_select_query(query, values)`: Executes a SELECT SQL query.
    - `disconnect()`: Closes the database connection.

### `ToDo` Class

- **Purpose**: Main user interface for task management.
- **Methods**:
    - `create_delete_dialog()`: Creates a dialog box for confirming task deletion.
    - `refresh_ui()`, `update()`: Updates the UI with current task data.
    - `delete_item_callback(item)`: Callback for deleting a task.
    - `submit_item(e)`: Submits a new task.
    - `refresh_tasks()`, `clear_and_reload_tasks()`: Refreshes the task list.
    - `load_tasks()`: Loads tasks from the database.

### `TodoItem` Class

- **Purpose**: Represents a single task in the UI.
- **Methods**:
    - `edit_item(e)`, `save_edit(e)`, `delete_item(e)`: Handles task editing, saving, and deletion.
    - `copy_item(e)`: Copies task information to the clipboard.
    - `build()`: Constructs the UI for a single task item.

### `RequestList` Class

- **Purpose**: Provides static methods to create SQL queries.
- **Methods**:
    - `add_user(mail, name, hashed_password, salt)`: Creates a query to add a new user.
    - `authenticate_user(mail)`: Creates a query to authenticate a user.

### `MethodList` Class

- **Purpose**: Executes database operations using `DatabaseConnection`.
- **Methods**:
    - `register_user(mail, name, password)`: Registers a new user.
    - `login_user(mail, password)`: Authenticates a user.
    - `fetch_tasks(user_id)`: Fetches tasks for a given user.
    - `delete_task(task_id)`, `update_task(task_id, name, description, due_date)`: Manages task updates and deletions.
    - `add_task(name, description, due_date, user_id)`: Adds a new task.

### `LoginPage` Class

- **Purpose**: Manages the login interface.
- **Methods**:
    - `build()`: Builds the login page UI.
    - `on_login_click(e)`: Handles the login process.

### `SignupPage` Class

- **Purpose**: Manages the registration interface.
- **Methods**:
    - `build()`: Builds the signup page UI.
    - `on_signup_click(e)`: Handles the registration process.

### Main Function (`main`)

- **Purpose**: Initializes and controls the application flow.
- **Description**: Sets up the Flet application, initializes UI components, and manages navigation between different pages (login, signup, and todo).

## Application Flow

1. **Start**: The application starts by executing `ft.app(target=main)`.
2. **Login/Signup**: The user is first presented with a login page. They can switch to the signup page if they don't have an account.
3. **Task Management**: Once logged in, the user can view, add, edit, and delete tasks.

--- 

The `methods_list.py` module in the Tasko Reminder Application is a comprehensive collection of methods facilitating interactions with the application's database. It functions as a middleware between the database and the application's front-end, executing various CRUD (Create, Read, Update, Delete) operations and queries.

## Class: MethodList

### Constructor

- **Purpose**: Initializes the `DatabaseConnection` instance.
- **Parameters**: None.

### Methods

#### Getters

- **Purpose**: Retrieve data from the database.
- **Methods**:
    - `get_user(username)`: Retrieves a user by username.
    - `get_task(task_id)`: Fetches a task by its ID.
    - `get_all_tasks()`: Retrieves all tasks.
    - `get_task_name(task_name)`: Fetches tasks by name.
    - `get_subtasks(subtask_id)`: Retrieves subtasks by ID.
    - `get_subtask_name(subtask_name)`: Fetches subtasks by name.
    - `get_flag(flag_id)`: Retrieves a flag by its ID.
    - `get_priority(priority_id)`: Fetches a priority by its ID.
    - `get_state(state_id)`: Retrieves a state by its ID.
    - `get_task_due_date(task_id)`: Fetches the due date of a task.
    - `get_subtask_due_date(subtask_id)`: Retrieves the due date of a subtask.
    - `get_project(project_id)`: Fetches a project by its ID.
    - `get_user_project(user_id)`: Retrieves projects associated with a user.
    - `get_project_task(project_id)`: Fetches tasks associated with a project.

#### Setters

- **Purpose**: Insert data into the database.
- **Methods**:
    - `add_user(mail, password, name, rights_id)`: Adds a new user.
    - `add_task(...)`: Creates a new task.
    - `add_subtask(...)`: Inserts a new subtask.
    - `add_priority(name)`: Adds a new priority.
    - `add_state(name)`: Inserts a new state.
    - `add_user_to_task(user_id, task_id)`: Associates a user with a task.
    - `add_user_to_subtask(user_id, subtask_id)`: Links a user to a subtask.
    - `add_subtask_to_task(subtask_id, task_id)`: Associates a subtask with a task.

#### Updaters

- **Purpose**: Update existing data in the database.
- **Methods**:
    - `update_user(...)`: Modifies an existing user's details.
    - `update_project(...)`: Updates a project's details.
    - `update_task(...)`: Changes a task's attributes.
    - `update_subtask(...)`: Modifies a subtask's properties.
    - `update_flag(...)`: Updates a flag's details.
    - `update_priority(...)`: Changes a priority's name.
    - `update_state(...)`: Modifies a state's name.
    - `update_date_task(task_id, due_date)`: Updates a task's due date.
    - `update_date_subtask(subtask_id, due_date)`: Changes a subtask's due date.
    - `update_user_to_task(...)`: Modifies the user-task association.
    - `update_user_to_subtask(...)`: Changes the user-subtask link.

#### Deleters

- **Purpose**: Remove data from the database.
- **Methods**:
    - `delete_user(user_id)`: Deletes a user.
    - `delete_task(task_id)`: Removes a task.
    - `delete_subtask(subtask_id)`: Deletes a subtask.
    - `delete_flag(flag_id)`: Removes a flag.
    - `delete_priority(priority_id)`: Deletes a priority.
    - `delete_state(state_id)`: Removes a state.

#### Requests

- **Purpose**: Perform specific data retrieval operations.
- **Methods**:
    - `get_user_in_task(task_id)`: Retrieves users associated with a task.
    - `get_user_in_subtask(subtask_id)`: Fetches users linked to a subtask.
    - `get_subtask_in_task(task_id)`: Retrieves subtasks of a task.
    - `get_priority_in_task(task_id)`: Fetches priorities of a task.
    - `get_flag_in_task(task_id)`: Retrieves flags associated with a task.
    - `get_state_in_task(task_id)`: Fetches states of a task.
    - `get_priority_in_subtask(subtask_id)`: Retrieves priorities of a subtask.
    - `get_flag_in_subtask(subtask_id)`: Fetches flags of a subtask.
    - `get_state_in_subtask(subtask_id)`: Retrieves states of a subtask.
    - `get_task_in_project(project_id)`: Fetches tasks in a project.
    - `get_user_in_project(project_id)`: Retrieves users in a project.

#### Searches

- **Purpose**: Conduct search operations in the database.
- **Methods**:
    - `search_user(name)`: Searches for users by name.
    - `search_task(name)`: Looks up tasks by name.
    - `search_subtask(name)`: Searches for subtasks by name.
    - `search_flag(name)`: Looks up flags by name.
    - `search_priority(name)`: Searches for priorities by name.
    - `search_state(name)`: Looks up states by name.
    - `search_project(name)`: Searches for projects by name.
    - `search_task_by_name_and_state(...)`: Searches tasks by name and state.
    - `serch_task_by_priority_and_user(...)`: Looks up tasks by priority and user.
    - `search_task_by_flag_and_due_date(...)`: Searches tasks by flag and due date.
    - `search_subtask_by_name_and_user(...)`: Looks up subtasks by name and user.
    - `search_project_by_name_and_description(...)`: Searches projects by name and description.

#### Security

- **Purpose**: Ensure password security.
- **Methods**:
    - `check_password_secure(mail, user_password)`: Verifies a user's password.

---

The `requests_list.py` file in the Tasko Reminder Application serves as a centralized repository of SQL queries. These queries are used across the application to interact with the database for various operations, including fetching, creating, updating, and deleting records.

## Class: RequestList

### Getters

- **Purpose**: Retrieve data from the database.
- **Methods**:
    - `get_user(username)`: Fetches a user by their username.
    - `get_task(task_id)`: Retrieves a task by its ID.
    - `get_all_tasks()`: Gets all tasks in the database.
    - `get_task_name(task_name)`: Fetches tasks by their name.
    - `get_subtask(subtask_id)`: Retrieves a subtask by its ID.
    - `get_subtask_name(subtask_name)`: Gets subtasks by their name.
    - `get_flag(flag_id)`: Fetches a flag by its ID.
    - `get_priority(priority_id)`: Retrieves a priority by its ID.
    - `get_state(state_id)`: Fetches a state by its ID.
    - `get_task_due_date(task_id)`: Retrieves the due date of a task.
    - `get_subtask_due_date(subtask_id)`: Gets the due date of a subtask.
    - `get_project(project_id)`: Fetches a project by its ID.
    - `get_user_project(user_id)`: Retrieves projects associated with a user.
    - `get_project_task(project_id)`: Gets tasks associated with a project.

### Setters

- **Purpose**: Insert new records into the database.
- **Methods**:
    - `add_user_secure(mail, password, name, rights_id)`: Adds a new user with secure password hashing.
    - `add_task(...)`: Creates a new task.
    - `add_subtask(...)`: Inserts a new subtask.
    - `add_project(name, description, user_id)`: Adds a new project.
    - `add_flag(name, color)`: Inserts a new flag.
    - `add_priority(name)`: Adds a new priority.
    - `add_state(name)`: Inserts a new state.
    - `add_user_to_task(user_id, task_id)`: Associates a user with a task.
    - `add_user_to_subtask(user_id, subtask_id)`: Links a user to a subtask.
    - `add_subtask_to_task(subtask_id, task_id)`: Associates a subtask with a task.

### Updaters

- **Purpose**: Update existing records in the database.
- **Methods**:
    - `update_user(...)`: Modifies an existing user's details.
    - `update_project(...)`: Updates a project's details.
    - `update_task(...)`: Changes a task's attributes.
    - `update_subtask(...)`: Modifies a subtask's properties.
    - `update_flag(...)`: Updates a flag's details.
    - `update_priority(...)`: Changes a priority's name.
    - `update_state(...)`: Modifies a state's name.
    - `update_date_task(...)`: Updates a task's due date.
    - `update_date_subtask(...)`: Changes a subtask's due date.
    - `update_user_to_task(...)`: Modifies the user-task association.
    - `update_user_to_subtask(...)`: Changes the user-subtask link.
    - `update_task_to_subtask(...)`: Modifies the task-subtask relationship.

### Deleters

- **Purpose**: Remove records from the database.
- **Methods**:
    - `delete_user(id)`: Deletes a user.
    - `delete_task(id)`: Removes a task.
    - `delete_subtask(id)`: Deletes a subtask.
    - `delete_flag(id)`: Removes a flag.
    - `delete_priority(id)`: Deletes a priority.
    - `delete_state(id)`: Removes a state.

### Requests

- **Purpose**: Perform specific data retrieval operations.
- **Methods**:
    - `get_user_in_task(task_id)`: Retrieves users associated with a task.
    - `get_user_in_subtask(subtask_id)`: Fetches users linked to a subtask.
    - `get_subtask_in_task(task_id)`: Retrieves subtasks of a task.
    - `get_priority_in_task(task_id)`: Fetches priorities of a task.
    - `get_flag_in_task(task_id)`: Retrieves flags associated with a task.
    - `get_state_in_task(task_id)`: Fetches states of a task.
    - `get_priority_in_subtask(subtask_id)`: Retrieves priorities of a subtask.
    - `get_flag_in_subtask(subtask_id)`: Fetches flags of a subtask.
    - `get_state_in_subtask(subtask_id)`: Retrieves states of a subtask.
    - `get_password_secure(username, mail)`: Fetches the password and salt of a user.
    - `get_user_in_project(project_id)`: Retrieves users in a project.

### Search Functions

- **Purpose**: Conduct search operations in the database.
- **Methods**:
    - `search_user(username)`: Searches for users by name.
    - `search_project(projectname)`: Looks up projects by name.
    - `search_task(asker_id)`: Fetches tasks associated with a user.
    - `search_subtask(subtaskname)`: Searches for subtasks by name.
    - `search_flag(flagname)`: Looks up flags by name.
    - `search_priority(priorityname)`: Searches for priorities by name.
    - `search_state(statename)`: Looks up states by name.
    - `search_task_by_name_and_state(...)`: Searches tasks by name and state.
    - `search_task_by_priority_and_user(...)`: Looks up tasks by priority and user.
    - `search_task_by_flag_and_due_date(...)`: Searches tasks by flag and due date.
    - `search_subtask_by_name_and_user(...)`: Looks up subtasks by name and user.
    - `search_project_by_name_and_description(...)`: Searches projects by name and description.

---

The `security.py` module in the Tasko Reminder Application is dedicated to handling password security through hashing and verification. It uses the `bcrypt` library to secure passwords, ensuring that sensitive user data is safely stored and validated.

## Overview

This module provides two primary functions: `hash_password` for hashing a password and `check_password` for verifying a hashed password. These functions are critical for maintaining user security in the application.

## Functions

### `hash_password(password)`

- **Purpose**: Generates a hashed password using bcrypt.
- **Parameters**:
    - `password` (str): The plain text password to be hashed.
- **Returns**:
    - `salt` (bytes): The generated salt used for hashing.
    - `hashed_password` (bytes): The hashed password.
- **Description**:
    - This function takes a plain text password, generates a random salt using `bcrypt.gensalt()`, and then creates a hashed password using `bcrypt.hashpw()`. The salt and the hashed password are returned.

### `check_password(input_password, stored_salt, stored_hashed_password)`

- **Purpose**: Verifies if an input password matches the stored hashed password.
- **Parameters**:
    - `input_password` (str): The plain text password to verify.
    - `stored_salt` (bytes): The salt used to hash the stored password.
    - `stored_hashed_password` (bytes): The hashed password stored in the database.
- **Returns**:
    - `True` or `False` (bool): Whether the input password matches the stored hashed password.
- **Description**:
    - This function hashes the input password using the stored salt and compares it with the stored hashed password. It returns `True` if they match, indicating the input password is correct, or `False` otherwise.

## Example Usage

The file includes a practical example demonstrating how to hash and verify passwords:

1. **Hashing a Password**:
    
    - The user is prompted to enter a password, which is then hashed using the `hash_password` function. The hashed password and the salt are displayed.
2. **Verifying a Password**:
    
    - The user is prompted to enter a password for verification. The `check_password` function is used to check if this entered password, when hashed with the previously generated salt, matches the stored hashed password. The result of this verification is displayed to the user.