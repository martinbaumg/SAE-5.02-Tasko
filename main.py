import time
import flet as ft
import bcrypt 
import database_connection

# import logging
# logging.basicConfig(level=logging.DEBUG)

import mysql.connector as mysql
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.host = "45.154.99.10"
        self.database = "tasko"
        self.user = "admin"
        self.password = "48wGK#t0:ZOx9c"

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

    def execute_query(self, query, values):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            print(f"Executing query: {query} with values {values}")  # Log the query and parameters
            cursor.execute(query, values)
            conn.commit()  # Commit the transaction
            print("Query committed successfully.")  # Log the commit
            if cursor.rowcount > 0:
                return True  # Rows were affected, indicating success
            else:
                return False  # No rows were affected
        except Exception as e:
            print(f"Query execution error: {e}")
            conn.rollback()  # Rollback in case of error
            print("Query rolled back due to error.")  # Log the rollback
            return False  # Indicate failure            
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed.")  # Log the connection close

    def disconnect(self, connection):
        if connection and connection.is_connected():
            connection.close()
            print("MySQL Database connection closed")

# Example usage
if __name__ == "__main__":
    db = DatabaseConnection()
    connection = db.get_connection()
    if connection:
        # Perform database operations here
        db.disconnect(connection)



class ToDO(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.main_container = None
        self.tasks_view = None
        self.text_field = None
        self.tabs = None
        self.delete_dialog = ft.AlertDialog(
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

        # the item which caused the opening of the delete-dialog box
        self._actual_deleted_item = None

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

    def update(self):
        """
        The update function is called when the user changes tabs.
        It hides or shows the to-do items depending on which tab is selected.
        """
        # index 0 refers to 'all' tab, index 1 refers to 'not yet done' tab, index 2 refers to 'done' tab,
        index = self.tabs.current.selected_index

        # Looping through the list of controls in the tasks_view, and then setting the visibility of each control
        # to True or False depending on the selected tab(precisely, it's index).
        for todo_item_control in self.tasks_view.current.controls:
            if index == 1:
                # show tasks that have not yet been done
                todo_item_control.visible = not todo_item_control.item_checkbox.current.value
            elif index == 2:
                # show tasks that have already been done
                todo_item_control.visible = todo_item_control.item_checkbox.current.value
            else:
                # show all tasks
                todo_item_control.visible = True
        super().update()

    def delete_item_callback(self, item):
        """
        It removes the item from the list of controls in the current view, and then updates the view

        :param item: The to-do item to be deleted
        """
        self.tasks_view.current.controls.remove(item)
        self.update()

    def submit_item(self, e: ft.ControlEvent):
        """
        It creates a new TodoItem object, adds it to the list of controls in the tasks_view(below the tabs),
        and then clears the text field

        :param e: The event object (ControlEvent)
        """
        if self.text_field.current.value:
            item = TodoItem(self.text_field.current.value, self.update, self.open_delete_dialog)
            self.tasks_view.current.controls.append(item)
            self.text_field.current.value = ""
            self.text_field.current.counter_text = '0 chars'
            self.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Added New To-Do Item"),
                    action="OK!",
                    open=True
                )
            )
            self.update()

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
        self.text_field.current.counter_text = f'{len(e.data)} chars'
        self.text_field.current.update()

    def build(self):
        """
        It builds the UI with a maximum width of 600px.
        :return: A Column widget with a Row widget and a Tabs widget as its children.
        """
        self.text_field = ft.Ref[ft.TextField]()
        self.tasks_view = ft.Ref[ft.Column]()
        self.main_container = ft.Ref[ft.Column]()
        self.tabs = ft.Ref[ft.Tabs]()

        return ft.Column(ref=self.main_container,
                         controls=[
                             ft.Row(
                                 controls=[
                                     ft.TextField(
                                         ref=self.text_field,
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
                                     ),
                                     ft.FloatingActionButton(
                                         icon=ft.icons.ADD,
                                         tooltip="add item",
                                         on_click=self.submit_item
                                     )
                                 ]
                             ),
                             ft.Tabs(
                                 ref=self.tabs,
                                 tabs=[
                                     ft.Tab(text='all', icon=ft.icons.CHECKLIST_OUTLINED),
                                     ft.Tab(text='not yet done', icon=ft.icons.CHECK),
                                     ft.Tab(text='done', icon=ft.icons.DONE_ALL)
                                 ],
                                 selected_index=0,
                                 on_change=self.tabs_change
                             ),
                             ft.Column(
                                 ref=self.tasks_view,
                                 scroll=ft.ScrollMode.ALWAYS
                             )
                         ],
                         spacing=24,
                         width=630
                         )


class TodoItem(ft.UserControl):
    def __init__(self, item_text, checkbox_change, delete_dialog_callback):
        """
        The function takes in three arguments: item_text, checkbox_change, and delete_callback. It then calls the
        super() function, which is a special function that allows you to call a method from the parent class.

        :param item_text: The text that will be displayed in the item
        :param checkbox_change: This is a callback function that will be called when the value of checkbox changes
        :param delete_dialog_callback: This is a function that will be called when the delete button of an item is pressed
        """
        super().__init__()
        self.item_text = item_text
        self.open_delete_dialog = delete_dialog_callback
        self.checkbox_change = checkbox_change
        self.normal_view = ft.Ref[ft.Row]()
        self.edit_view = ft.Ref[ft.Row]()
        self.item_checkbox = ft.Ref[ft.Checkbox]()
        self.text_field = ft.Ref[ft.TextField]()

    def save_edit(self, e):
        """
        It makes the normal_view visible, the edit_view invisible and sets the
        label of the checkbox to the value from the text field in the edit_view

        :param e: The event that triggered the function (ControlEvent)
        """
        self.normal_view.current.visible = True
        self.edit_view.current.visible = False
        self.text_field.current.autofocus = False
        self.item_checkbox.current.label = self.text_field.current.value
        # It updates the UI.
        self.update()
        e.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Updated Item successfully!"),
                action="OK!",
                open=True
            )
        )

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
        """
        Changes the view to an editable view. By setting the normal_view to invisible, and the edit_view to visible.

        :param e: The event that triggered this function (ControlEvent)
        """
        self.normal_view.current.visible = False
        self.edit_view.current.visible = True
        self.text_field.current.autofocus = True
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
                            suffix=ft.ElevatedButton(text="Update", on_click=self.save_edit))
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
        self.db = database_connection.DatabaseConnection()

    def register_user(self, mail, name, password):
        self.db.connect()
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
            else:
                print("User registration failed - no result returned from the query.")
        except Exception as e:
            print(f"Error occurred during user registration: {e}")
        finally:
            self.db.disconnect()


    def login_user(self, mail, password):
        self.db.connect()
        query, values = RequestList.authenticate_user(mail)
        result = self.db.execute_query(query, values)
        login_success = False
        if result:
            stored_password, salt = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                print("Login successful.")
                login_success = True
            else:
                print("Invalid password.")
        else:
            print("User not found.")
        self.db.disconnect()
        return login_success


class LoginPage(ft.UserControl):
    def __init__(self, on_login_success):
        super().__init__()
        self.email_input = ft.Ref[ft.TextField]()
        self.password_input = ft.Ref[ft.TextField]()
        self.on_login_success = on_login_success

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(ref=self.email_input, hint_text="Email"),
                ft.TextField(ref=self.password_input, hint_text="Password", password=True),
                ft.ElevatedButton(text="Login", on_click=self.on_login_click)
            ],
            spacing=10
        )

    def on_login_click(self, e):
        email = self.email_input.current.value
        password = self.password_input.current.value
        method_list = MethodList()
        if method_list.login_user(email, password):
            self.on_login_success()
        else:
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Login failed!"), action="OK!", open=True))

class SignupPage(ft.UserControl):
    def __init__(self):
        super().__init__()
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
                ft.ElevatedButton(text="Signup", on_click=self.on_signup_click)
            ],
            spacing=10
        )

    def on_signup_click(self, e):
        email = self.email_input.current.value
        name = self.name_input.current.value
        password = self.password_input.current.value
        confirm_password = self.confirm_password_input.current.value
        if password == confirm_password:
            method_list = MethodList()
            method_list.register_user(email, name, password)
            # You can add logic here to switch to the login page or ToDo page on successful registration
        else:
            print("Passwords do not match.")


def main(page: ft.Page):
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
        page.controls.clear()
        page.add(todo_page)

    def show_login_page():
        page.controls.clear()
        page.add(login_page)

    def show_signup_page():
        page.controls.clear()
        page.add(signup_page)

    login_page = LoginPage(on_login_success=show_todo_page)
    signup_page = SignupPage()
    todo_page = ToDO()

    show_signup_page()


# running the app
ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")