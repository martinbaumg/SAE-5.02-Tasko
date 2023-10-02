import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets
import sys
import os
import random
import database_connection as db

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # Créez une instance de DatabaseConnection
        self.db = db.DatabaseConnection()

        self.text = QtWidgets.QLabel("")

        # Bouton pour se connecter à la base de données
        self.connect_button = QtWidgets.QPushButton("Connect to database")
        self.connect_button.clicked.connect(self.connect_to_database)

        # Bouton pour se déconnecter de la base de données
        self.disconnect_button = QtWidgets.QPushButton("Disconnect from database")
        self.disconnect_button.clicked.connect(self.disconnect_from_database)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.connect_button)
        self.layout.addWidget(self.disconnect_button)

    @QtCore.Slot()
    def connect_to_database(self):
        # Essayez de vous connecter à la base de données
        self.db.connect()
        
        # Vérifiez si la connexion est établie
        if self.db.connection.is_connected():
            self.connect_button.setText("Connected to database")
        else:
            self.connect_button.setText("Failed to connect")

    @QtCore.Slot()
    def disconnect_from_database(self):
        # Essayez de vous déconnecter de la base de données
        self.db.disconnect()
        self.connect_button.setText("Connect to database")

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
