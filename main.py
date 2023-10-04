import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from todolist_ui import Ui_MainWindow


class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addTaskButton.clicked.connect(self.add_task)
        self.ui.removeTaskButton.clicked.connect(self.remove_task)
        self.ui.transferButton.clicked.connect(self.transfer_task)
        self.ui.removeCompletedButton.clicked.connect(self.remove_completed_task)


        self.tasks = []
        self.completed_tasks = []

    def add_task(self):
        task_text = self.ui.taskLineEdit.text()
        if task_text:
            self.tasks.append(task_text)
            self.ui.taskListWidget.addItem(task_text)
            self.ui.taskLineEdit.clear()

    def remove_task(self):
        selected_item = self.ui.taskListWidget.currentItem()
        if selected_item:
            task_text = selected_item.text()
            self.tasks.remove(task_text)
            self.ui.taskListWidget.takeItem(self.ui.taskListWidget.row(selected_item))
        else:
            QMessageBox.warning(self, "Avertissement", "Sélectionnez une tâche à supprimer.")
    def transfer_task(self):
        selected_item = self.ui.taskListWidget.currentItem()
        if selected_item:
            task_text = selected_item.text()
            self.tasks.remove(task_text)
            self.ui.taskListWidget.takeItem(self.ui.taskListWidget.row(selected_item))
            self.completed_tasks.append(task_text)
            self.ui.completedTaskListWidget.addItem(task_text)
        else:
            QMessageBox.warning(self, "Avertissement", "Sélectionnez une tâche à transférer.")

    def remove_completed_task(self):
        selected_item = self.ui.completedTaskListWidget.currentItem()
        if selected_item:
            task_text = selected_item.text()
            self.completed_tasks.remove(task_text)
            self.ui.completedTaskListWidget.takeItem(self.ui.completedTaskListWidget.row(selected_item))
        else:
            QMessageBox.warning(self, "Avertissement", "Sélectionnez une tâche à supprimer.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec())
