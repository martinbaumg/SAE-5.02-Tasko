import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from requests_list import RequestList
import database_connection

# Import your RequestList class here


class LoginSignupApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login / Signup")
        self.setGeometry(100, 100, 400, 200)

        self.login_ui()
        self.signup_ui()

        self.show_login()

    def login_ui(self):
        self.login_label = QLabel("Login")
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")

        self.login_button.clicked.connect(self.login)

        login_layout = QVBoxLayout()
        login_layout.addWidget(self.login_label)
        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(self.login_button)

        login_widget = QWidget()
        login_widget.setLayout(login_layout)

        self.setCentralWidget(login_widget)

    def signup_ui(self):
        self.signup_label = QLabel("Signup")
        self.new_username_label = QLabel("New Username:")
        self.new_username_input = QLineEdit()
        self.new_password_label = QLabel("New Password:")
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(QLineEdit.Password)
        self.signup_button = QPushButton("Signup")

        self.signup_button.clicked.connect(self.signup)

        signup_layout = QVBoxLayout()
        signup_layout.addWidget(self.signup_label)
        signup_layout.addWidget(self.new_username_label)
        signup_layout.addWidget(self.new_username_input)
        signup_layout.addWidget(self.new_password_label)
        signup_layout.addWidget(self.new_password_input)
        signup_layout.addWidget(self.signup_button)

        signup_widget = QWidget()
        signup_widget.setLayout(signup_layout)

        self.setCentralWidget(signup_widget)

    def show_login(self):
        self.centralWidget().deleteLater()  # Remove the existing central widget
        self.login_ui()

    def show_signup(self):
        self.centralWidget().deleteLater()  # Remove the existing central widget
        self.signup_ui()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Use the get_user and check_password_match functions from RequestList
        user_query = RequestList.get_user(username)
        password_query = RequestList.check_password_match(username, password)

        # Execute the queries and check the results here
        # You need to interact with your database or server to verify the login

        # If login is successful, you can switch to another screen or perform actions
        # For now, we will just print messages
        print("Attempting login with username:", username)
        print("User query:", user_query)
        print("Password query:", password_query)

    def signup(self):
        new_username = self.new_username_input.text()
        new_password = self.new_password_input.text()

        # Use the add_user function from RequestList to create a new user
        add_user_query = RequestList.add_user(
            new_username, new_password, new_username, 1
        )

        # Execute the query to add a new user to your database or server
        # Make sure you have a database connection and cursor available
        # For example, if you're using MySQL:
        # cursor.execute(add_user_query)

        # Commit the changes to the databases
        # connection.commit()

        # If signup is successful, you can switch to another screen or perform actions
        # For now, we will just print a success message
        print("User signed up successfully with username:", new_username)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginSignupApp()
    window.show()
    sys.exit(app.exec_())
