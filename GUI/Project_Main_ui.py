# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from NewProjectWindow_ui import Ui_CreateNewProjectWindow

class Ui_Project_Main(object):
    # show new window
    def openNewProjectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateNewProjectWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Project_Main):
        Project_Main.setObjectName("Project_Main")
        Project_Main.resize(1089, 586)
        self.centralwidget = QtWidgets.QWidget(Project_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(32, 10, 1041, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.main_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setObjectName("main_layout")

        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.menu_layout.setSpacing(1)
        self.menu_layout.setObjectName("menu_layout")

        self.manual_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.manual_button.setMinimumSize(QtCore.QSize(250, 40))
        self.manual_button.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manual_button.setFont(font)
        self.manual_button.setObjectName("manual_button")
        self.menu_layout.addWidget(self.manual_button)

        self.dv_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dv_button.setMinimumSize(QtCore.QSize(250, 40))
        self.dv_button.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dv_button.setFont(font)
        self.dv_button.setObjectName("dv_button")
        self.menu_layout.addWidget(self.dv_button)

        self.account_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.account_button.setMinimumSize(QtCore.QSize(250, 40))
        self.account_button.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.account_button.setFont(font)
        self.account_button.setObjectName("account_button")
        self.menu_layout.addWidget(self.account_button)

        self.project_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.project_button.setMinimumSize(QtCore.QSize(250, 40))
        self.project_button.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_button.setFont(font)
        self.project_button.setObjectName("project_button")
        self.menu_layout.addWidget(self.project_button)

        self.logout_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.logout_button.setMinimumSize(QtCore.QSize(250, 40))
        self.logout_button.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName("logout_button")
        self.menu_layout.addWidget(self.logout_button)

        self.main_layout.addLayout(self.menu_layout)

        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_layout.addWidget(self.line)

        self.project_layout = QtWidgets.QVBoxLayout()
        self.project_layout.setContentsMargins(20, 20, 20, -1)
        self.project_layout.setObjectName("project_layout")

        self.newproject_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newproject_button.setMinimumSize(QtCore.QSize(120, 50))
        self.newproject_button.setMaximumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newproject_button.setFont(font)
        self.newproject_button.setObjectName("newproject_button")
        self.project_layout.addWidget(self.newproject_button)
        # when button is clicked, called the function to open next window and close the old one
        self.newproject_button.clicked.connect(lambda: self.openNewProjectWindow())
        self.newproject_button.clicked.connect(lambda: Project_Main.close())

        self.projects_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.projects_table.setGridStyle(QtCore.Qt.SolidLine)
        self.projects_table.setObjectName("projects_table")
        self.projects_table.setColumnCount(7)
        self.projects_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(6, item)
        self.projects_table.horizontalHeader().setCascadingSectionResizes(False)
        self.project_layout.addWidget(self.projects_table)

        self.main_layout.addLayout(self.project_layout)

        self.centralwidget.setLayout(self.main_layout)
        Project_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Project_Main)
        QtCore.QMetaObject.connectSlotsByName(Project_Main)

    def retranslateUi(self, Project_Main):
        _translate = QtCore.QCoreApplication.translate
        Project_Main.setWindowTitle(_translate("Project_Main", "MainWindow"))
        self.manual_button.setText(_translate("Project_Main", "Projects"))
        self.dv_button.setText(_translate("Project_Main", "Data Visualisation"))
        self.account_button.setText(_translate("Project_Main", "Instruction Manual"))
        self.project_button.setText(_translate("Project_Main", "My Account"))
        self.logout_button.setText(_translate("Project_Main", "Log out"))
        self.newproject_button.setText(_translate("Project_Main", "New Project"))
        item = self.projects_table.verticalHeaderItem(0)
        item.setText(_translate("Project_Main", "1"))
        item = self.projects_table.verticalHeaderItem(1)
        item.setText(_translate("Project_Main", "2"))
        item = self.projects_table.verticalHeaderItem(2)
        item.setText(_translate("Project_Main", "3"))
        item = self.projects_table.horizontalHeaderItem(0)
        item.setText(_translate("Project_Main", "Project Name"))
        item = self.projects_table.horizontalHeaderItem(1)
        item.setText(_translate("Project_Main", "Last Edit"))
        item = self.projects_table.horizontalHeaderItem(2)
        item.setText(_translate("Project_Main", "Data Extracted"))
        item = self.projects_table.horizontalHeaderItem(3)
        item.setText(_translate("Project_Main", "URL"))
        item = self.projects_table.horizontalHeaderItem(4)
        item.setText(_translate("Project_Main", "Input1"))
        item = self.projects_table.horizontalHeaderItem(5)
        item.setText(_translate("Project_Main", "Input2"))
        item = self.projects_table.horizontalHeaderItem(6)
        item.setText(_translate("Project_Main", "Get Data"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Project_Main = QtWidgets.QMainWindow()
    ui = Ui_Project_Main()
    ui.setupUi(Project_Main)
    Project_Main.show()
    sys.exit(app.exec_())