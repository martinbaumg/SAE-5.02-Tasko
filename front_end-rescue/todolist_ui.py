# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todolist.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.taskLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.taskLineEdit.setGeometry(QtCore.QRect(310, 280, 191, 22))
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.addTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTaskButton.setGeometry(QtCore.QRect(80, 240, 161, 28))
        self.addTaskButton.setObjectName("addTaskButton")
        self.taskListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.taskListWidget.setGeometry(QtCore.QRect(10, 60, 311, 181))
        self.taskListWidget.setObjectName("taskListWidget")
        self.removeTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeTaskButton.setGeometry(QtCore.QRect(70, 270, 181, 28))
        self.removeTaskButton.setObjectName("removeTaskButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 111, 41))
        self.label.setObjectName("label")
        self.completedTaskListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.completedTaskListWidget.setGeometry(QtCore.QRect(490, 60, 301, 181))
        self.completedTaskListWidget.setObjectName("completedTaskListWidget")
        self.transferButton = QtWidgets.QPushButton(self.centralwidget)
        self.transferButton.setGeometry(QtCore.QRect(360, 200, 93, 28))
        self.transferButton.setObjectName("transferButton")
        self.removeCompletedButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeCompletedButton.setGeometry(QtCore.QRect(530, 270, 201, 28))
        self.removeCompletedButton.setObjectName("removeCompletedButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 40, 101, 16))
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(200, 310, 411, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTaskButton.setText(_translate("MainWindow", "Ajouter une tache"))
        self.removeTaskButton.setText(_translate("MainWindow", "Retirer une tache a faire"))
        self.label.setText(_translate("MainWindow", "Tasko"))
        self.transferButton.setText(_translate("MainWindow", "Transferer"))
        self.removeCompletedButton.setText(_translate("MainWindow", "retirer une tache terminé"))
        self.label_2.setText(_translate("MainWindow", "Tache a faire"))
        self.label_3.setText(_translate("MainWindow", "Tache terminé"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
