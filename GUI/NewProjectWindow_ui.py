# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProjectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl

import Project_Main_ui
import project_ui

class Ui_CreateNewProjectWindow(object):
    def openProjectTask(self):
        # open project task window
        self.window = QtWidgets.QMainWindow()
        self.ui = project_ui.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        # get the project name and url
        projectname = self.project_name_editText.text()
        url = self.url_editText.text()
        self.ui.lbl_pname.setText(projectname)
        # set the browser with the URL user has inputted
        self.ui.browser.setUrl(QUrl(url))
        self.ui.url_bar.setText(url)

    def closeProjectTask(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Project_Main_ui.Ui_Project_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def setupUi(self, CreateNewProjectWindow):
        CreateNewProjectWindow.setObjectName("CreateNewProjectWindow")
        CreateNewProjectWindow.resize(1091, 663)
        self.centralwidget = QtWidgets.QWidget(CreateNewProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 30, 961, 601))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.main_layout.setContentsMargins(100, 100, 100, 100)
        self.main_layout.setObjectName("main_layout")

        self.main_label_layout = QtWidgets.QVBoxLayout()
        self.main_label_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_label_layout.setObjectName("main_label_layout")

        self.main_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.main_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_label.sizePolicy().hasHeightForWidth())
        self.main_label.setSizePolicy(sizePolicy)
        self.main_label.setMinimumSize(QtCore.QSize(500, 70))
        self.main_label.setMaximumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.main_label.setFont(font)
        self.main_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_label.setObjectName("main_label")
        self.main_label_layout.addWidget(self.main_label)

        self.main_layout.addLayout(self.main_label_layout)

        self.project_name_layout = QtWidgets.QVBoxLayout()
        self.project_name_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.project_name_layout.setObjectName("project_name_layout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.project_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_name_label.setFont(font)
        self.project_name_label.setObjectName("project_name_label")
        self.horizontalLayout.addWidget(self.project_name_label)

        self.project_name_editText = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_name_editText.setFont(font)
        self.project_name_editText.setObjectName("project_name_editText")
        self.horizontalLayout.addWidget(self.project_name_editText)
        self.project_name_layout.addLayout(self.horizontalLayout)

        self.main_layout.addLayout(self.project_name_layout)

        self.url_layout = QtWidgets.QVBoxLayout()
        self.url_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.url_layout.setObjectName("url_layout")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.url_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.horizontalLayout_3.addWidget(self.url_label)

        self.url_editText = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_editText.setFont(font)
        self.url_editText.setObjectName("url_editText")
        self.horizontalLayout_3.addWidget(self.url_editText)

        self.url_layout.addLayout(self.horizontalLayout_3)
        self.main_layout.addLayout(self.url_layout)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.buttons_layout.setObjectName("buttons_layout")

        self.create_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.buttons_layout.addWidget(self.create_button)
        #called the function and close the old window
        self.create_button.clicked.connect(lambda: self.openProjectTask())
        self.create_button.clicked.connect(lambda: CreateNewProjectWindow.close())

        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.buttons_layout.addWidget(self.cancel_button)

        self.cancel_button.clicked.connect(lambda: self.closeProjectTask())
        self.cancel_button.clicked.connect(lambda: CreateNewProjectWindow.close())

        self.main_layout.addLayout(self.buttons_layout)

        self.centralwidget.setLayout(self.main_layout)
        CreateNewProjectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateNewProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateNewProjectWindow)

    def retranslateUi(self, CreateNewProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateNewProjectWindow.setWindowTitle(_translate("CreateNewProjectWindow", "MainWindow"))
        self.main_label.setText(_translate("CreateNewProjectWindow", "Create New Project"))
        self.project_name_label.setText(_translate("CreateNewProjectWindow", "Project Name:"))
        self.url_label.setText(_translate("CreateNewProjectWindow", "URL:"))
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
