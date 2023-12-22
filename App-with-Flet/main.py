import time
import flet as ft
import bcrypt 

# import logging
# logging.basicConfig(level=logging.DEBUG)

import mysql.connector as mysql
from mysql.connector import Error

logged_in_user_id = None


class DatabaseConnection:
    def __init__(self):
        self.host = "45.154.99.10"
        self.database = "tasko"
        self.user = "admin"
        self.password = "48wGK#t0:ZOx9c"
        self.connection = None
        self.cursor = None

    def get_connection(self):
        try:
            connection = mysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                connect_timeout=100,
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def execute_query(self, query, values, return_lastrowid=False):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            print(f"Executing query: {query} with values {values}")
            cursor.execute(query, values)
            conn.commit()
            print("Query committed successfully.")
            if return_lastrowid:
                return cursor.lastrowid  # Return the last inserted row ID
            return cursor.rowcount > 0  # True if rows were affected
        except Exception as e:
            print(f"Query execution error: {e}")
            conn.rollback()
            print("Query rolled back due to error.")
            return False
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed.")

    def execute_select_query(self, query, values):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            print(f"Executing select query: {query} with values {values}")
            cursor.execute(query, values)
            result = cursor.fetchall()  # Fetch all results
            return result
        except Exception as e:
            print(f"Select query execution error: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed for select query.")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None  # Set to None after closing
            print("MySQL Database connection closed")

# Example usage
if __name__ == "__main__":
    db = DatabaseConnection()
    connection = db.get_connection()
    if connection:
        # Perform database operations here
        db.disconnect()



class ToDO(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.main_container = ft.Ref[ft.Column]()
        self.tasks_view = ft.Ref[ft.Column]()
        self.text_field = ft.Ref[ft.TextField]()
        self.tabs = ft.Ref[ft.Tabs]()
        self.delete_dialog = self.create_delete_dialog()
        self._actual_deleted_item = None

    def create_delete_dialog(self):
        return ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete this item?"),
            actions=[
                ft.TextButton("Yes", on_click=self.delete_confirmed),
                ft.TextButton("No", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def close_dialog(self, e):
        """when the 'No' button of the delete-dialog is triggered, the dialog is just closed"""
        self.delete_dialog.open = False
        e.page.update()

    def delete_confirmed(self, e):
        """
        when the 'Yes' button of the delete-dialog is triggered,
        the item is deleted and the delete-dialog is closed
        """
        self.delete_item_callback(self._actual_deleted_item)
        self.delete_dialog.open = False
        e.page.update()
        e.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Deleted Item successfully!"),
                action="OK!",
                open=True
            )
        )

    def open_delete_dialog(self, item):
        """opens the delete-dialog, and keeps a reference to the item which triggered it(self._actual_deleted_item)"""
        item.page.dialog = self.delete_dialog
        item.page.dialog.open = True
        self._actual_deleted_item = item
        item.page.update()

    def refresh_ui(self):
        self.update()

    def update(self):
        index = self.tabs.selected_index

        for todo_item_control in self.tasks_view.controls:
            # Check if the todo item and its checkbox are properly initialized
            if todo_item_control and todo_item_control.item_checkbox and todo_item_control.item_checkbox.current:
                checkbox_value = todo_item_control.item_checkbox.current.value
                # Update visibility based on the selected tab index
                todo_item_control.visible = (index == 0 or
                                            (index == 1 and not checkbox_value) or
                                            (index == 2 and checkbox_value))
            else:
                print("Checkbox or todo item not properly initialized")

        super().update()

    def delete_item_callback(self, item):
        """
        It removes the item from the list of controls in the current view, and then updates the view
        :param item: The to-do item to be deleted
        """
        task_id = item.task_id
        method_list = MethodList()
        if method_list.delete_task(task_id):
            self.tasks_view.controls.remove(item)  # Directly access controls
            self.update()
        else:
            print(f"Failed to delete task with id {task_id}.")
    
    def submit_item(self, e: ft.ControlEvent):
        """
        It creates a new TodoItem object, adds it to the list of controls in the tasks_view(below the tabs),
        and then clears the text field

        :param e: The event object (ControlEvent)
        """
        global logged_in_user_id
        task_name = self.text_field.value  # Accessing the value directly
        task_description = "Your default description"  # Replace with actual input from user
        task_due_date = "2023-01-01"  # Replace with actual input from user (YYYY-MM-DD format)

        if task_name and logged_in_user_id is not None:
            method_list = MethodList()
            if method_list.add_task(task_name, task_description, task_due_date, logged_in_user_id):
                self.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text("Task added successfully"),
                        action="OK",
                        open=True
                    )
                )
                self.refresh_tasks()
            else:
                self.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text("Failed to add task"),
                        action="OK",
                        open=True
                    )
                )

            self.text_field.value = ""
            e.page.update()

    def clear_and_reload_tasks(self):
        # Clear existing tasks
        self.tasks_view.current.controls.clear()

        # Reload tasks from the database
        self.load_tasks()
        self.update()
        
    def refresh_tasks(self):
        """ Clear and reload tasks """
        self.tasks_view.controls.clear()  # Accessing controls directly
        self.load_tasks()

    def tabs_change(self, e):
        """
        It updates the UI when the user changes tabs

        :param e: The event object (ControlEvent)
        """
        self.update()

    def counter_text_change(self, e: ft.ControlEvent):
        """
        It updates the counter text of the text field.

        :param e: The event object (ControlEvent)
        """
        self.text_field.counter_text = f'{len(e.data)} chars'
        self.text_field.update()

    def logout(self, e):
        """ Log out the current user and show the login page. """
        global logged_in_user_id
        logged_in_user_id = None
        show_login_page()

    def build(self):
        self.text_field = ft.TextField(
            helper_text="What do you plan to do?",
            hint_text="ex: learn flutter..",
            counter_text='0 chars',
            keyboard_type=ft.KeyboardType.TEXT,
            label="New Item",
            expand=True,
            text_size=20,
            tooltip="Field for new items",
            prefix_icon=ft.icons.LIST_ALT_ROUNDED,
            autofocus=True,
            on_change=self.counter_text_change,
            on_submit=self.submit_item
        )
        
        self.tasks_view = ft.Column(scroll=ft.ScrollMode.ALWAYS)
        
        self.tabs = ft.Tabs(
            tabs=[
                ft.Tab(text='all', icon=ft.icons.CHECKLIST_OUTLINED),
                ft.Tab(text='not yet done', icon=ft.icons.CHECK),
                ft.Tab(text='done', icon=ft.icons.DONE_ALL)
            ],
            selected_index=0,
            on_change=self.tabs_change
        )

        logout_button = ft.ElevatedButton(
            text="Logout",
            on_click=self.logout
        )

        # Reconstruct the main container with logout button
        self.main_container = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        logout_button,
                        self.text_field,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD,
                            tooltip="add item",
                            on_click=self.submit_item
                        )
                    ]
                ),
                self.tabs,
                self.tasks_view
            ],
            spacing=24,
            width=630
        )

        return self.main_container  # Return the main container directly

    def load_tasks(self):
        global logged_in_user_id
        if logged_in_user_id is not None:
            method_list = MethodList()
            tasks = method_list.fetch_tasks(logged_in_user_id)
            if tasks:
                self.tasks_view.controls.clear()
                for task in tasks:
                    task_id, task_name, task_description, task_due_date = task
                    formatted_date = task_due_date.strftime("%Y-%m-%d") if task_due_date else ""
                    todo_item = TodoItem(task_id, task_name, task_description, formatted_date, self, self.update, self.open_delete_dialog)
                    self.tasks_view.controls.append(todo_item)
                self.update()
            else:
                print("No tasks found for the current user.")
        else:
            print("No logged-in user.")

class TodoItem(ft.UserControl):
    def __init__(self, task_id, item_text, item_description, item_due_date, todo_page_instance, checkbox_change, delete_dialog_callback):
        """
        The function takes in three arguments: item_text, checkbox_change, and delete_callback. It then calls the
        super() function, which is a special function that allows you to call a method from the parent class.

        :param item_text: The text that will be displayed in the item
        :param checkbox_change: This is a callback function that will be called when the value of checkbox changes
        :param delete_dialog_callback: This is a function that will be called when the delete button of an item is pressed
        """
        super().__init__()
        self.task_id = task_id
        self.item_text = item_text
        self.item_description = item_description
        self.item_due_date = item_due_date
        self.todo_page_instance = todo_page_instance  # Reference to ToDO instance
        self.open_delete_dialog = delete_dialog_callback
        self.checkbox_change = checkbox_change
        self.normal_view = ft.Ref[ft.Row]()
        self.edit_view = ft.Ref[ft.Row]()
        self.item_checkbox = ft.Ref[ft.Checkbox]()
        self.text_field = ft.Ref[ft.TextField]()
        self.description_field = ft.Ref[ft.TextField]()
        self.due_date_field = ft.Ref[ft.TextField]()

    def copy_item(self, e):
        """
        Copies Text of to-do Item to clipboard.

        :param e: The event that triggered this function (ControlEvent)
        """
        e.page.set_clipboard(self.item_checkbox.current.label)
        e.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Content copied to Clipboard!"),
                action="OK!",
                open=True
            )
        )

    def edit_item(self, e):
        # Populate edit fields with current data
        self.text_field.current.value = self.item_text
        self.description_field.current.value = self.item_description
        self.due_date_field.current.value = self.item_due_date
        self.normal_view.current.visible = False
        self.edit_view.current.visible = True
        self.text_field.current.autofocus = True
        self.update()

    def save_edit(self, e):
        # Gather updated data
        updated_name = self.text_field.current.value
        updated_description = self.description_field.current.value
        updated_due_date = self.due_date_field.current.value

        # Update task in database
        method_list = MethodList()
        if method_list.update_task(self.task_id, updated_name, updated_description, updated_due_date):
            # Show success message and refresh task list
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Task updated successfully!"), action="OK!", open=True))
            self.todo_page_instance.refresh_tasks()
        else:
            # Show error message
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Failed to update task!"), action="OK!", open=True))

        # Close edit view and open normal view
        self.normal_view.current.visible = True
        self.edit_view.current.visible = False
        self.update()

    def delete_item(self, e):
        """
        It calls the delete_callback function which will delete/remove this item from the to-do listbox(tasks_view)

        :param e: The event that triggered the callback (ControlEvent)
        """
        self.open_delete_dialog(self)

    def item_checkbox_value_change(self, e):
        """
        Listens to changes on the value(bool) of our checkbox.
        For any change, we update the UI to correctly show the Item in the corresponding tab.

        :param e: The event object (ControlEvent)
        """
        self.checkbox_change()

    def build(self):
        """
        Building up of the UI for a To-Do Item.

                            Row(Checkbox and a Row with two IconButtons)
        :return: Column --<
                            Row (Textfield and an Update button)
        """
        return ft.Column(
            controls=[
                ft.Row(
                    ref=self.normal_view,
                    controls=[
                        ft.Checkbox(
                            ref=self.item_checkbox,
                            label=self.item_text,
                            value=False,
                            on_change=self.item_checkbox_value_change),
                        ft.Text(self.item_description),  # Display the description
                        ft.Text(self.item_due_date if self.item_due_date else ""),  # Directly display the due date string
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.COPY,
                                    icon_color=ft.colors.BLUE,
                                    tooltip="copy",
                                    on_click=self.copy_item,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color=ft.colors.LIGHT_GREEN_ACCENT_700,
                                    on_click=self.edit_item,
                                    tooltip="update item",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_FOREVER,
                                    icon_color=ft.colors.RED_900,
                                    tooltip="delete item",
                                    on_click=self.delete_item,
                                ),
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    ref=self.edit_view,
                    visible=False,
                    controls=[
                        ft.TextField(
                            ref=self.text_field,
                            value=self.item_text,
                            tooltip="field to edit the item",
                            autofocus=False,
                            label="Edit Item",
                            expand=True,
                            on_submit=self.save_edit,
                            suffix=ft.ElevatedButton(text="Update", on_click=self.save_edit)),
                            ft.TextField(
                                ref=self.description_field,
                                label="Description",
                                value=self.item_description,
                                expand=True
                            ),
                            ft.TextField(
                                ref=self.due_date_field,
                                label="Due Date",
                                value=self.item_due_date,
                                expand=True
                            )
                    ],
                )
            ],
        )

class RequestList:
    @staticmethod
    def add_user(mail, name, hashed_password, salt):
        rights_id = 1  # Assuming a default rights_id for simplicity

        # Use query parameters to avoid SQL injection attacks
        query = "INSERT INTO USER (mail, password, name, rights_id, salt) VALUES (%s, %s, %s, %s, %s)"

        # Pass the values as a tuple for the query parameters
        values = (mail, hashed_password, name, rights_id, salt)

        return query, values

    @staticmethod
    def authenticate_user(mail):
        return "SELECT password, salt FROM USER WHERE mail = %s", (mail,)
    
class MethodList:
    def __init__(self):
        self.db = DatabaseConnection()

    def register_user(self, mail, name, password):
        self.db.get_connection()
        try:
            # Hash the password
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Convert hash and salt to strings
            salt_str = salt.decode('utf-8')
            hashed_password_str = hashed_password.decode('utf-8')

            # Prepare and execute the query
            query, values = RequestList.add_user(mail, name, hashed_password_str, salt_str)
            
            # Log the query and values
            print(f"Attempting to register user with query: {query} and values: {values}")

            result = self.db.execute_query(query, values)
            if result is not None:
                print("User registered successfully.")
                print(f"Result: {result}")
            else:
                print("User registration failed - no result returned from the query.")
        except Exception as e:
            print(f"Error occurred during user registration: {e}")
        finally:
            self.db.disconnect()


    def login_user(self, mail, password):
        self.db.get_connection()
        query, values = RequestList.authenticate_user(mail)
        result = self.db.execute_select_query(query, values)
        if result:
            stored_password, salt = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Fetch user ID here
                query = "SELECT id FROM USER WHERE mail = %s"
                user_id_result = self.db.execute_select_query(query, (mail,))
                user_id = user_id_result[0][0] if user_id_result else None
                self.db.disconnect()
                print(f"User with id {user_id} logged in successfully.")
                return True, user_id
            else:
                print("Incorrect password.")
                self.db.disconnect()
                return False, None
        else:
            print("User not found.")
            self.db.disconnect()
            return False, None
    
    def fetch_tasks(self, user_id):
        self.db.get_connection()
        try:
            query = """
                SELECT TASK.id, TASK.name, TASK.description, TASK.due_date
                FROM TASK
                JOIN TASK_USER ON TASK.id = TASK_USER.task_id
                WHERE TASK_USER.user_id = %s
            """
            values = (user_id,)
            tasks = self.db.execute_select_query(query, values)
            return tasks
        except Exception as e:
            print(f"Error occurred during tasks fetch: {e}")
            return []
        finally:
            self.db.disconnect()
    
    def delete_task(self, task_id):
        self.db.get_connection()
        try:
            # First, delete the task from TASK_USER
            task_user_query = "DELETE FROM TASK_USER WHERE task_id = %s"
            task_user_values = (task_id,)
            if not self.db.execute_query(task_user_query, task_user_values):
                print(f"Failed to delete task-user linkage for task id {task_id}.")
                return False

            # Then, delete the task from TASK
            task_query = "DELETE FROM TASK WHERE id = %s"
            task_values = (task_id,)

            if self.db.execute_query(task_query, task_values):
                print(f"Task with id {task_id} deleted successfully.")
                return True
            else:
                print(f"Failed to delete task with id {task_id}.")
                return False
        except Exception as e:
            print(f"Error occurred during task deletion: {e}")
            return False
        finally:
            self.db.disconnect()
                
    def update_task(self, task_id, name, description, due_date):
        self.db.get_connection()
        try:
            query = "UPDATE TASK SET name = %s, description = %s, due_date = %s WHERE id = %s"
            values = (name, description, due_date, task_id)
            result = self.db.execute_query(query, values)
            return result  # This should be True if the update is successful
        except Exception as e:
            print(f"Error occurred during task update: {e}")
            return False
        finally:
            self.db.disconnect()

    def add_task(self, name, description, due_date, user_id):
        self.db.get_connection()
        try:
            # Insert into TASK
            task_query = "INSERT INTO TASK (name, description, due_date) VALUES (%s, %s, %s)"
            task_values = (name, description, due_date)
            task_result = self.db.execute_query(task_query, task_values, return_lastrowid=True)
            
            if task_result:
                task_id = task_result

                # Insert into TASK_USER
                task_user_query = "INSERT INTO TASK_USER (task_id, user_id) VALUES (%s, %s)"
                task_user_values = (task_id, user_id)
                self.db.execute_query(task_user_query, task_user_values)

                return True
            else:
                return False
        except Exception as e:
            print(f"Error occurred during task addition: {e}")
            return False
        finally:
            self.db.disconnect()


class LoginPage(ft.UserControl):
    def __init__(self, on_login_success, on_signup_page):
        super().__init__()
        self.email_input = ft.Ref[ft.TextField]()
        self.password_input = ft.Ref[ft.TextField]()
        self.on_login_success = on_login_success
        self.on_signup_page = on_signup_page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(ref=self.email_input, hint_text="Email"),
                ft.TextField(ref=self.password_input, hint_text="Password", password=True),
                ft.ElevatedButton(text="Login", on_click=self.on_login_click),
                ft.TextButton(
                    "Don't have an account? Sign up here",
                    on_click=lambda e: self.on_signup_page()
                )
            ],
            spacing=10
        )
    
    def on_login_click(self, e):
        email = self.email_input.current.value
        password = self.password_input.current.value
        method_list = MethodList()
        login_success, user_id = method_list.login_user(email, password)
        if login_success:
            global logged_in_user_id
            logged_in_user_id = user_id
            self.on_login_success()
        else:
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Login failed!"), action="OK!", open=True))

class SignupPage(ft.UserControl):
    def __init__(self, on_login_page):
        super().__init__()
        self.on_login_page = on_login_page
        self.email_input = ft.Ref[ft.TextField]()
        self.name_input = ft.Ref[ft.TextField]()
        self.password_input = ft.Ref[ft.TextField]()
        self.confirm_password_input = ft.Ref[ft.TextField]()

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Signup", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(ref=self.email_input, hint_text="Email"),
                ft.TextField(ref=self.name_input, hint_text="Name"),
                ft.TextField(ref=self.password_input, hint_text="Password", password=True),
                ft.TextField(ref=self.confirm_password_input, hint_text="Confirm Password", password=True),
                ft.ElevatedButton(text="Signup", on_click=self.on_signup_click),
                ft.TextButton(
                    "Already have an account? Login here",
                    on_click=lambda e: self.on_login_page()
                )
            ],
            spacing=10
        )

    def on_signup_click(self, e):
        email = self.email_input.current.value
        name = self.name_input.current.value
        password = self.password_input.current.value
        confirm_password = self.confirm_password_input.current.value
        if password == confirm_password:
            MethodList().register_user(email, name, password)
            self.on_login_page()
        else:
            print("Passwords do not match.")


def main(page: ft.Page):
    global show_todo_page, show_login_page, show_signup_page
    page.title = "myToDo App"
    page.window_width = 562
    page.window_height = 720
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.fonts = {
        "SF-simple": "/fonts/San-Francisco/SFUIDisplay-Light.ttf",
        "SF-bold": "/fonts/San-Francisco/SFUIDisplay-Bold.ttf"
    }
    page.theme_mode = "light"
    page.theme = ft.Theme(
        font_family="SF-simple",
        use_material3=True,
        visual_density=ft.ThemeVisualDensity.COMPACT,
    )

    def show_todo_page():
        global todo_page
        try:
            todo_page = ToDO()
            if todo_page is not None:
                page.controls.clear()
                page.add(todo_page)
                todo_page.load_tasks()
            else:
                print("Error: todo_page is None.")
        except Exception as e:
            print(f"Error in show_todo_page: {e}")

    def show_login_page():
        login_page = LoginPage(on_login_success=show_todo_page, on_signup_page=show_signup_page)
        page.controls.clear()
        page.add(login_page)

    def show_signup_page():
        signup_page = SignupPage(on_login_page=show_login_page)
        page.controls.clear()
        page.add(signup_page)

    # login_page = LoginPage(on_login_success=show_todo_page)
    # signup_page = SignupPage(show_login_page)  # Pass show_login_page here
    # todo_page = ToDO()

    show_login_page()

# running the app
ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")