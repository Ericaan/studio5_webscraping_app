# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProjectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#go to project task window
from ex1url_ui import Ui_MainWindow


class Ui_CreateNewProjectWindow(object):
    def open_ex1(self):
        #open project task window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #get the project name and url
        projectname = self.name_editText.text()
        url = self.url_editText.text()
        self.ui.project_name.setText(projectname)
        self.ui.url.setText(url)

    def setupUi(self, CreateNewProjectWindow):
        CreateNewProjectWindow.setObjectName("CreateNewProjectWindow")
        CreateNewProjectWindow.resize(1091, 663)
        self.centralwidget = QtWidgets.QWidget(CreateNewProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(370, 50, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 170, 591, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)

        self.name_editText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_editText.setFont(font)
        self.name_editText.setObjectName("name_editText")
        self.horizontalLayout.addWidget(self.name_editText)

        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 270, 591, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.url_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.horizontalLayout_3.addWidget(self.url_label)

        self.url_editText = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.url_editText.setFont(font)
        self.url_editText.setObjectName("url_editText")
        self.horizontalLayout_3.addWidget(self.url_editText)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(330, 450, 419, 78))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.create_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_4.addWidget(self.create_button)
        self.create_button.clicked.connect(lambda :self.open_ex1())


        self.cancel_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)

        CreateNewProjectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateNewProjectWindow)
        self.name_editText.textChanged['QString'].connect(self.name_editText.setText)
        self.url_editText.textChanged['QString'].connect(self.url_editText.setText)
        QtCore.QMetaObject.connectSlotsByName(CreateNewProjectWindow)
        CreateNewProjectWindow.setTabOrder(self.create_button, self.cancel_button)

    def retranslateUi(self, CreateNewProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateNewProjectWindow.setWindowTitle(_translate("CreateNewProjectWindow", "MainWindow"))
        self.main_label.setText(_translate("CreateNewProjectWindow", "Create New Project"))
        self.name_label.setText(_translate("CreateNewProjectWindow", "Project Name:"))
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
