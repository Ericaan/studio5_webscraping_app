# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl

import crud
import pandas as pd
import new_project_ui
import project_ui




class Ui_Project_Main(object):
    # show create project window
    def openNewProjectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = new_project_ui.Ui_CreateNewProjectWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # show the project task -- code for now --
    def openProjectTask(self):
        projectId = self.label_hidden.text()
        if projectId == "":
            print("User has not select any projects")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = project_ui.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            # showing existing project name, url, and inputs
            project_name = crud.read_project_name(self.label_hidden.text())
            URL = crud.read_project_url(self.label_hidden.text())
            user_inputs = crud.read_project_inputs(self.label_hidden.text())
            self.ui.lbl_pname.setText(project_name)
            self.ui.browser.setUrl(QUrl(URL))
            self.ui.url_bar.setText(URL)
            self.ui.txt_input1.setText(user_inputs[0])
            self.ui.txt_input2.setText(user_inputs[1])

    # get the project ID from selected row
    def clicked_row(self):
        currentRow = self.projects_table.currentIndex().row()
        # only want first column -- project ID
        for j in range(1):
            if not self.projects_table.item(currentRow, j) is None:
                selected_project_id = self.projects_table.item(currentRow, j).text()
                # print(selected_project_id)
        self.label_hidden.setText(selected_project_id)
        # return selected_project_id



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

        self.label_hidden = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.menu_layout.addWidget(self.label_hidden)
        self.label_hidden.setHidden(True)

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

        self.open_project_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open_project_button.setMinimumSize(QtCore.QSize(120, 50))
        self.open_project_button.setMaximumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_project_button.setFont(font)
        self.open_project_button.setObjectName("open_project_button")
        self.project_layout.addWidget(self.open_project_button)

        self.projects_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.projects_table.setGridStyle(QtCore.Qt.SolidLine)
        self.projects_table.setObjectName("projects_table")
        self.rowPosition = self.projects_table.rowCount()
        self.projects_table.insertRow(self.rowPosition)
        self.project_layout.addWidget(self.projects_table)

        # get the data from firestore and convert it to csv file
        def data_from_firestore():
            data = crud.read_all_projects()
            count = 1
            data_dict = []

            # append the data into dictionary format
            '''
                {
                    "1":{
                            "URL": "www.google.com"
                        },
                    "2":{
                            "URL": "www.trademe.co.nz"
                        }
                }
            '''
            for i in data:
                data_dict.append(f"\'{count}\':{i}")
                count+=1

            # remove characters from string
            data_dict_remove = re.sub('"','', str(data_dict))
            data_dict_final = str(data_dict_remove).replace("'", '"')
            data_dict_final = str(data_dict_final).lstrip("[").rstrip("]")
            data_dict_final = "{"+f"{data_dict_final}"+"}"

            # create a json file and put the data inside
            with open('project_details_json.json', 'w') as outfile:
                outfile.write(data_dict_final)

            #create csv file from json
            json_to_csv = pd.read_json('project_details_json.json', orient='index')
            json_to_csv.to_csv('project_details.csv', index=False)

        # call the function
        data_from_firestore()

        # read csv file
        read_csv = pd.read_csv('project_details.csv')
        # order the column
        read_csv_reorder = read_csv[['projectId', 'projectName', 'URL', 'userInput', 'lastDate', 'dataDownload']]
        read_csv_reorder.to_csv('project_details_table.csv')

        read_csv = pd.read_csv('project_details_table.csv')
        # rename headers
        read_csv.rename(columns={"dataDownload":"Data Download",
                                 "lastDate": "Last Date",
                                 "userInput": "User Inputs",
                                 "projectName": "Project Name",
                                 "projectId":"Project ID"}, inplace=True)

        # delete some column (displayed on main page)
        read_csv.drop("User Inputs", inplace=True, axis=1)
        read_csv.drop("Unnamed: 0", inplace=True, axis=1)
        # set the rows, columns, and labels for header
        rows = len(read_csv)
        columns = len(read_csv.columns)
        header_labels = read_csv.columns

        # set the table widget
        self.projects_table.setRowCount(rows)
        self.projects_table.setColumnCount(columns)
        self.projects_table.setHorizontalHeaderLabels(header_labels)

        # put the data in table widget item
        for i in range(rows):
            for j in range(columns):
                self.projects_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(read_csv.iat[i,j])))

        # resize the contents of the table
        self.projects_table.resizeColumnsToContents()
        self.projects_table.resizeRowsToContents()

        # for now -- user cannot edit the table
        self.projects_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # open the project task window
        self.open_project_button.clicked.connect(lambda :self.openProjectTask())
        self.open_project_button.clicked.connect(lambda : Project_Main.close())
        # click the table widget to retrieve project ID
        self.projects_table.clicked.connect(lambda :self.clicked_row())
        print(self.label_hidden.text())

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
        self.open_project_button.setText(_translate("Project_Main", "Open"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project_Main = QtWidgets.QMainWindow()
    ui = Ui_Project_Main()
    ui.setupUi(Project_Main)
    Project_Main.show()
    sys.exit(app.exec_())
