# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allProjects.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import bcrypt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PIL import ImageQt
import new_project_ui
import project_ui
import crud
from PyQt5.QtGui import QPixmap
# import selectReportui
import selectReportui
import loginui
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

# showing necessary button in navigation toolbar
class NavigationToolbar(NavigationToolbar):
    NavigationToolbar.toolitems = (
        ('Save', 'Save as Image', 'filesave', 'save_figure'),
    )

class Ui_Project_Main(object):
    def openProjectsTab(self):
        self.stackedWidget.setCurrentIndex(1)
        crud.read_specific_fields(self.userId_label.text())

        # read csv file
        read_csv = pd.read_csv('project_details.csv')
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
                self.projects_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(read_csv.iat[i, j])))

        # resize the contents of the table
        self.projects_table.resizeColumnsToContents()
        self.projects_table.resizeRowsToContents()

        # for now -- user cannot edit the table
        self.projects_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def openDVTab(self):
        self.stackedWidget.setCurrentIndex(2)

    def openManualTab(self):
        self.stackedWidget.setCurrentIndex(4)

    def openAccountTab(self):
        self.stackedWidget.setCurrentIndex(5)
        email = crud.return_user_email(self.userId_label.text())
        self.email_acc_text.setText(email)
        # cannot be change by user
        self.email_acc_text.setReadOnly(True)
        # hide the password
        self.pass_acc_text.setEchoMode(QtWidgets.QLineEdit.Password)

    # show create project window
    def openNewProjectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = new_project_ui.Ui_CreateNewProjectWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.label_hidden.setText(self.userId_label.text())

    def go_to_login_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = loginui.Ui_LOGIN()
        self.ui.setupUi(self.window)
        self.window.show()

    def openProjectTask(self):
        message = QMessageBox()
        projectId = self.label_hidden.text()
        u_temp_dict = crud.read_user_input(projectId)
        if projectId == "":
            message.setText("User has not selected any projects")
            message.exec_()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = project_ui.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            # showing existing project name, url, and inputs
            project_name = crud.read_project_name(self.label_hidden.text())
            URL = crud.read_project_url(self.label_hidden.text())
            URL2 = crud.read_project_url2(self.label_hidden.text())
            # project title
            self.ui.lbl_pname.setText(project_name)
            # tab 1
            self.ui.browser.setUrl(QtCore.QUrl(URL))
            self.ui.url_bar.setText(URL)
            self.ui.tableWidget.setRowCount(2)
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(0, item)
            item.setText("1")
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(1, item)
            item.setText("2")
            # tab 2
            if URL2 != "":
                self.ui.browser_2.setUrl(QtCore.QUrl(URL2))
                self.ui.url_bar_2.setText(URL2)
                self.ui.tableWidget.setRowCount(4)
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget.setVerticalHeaderItem(2, item)
                item.setText("3")
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget.setVerticalHeaderItem(3, item)
                item.setText("4")
            # set up the template for opened project
            self.ui.tableWidget.setColumnCount(0)
            if u_temp_dict is not None:
                print("dict not empty")
                for key in u_temp_dict:
                    item_0 = QtWidgets.QTreeWidgetItem(self.ui.tree_template)
                    count = self.ui.tree_template.topLevelItemCount()
                    self.ui.tree_template.topLevelItem(count-1).setText(0, key)
                    self.ui.tree_template.topLevelItem(count-1).setText(1, u_temp_dict[key][0])
                    self.ui.tree_template.topLevelItem(count-1).setText(2, u_temp_dict[key][1])
                    if URL2 != "":
                        self.ui.tree_template.topLevelItem(count - 1).setText(3, u_temp_dict[key][2])
                        self.ui.tree_template.topLevelItem(count - 1).setText(4, u_temp_dict[key][3])
                    self.ui.tree_template.topLevelItem(count-1).setFlags(self.ui.tree_template.topLevelItem(count-1).flags() | QtCore.Qt.ItemIsEditable)
                    # table update
                    # column
                    item_1 = QtWidgets.QTableWidgetItem()
                    cols = self.ui.tableWidget.columnCount()
                    self.ui.tableWidget.setColumnCount(cols + 1)
                    self.ui.tableWidget.setHorizontalHeaderItem(cols, item_1)
                    self.ui.tableWidget.horizontalHeaderItem(cols).setText(key)
                    # row 1 item
                    item_2 = QtWidgets.QTableWidgetItem()
                    self.ui.tableWidget.setItem(0, cols, item_2)
                    self.ui.tableWidget.item(0, cols).setText(u_temp_dict[key][0])
                    # row 2 item
                    item_3 = QtWidgets.QTableWidgetItem()
                    self.ui.tableWidget.setItem(1, cols, item_3)
                    self.ui.tableWidget.item(1, cols).setText(u_temp_dict[key][1])
                    if URL2 != "":
                        # row 3 item
                        item_2 = QtWidgets.QTableWidgetItem()
                        self.ui.tableWidget.setItem(2, cols, item_2)
                        self.ui.tableWidget.item(2, cols).setText(u_temp_dict[key][2])
                        # row 4 item
                        item_3 = QtWidgets.QTableWidgetItem()
                        self.ui.tableWidget.setItem(3, cols, item_3)
                        self.ui.tableWidget.item(3, cols).setText(u_temp_dict[key][3])
                    for item in u_temp_dict[key]:
                        if type(item) is dict:
                            for key_b in item:
                                prnt = self.ui.tree_template.topLevelItem(count - 1)
                                the_child = QtWidgets.QTreeWidgetItem()
                                the_child.setText(0, key_b)
                                the_child.setText(1, item[key_b][0])
                                the_child.setText(2, item[key_b][1])
                                if URL2 != "":
                                    the_child.setText(3, item[key_b][2])
                                    the_child.setText(4, item[key_b][3])
                                the_child.setFlags(the_child.flags() | QtCore.Qt.ItemIsEditable)
                                prnt.addChild(the_child)
                                # table update
                                # column
                                itm_1 = QtWidgets.QTableWidgetItem()
                                col = self.ui.tableWidget.columnCount()
                                self.ui.tableWidget.setColumnCount(col + 1)
                                self.ui.tableWidget.setHorizontalHeaderItem(col, itm_1)
                                self.ui.tableWidget.horizontalHeaderItem(col).setText(key_b)
                                # row 1 item
                                itm_2 = QtWidgets.QTableWidgetItem()
                                self.ui.tableWidget.setItem(0, (col), itm_2)
                                self.ui.tableWidget.item(0, (col)).setText(item[key_b][0])
                                # row 2 item
                                itm_3 = QtWidgets.QTableWidgetItem()
                                self.ui.tableWidget.setItem(1, (col), itm_3)
                                self.ui.tableWidget.item(1, (col)).setText(item[key_b][1])
                                if URL2 != "":
                                    # row 3 item
                                    itm_2 = QtWidgets.QTableWidgetItem()
                                    self.ui.tableWidget.setItem(2, (col), itm_2)
                                    self.ui.tableWidget.item(2, (col)).setText(item[key_b][2])
                                    # row 4 item
                                    itm_3 = QtWidgets.QTableWidgetItem()
                                    self.ui.tableWidget.setItem(3, (col), itm_3)
                                    self.ui.tableWidget.item(3, (col)).setText(item[key_b][3])
            else:
                print("dict is empty")


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

    def alertLogout(self):
        message = QMessageBox()
        message.setObjectName("LOGOUT")
        message.setText("Do you want to logout?")
        message.setStandardButtons(message.Yes | message.No)
        message.exec_()
        # print(int(message.exec_()))
        if message.exec_() == 16384:
            Project_Main.close()
        #     print("yes")
        # elif message.exec_() == 65536:
        #     print("no")

    def changePass(self):
        message = QMessageBox()
        message.setObjectName("Update Password")
        message.setText("Do you want to update the password?")
        message.setStandardButtons(message.Yes | message.No)
        message.exec_()
        if message.exec_() == 16384:
            # user hasn't change the pass
            user_changed_password = self.pass_acc_text.text().encode('utf-8')
            user_pass_firestore = crud.return_user_pass(self.userId_label.text())
            if self.pass_acc_text.text() != "":
                if bcrypt.checkpw(user_changed_password, user_pass_firestore):
                    msg = QMessageBox()
                    msg.setText("You have not changed the password")
                    msg.exec_()
                else:
                    changed_password = self.pass_acc_text.text()
                    changed_password = changed_password.encode('utf-8')
                    hashed_pass = bcrypt.hashpw(changed_password, bcrypt.gensalt(10))
                    crud.update_user(self.userId_label.text(), hashed_pass)
                    msg = QMessageBox()
                    msg.setText("You have changed the password")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Please make sure you've entered the new password")
                msg.exec_()

    def deleteAccount(self):
        message = QMessageBox()
        message.setObjectName("Delete Account")
        message.setText("Do you want to delete your account? Warning: Every project you've created will be deleted")
        message.setStandardButtons(message.Yes | message.No)
        message.exec_()
        if message.exec_() == 16384:
            crud.delete_user(self.userId_label.text())
            crud.delete_project_with_userId(self.userId_label.text())
            # close the main_menu and direct user to login window
            Project_Main.close()
            self.go_to_login_window()

    def go_to_select_report(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = selectReportui.Ui_SelectReport()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.id_lbl.setText(self.userId_label.text())

    def download_report(self):
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image","",
                                                            "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if filePath == "":
            return
        image = ImageQt.fromqpixmap(self.widget_8.grab())
        image.save(filePath)
        print("saved")

    def setupUi(self, Project_Main):
        Project_Main.setObjectName("Project_Main")
        Project_Main.resize(1106, 600)
        self.centralwidget = QtWidgets.QWidget(Project_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(200, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.project_button = QtWidgets.QPushButton(self.frame_4)
        self.project_button.setObjectName("project_button")
        self.verticalLayout_3.addWidget(self.project_button)
        self.dv_button = QtWidgets.QPushButton(self.frame_4)
        self.dv_button.setObjectName("dv_button")
        self.verticalLayout_3.addWidget(self.dv_button)
        self.manual_button = QtWidgets.QPushButton(self.frame_4)
        self.manual_button.setObjectName("manual_button")
        self.verticalLayout_3.addWidget(self.manual_button)
        self.account_button = QtWidgets.QPushButton(self.frame_4)
        self.account_button.setObjectName("account_button")
        self.verticalLayout_3.addWidget(self.account_button)
        self.logout_button = QtWidgets.QPushButton(self.frame_4)
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout_3.addWidget(self.logout_button)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.main_body)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line = QtWidgets.QFrame(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MainPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.MainPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.stackedWidget.addWidget(self.MainPage)
        self.Projects = QtWidgets.QWidget()
        self.Projects.setObjectName("Projects")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Projects)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_layout = QtWidgets.QVBoxLayout()
        self.project_layout.setContentsMargins(20, 20, 20, -1)
        self.project_layout.setObjectName("project_layout")
        self.newproject_button = QtWidgets.QPushButton(self.Projects)
        self.newproject_button.setMinimumSize(QtCore.QSize(120, 50))
        self.newproject_button.setMaximumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newproject_button.setFont(font)
        self.newproject_button.setObjectName("newproject_button")
        self.project_layout.addWidget(self.newproject_button)
        self.open_project_button = QtWidgets.QPushButton(self.Projects)
        self.open_project_button.setMinimumSize(QtCore.QSize(120, 50))
        self.open_project_button.setMaximumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_project_button.setFont(font)
        self.open_project_button.setObjectName("open_project_button")
        self.project_layout.addWidget(self.open_project_button)
        self.projects_table = QtWidgets.QTableWidget(self.Projects)
        self.projects_table.setGridStyle(QtCore.Qt.SolidLine)
        self.projects_table.setObjectName("projects_table")
        self.projects_table.setColumnCount(0)
        self.projects_table.setRowCount(0)
        self.projects_table.horizontalHeader().setCascadingSectionResizes(False)
        self.project_layout.addWidget(self.projects_table)
        self.horizontalLayout_2.addLayout(self.project_layout)
        self.stackedWidget.addWidget(self.Projects)
        self.DataVisualisation = QtWidgets.QWidget()
        self.DataVisualisation.setObjectName("DataVisualisation")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DataVisualisation)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.DataVisualisation)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.widget_5, 0, QtCore.Qt.AlignTop)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.select_report_dv_button = QtWidgets.QPushButton(self.widget_6)
        self.select_report_dv_button.setObjectName("select_report_dv_button")
        self.verticalLayout_14.addWidget(self.select_report_dv_button)
        self.verticalLayout_8.addWidget(self.widget_6, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_8.addWidget(self.widget_7)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.stackedWidget.addWidget(self.DataVisualisation)
        self.ReportDVTab = QtWidgets.QWidget()
        self.ReportDVTab.setObjectName("ReportDVTab")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.ReportDVTab)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_8 = QtWidgets.QWidget(self.ReportDVTab)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.widget_9.setFont(font)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.dv_report_name_lbl = QtWidgets.QLabel(self.widget_10)
        self.dv_report_name_lbl.setMinimumSize(QtCore.QSize(0, 70))
        self.dv_report_name_lbl.setObjectName("dv_report_name_lbl")
        self.verticalLayout_19.addWidget(self.dv_report_name_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_18.addWidget(self.widget_10, 0, QtCore.Qt.AlignTop)
        self.widget_12 = QtWidgets.QWidget(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_12.setFont(font)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.back_btn = QtWidgets.QPushButton(self.widget_12)
        # self.back_btn.setObjectName("back_btn")
        # self.horizontalLayout_6.addWidget(self.back_btn)
        self.download_btn = QtWidgets.QPushButton(self.widget_12)
        self.download_btn.setObjectName("download_btn")
        self.horizontalLayout_6.addWidget(self.download_btn)
        self.verticalLayout_18.addWidget(self.widget_12, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_17.addWidget(self.widget_9)
        self.widget_11 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 885, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.addWidget(self.scrollArea)
        self.verticalLayout_17.addWidget(self.widget_11)
        self.verticalLayout_16.addWidget(self.widget_8)
        self.stackedWidget.addWidget(self.ReportDVTab)
        self.Manual = QtWidgets.QWidget()
        self.Manual.setObjectName("Manual")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Manual)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.Manual)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.Manual)
        self.Account = QtWidgets.QWidget()
        self.Account.setObjectName("Account")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Account)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.Account)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.verticalLayout_9.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget = QtWidgets.QWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.email_acc_lbl = QtWidgets.QLabel(self.widget)
        self.email_acc_lbl.setObjectName("email_acc_lbl")
        self.horizontalLayout_3.addWidget(self.email_acc_lbl)
        self.email_acc_text = QtWidgets.QLineEdit(self.widget)
        self.email_acc_text.setObjectName("email_acc_text")
        self.horizontalLayout_3.addWidget(self.email_acc_text)
        self.verticalLayout_11.addWidget(self.widget, 0, QtCore.Qt.AlignBottom)
        self.widget_2 = QtWidgets.QWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pass_acc_lbl = QtWidgets.QLabel(self.widget_2)
        self.pass_acc_lbl.setObjectName("pass_acc_lbl")
        self.horizontalLayout_4.addWidget(self.pass_acc_lbl)
        self.pass_acc_text = QtWidgets.QLineEdit(self.widget_2)
        self.pass_acc_text.setObjectName("pass_acc_text")
        self.horizontalLayout_4.addWidget(self.pass_acc_text)
        self.change_pass_btn = QtWidgets.QPushButton(self.widget_2)
        self.change_pass_btn.setObjectName("change_pass_btn")
        self.horizontalLayout_4.addWidget(self.change_pass_btn)
        self.verticalLayout_11.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.delete_acc_button = QtWidgets.QPushButton(self.widget_3)
        self.delete_acc_button.setObjectName("delete_acc_button")
        self.verticalLayout_12.addWidget(self.delete_acc_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_11.addWidget(self.widget_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.Account)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.main_body)
        self.verticalLayout.addWidget(self.frame_2)
        Project_Main.setCentralWidget(self.centralwidget)

        self.label_hidden = QtWidgets.QLabel(self.frame_4)
        self.verticalLayout_3.addWidget(self.label_hidden)
        self.label_hidden.setHidden(True)

        self.userId_label = QtWidgets.QLabel(self.frame_4)
        self.verticalLayout_3.addWidget(self.userId_label)
        self.userId_label.setHidden(True)

        # self.lbl = QtWidgets.QLabel(self.widget_11)
        # self.verticalLayout_20.addWidget(self.lbl)
        # self.lbl.setHidden(True)

        self.project_button.clicked.connect(lambda: self.openProjectsTab())
        self.dv_button.clicked.connect(lambda: self.openDVTab())
        self.manual_button.clicked.connect(lambda: self.openManualTab())
        self.account_button.clicked.connect(lambda: self.openAccountTab())
        self.logout_button.clicked.connect(lambda: self.alertLogout())

        self.newproject_button.clicked.connect(lambda: self.openNewProjectWindow())
        self.newproject_button.clicked.connect(lambda: Project_Main.close())

        # open the project task window
        self.open_project_button.clicked.connect(lambda: self.openProjectTask())
        self.open_project_button.clicked.connect(lambda: Project_Main.close())
        # click the table widget to retrieve project ID
        self.projects_table.clicked.connect(lambda: self.clicked_row())

        self.select_report_dv_button.clicked.connect(lambda: self.go_to_select_report())
        self.select_report_dv_button.clicked.connect(lambda: Project_Main.close())

        # canvas for data visualisation
        self.figure = plt.figure(figsize=(20, 20))
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_21.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self.widget_12)
        self.horizontalLayout_6.addWidget(self.toolbar)

        self.dv_table = QtWidgets.QTableWidget(self.widget_11)
        self.dv_table.setObjectName("dv_table")
        self.verticalLayout_17.addWidget(self.dv_table)
        self.dv_table.setHidden(True)

        self.change_pass_btn.clicked.connect(lambda: self.changePass())

        self.delete_acc_button.clicked.connect(lambda: self.deleteAccount())

        self.download_btn.clicked.connect(lambda: self.download_report())

        self.retranslateUi(Project_Main)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Project_Main)

        self.retranslateUi(Project_Main)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Project_Main)

    def retranslateUi(self, Project_Main):
        _translate = QtCore.QCoreApplication.translate
        Project_Main.setWindowTitle(_translate("Project_Main", "MainWindow"))
        self.project_button.setText(_translate("Project_Main", "Projects"))
        self.dv_button.setText(_translate("Project_Main", "Data Visualisation"))
        self.manual_button.setText(_translate("Project_Main", "Instruction Manual"))
        self.account_button.setText(_translate("Project_Main", "My Account"))
        self.logout_button.setText(_translate("Project_Main", "Log out"))
        self.label.setText(_translate("Project_Main", "Main Page"))
        self.newproject_button.setText(_translate("Project_Main", "New Project"))
        self.open_project_button.setText(_translate("Project_Main", "Open"))
        self.label_2.setText(_translate("Project_Main", "Data Visualisation"))
        self.select_report_dv_button.setText(_translate("Project_Main", "Select Report"))
        self.dv_report_name_lbl.setText(_translate("Project_Main", "Data Visualisation Name"))
        # self.back_btn.setText(_translate("Project_Main", "Back"))
        self.download_btn.setText(_translate("Project_Main", "Download"))
        self.label_5.setText(_translate("Project_Main", "Instruction Manual"))
        self.label_3.setText(_translate("Project_Main", "My Account"))
        self.email_acc_lbl.setText(_translate("Project_Main", "Email"))
        self.pass_acc_lbl.setText(_translate("Project_Main", "Password"))
        self.change_pass_btn.setText(_translate("Project_Main", "Change Password"))
        self.delete_acc_button.setText(_translate("Project_Main", "Delete Account"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Project_Main = QtWidgets.QMainWindow()
    ui = Ui_Project_Main()
    ui.setupUi(Project_Main)
    Project_Main.show()
    sys.exit(app.exec_())
