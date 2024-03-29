# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from GUI.Projects import all_projects_ui
from GUI.Projects import project_ui
from Database import crud


class Ui_CreateNewProjectWindow(object):
    def openProjectTask(self):
        # get the project name and url
        projectname = self.project_name_editText.text()
        url = self.url_editText.text()
        url2 = self.url_editText2.text()
        if projectname != "" and url != "":
            # open project task window
            self.window = QtWidgets.QMainWindow()
            self.ui = project_ui.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            crud.create_project(self.label_hidden.text(), projectname, url, url2)
            self.ui.lbl_pname.setText(projectname)
            if url2 != "":
                self.ui.tableWidget.setRowCount(4)
            else:
                self.ui.tableWidget.setRowCount(2)
            # set the browser with the URL user has inputted
            self.ui.browser.setUrl(QUrl(url))
            self.ui.url_bar.setText(url)

            self.ui.browser_2.setUrl(QUrl(url2))
            self.ui.url_bar_2.setText(url2)

            print("userId-newproject ", self.label_hidden.text())

    def main_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = all_projects_ui.Ui_Project_Main()
        self.ui.setupUi(self.window)
        # passed the user id back to main menu
        self.ui.userId_label.setText(self.label_hidden.text())
        self.window.show()

    def setupUi(self, CreateNewProjectWindow):
        CreateNewProjectWindow.setObjectName("CreateNewProjectWindow")
        CreateNewProjectWindow.resize(902, 605)
        self.centralwidget = QtWidgets.QWidget(CreateNewProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(11, 11, 11, 11)
        self.main_layout.setObjectName("main_layout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.main_layout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_name_label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_name_label.setFont(font)
        self.project_name_label.setObjectName("project_name_label")
        self.horizontalLayout_2.addWidget(self.project_name_label)
        self.project_name_editText = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_name_editText.setFont(font)
        self.project_name_editText.setObjectName("project_name_editText")
        self.horizontalLayout_2.addWidget(self.project_name_editText)
        self.main_layout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.url_label = QtWidgets.QLabel(self.widget_3)
        self.url_label.setMinimumSize(QtCore.QSize(0, 50))
        self.url_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.verticalLayout_4.addWidget(self.url_label)
        self.url_editText = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_editText.setFont(font)
        self.url_editText.setObjectName("url_editText")
        self.verticalLayout_4.addWidget(self.url_editText)
        self.url_editText2 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_editText2.setFont(font)
        self.url_editText2.setObjectName("url_label2")
        self.verticalLayout_4.addWidget(self.url_editText2)
        self.main_layout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_button = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout.addWidget(self.create_button)
        self.cancel_button = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.main_layout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.main_layout)
        CreateNewProjectWindow.setCentralWidget(self.centralwidget)

        self.label_hidden = QtWidgets.QLabel(self.widget_4)
        self.horizontalLayout.addWidget(self.label_hidden)
        self.label_hidden.setHidden(True)

        # called the function and close the old window
        self.create_button.clicked.connect(lambda: self.openProjectTask())
        self.create_button.clicked.connect(lambda: CreateNewProjectWindow.close())
        self.cancel_button.clicked.connect(lambda: self.main_menu())

        self.retranslateUi(CreateNewProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateNewProjectWindow)

        self.retranslateUi(CreateNewProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateNewProjectWindow)

    def retranslateUi(self, CreateNewProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateNewProjectWindow.setWindowTitle(_translate("CreateNewProjectWindow", "MainWindow"))
        self.label.setText(_translate("CreateNewProjectWindow", "Create New Project"))
        self.project_name_label.setText(_translate("CreateNewProjectWindow", "Project Name:"))
        self.url_label.setText(_translate("CreateNewProjectWindow", "URL (user can input 2 URLs):"))
        self.create_button.setText(_translate("CreateNewProjectWindow", "Create"))
        self.cancel_button.setText(_translate("CreateNewProjectWindow", "Cancel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CreateNewProjectWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateNewProjectWindow()
    ui.setupUi(CreateNewProjectWindow)
    CreateNewProjectWindow.show()
    sys.exit(app.exec_())
