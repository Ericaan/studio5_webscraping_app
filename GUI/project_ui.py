# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

import web_scraper
from GUI import all_projects_ui
import crud
import pandas as pd
import download_data
from GUI import project_methods
import input_notice

# holds the data from template and its inputs
temp_dict = {}


class Ui_MainWindow(object):
    temp_dict.clear()

    # method to go back to projects
    def openAllProjectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = all_projects_ui.Ui_Project_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentIndex(1)
        uid = crud.return_userid_by_pname(self.lbl_pname.text())
        self.ui.userId_label.setText(uid)
        crud.read_specific_fields(uid)
        # read csv file
        read_csv = pd.read_csv('project_details.csv')
        rows = len(read_csv)
        columns = len(read_csv.columns)
        header_labels = read_csv.columns
        # set the table widget
        self.ui.projects_table.setRowCount(rows)
        self.ui.projects_table.setColumnCount(columns)
        self.ui.projects_table.setHorizontalHeaderLabels(header_labels)
        # put the data in table widget item
        for i in range(rows):
            for j in range(columns):
                self.ui.projects_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(read_csv.iat[i, j])))
        # resize the contents of the table
        self.ui.projects_table.resizeColumnsToContents()
        self.ui.projects_table.resizeRowsToContents()
        # for now -- user cannot edit the table
        self.ui.projects_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # open the window to download data
    def open_getData_dialog(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = download_data.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.my_url = self.url_bar.text()
        self.dialog.show()

    # open the input notice
    def open_inputNotice_dialog(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = input_notice.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tb_home = QtWidgets.QToolButton(self.groupBox_4)
        self.tb_home.setMinimumSize(QtCore.QSize(50, 50))
        self.tb_home.setObjectName("tb_home")
        self.horizontalLayout_4.addWidget(self.tb_home)
        self.lbl_pname = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_pname.setFont(font)
        self.lbl_pname.setObjectName("lbl_pname")
        self.horizontalLayout_4.addWidget(self.lbl_pname)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.lbl_input1 = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_input1.setObjectName("lbl_input1")
        self.verticalLayout_2.addWidget(self.lbl_input1)
        self.txt_input1 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txt_input1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_input1.setObjectName("txt_input1")
        self.verticalLayout_2.addWidget(self.txt_input1)
        self.lbl_input2 = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_input2.setObjectName("lbl_input2")
        self.verticalLayout_2.addWidget(self.lbl_input2)
        self.txt_input2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txt_input2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_input2.setObjectName("txt_input2")
        self.verticalLayout_2.addWidget(self.txt_input2)
        self.btn_add2template = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add2template.setObjectName("btn_add2template")
        self.verticalLayout_2.addWidget(self.btn_add2template)
        self.tree_template = QtWidgets.QTreeWidget(self.groupBox_2)
        self.tree_template.setMinimumSize(QtCore.QSize(0, 0))
        self.tree_template.setObjectName("tree_template")
        self.tree_template.headerItem().setText(0, "Project")
        self.verticalLayout_2.addWidget(self.tree_template)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.rb_second_tab = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_second_tab.setObjectName("rb_second_tab")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_second_tab)
        self.gridLayout.addWidget(self.rb_second_tab, 0, 1, 1, 1)
        self.rb_select = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_select.setChecked(True)
        self.rb_select.setObjectName("rb_select")
        self.buttonGroup.addButton(self.rb_select)
        self.gridLayout.addWidget(self.rb_select, 0, 0, 1, 1)
        self.rb_rel_select = QtWidgets.QRadioButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_rel_select.sizePolicy().hasHeightForWidth())
        self.rb_rel_select.setSizePolicy(sizePolicy)
        self.rb_rel_select.setChecked(False)
        self.rb_rel_select.setObjectName("rb_rel_select")
        self.buttonGroup.addButton(self.rb_rel_select)
        self.gridLayout.addWidget(self.rb_rel_select, 2, 0, 1, 1)
        self.rb_delete = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_delete.setObjectName("rb_delete")
        self.buttonGroup.addButton(self.rb_delete)
        self.gridLayout.addWidget(self.rb_delete, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_psave = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_psave.setFont(font)
        self.btn_psave.setObjectName("btn_psave")
        self.horizontalLayout_5.addWidget(self.btn_psave)
        self.btn_get_data = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_get_data.setFont(font)
        self.btn_get_data.setObjectName("btn_get_data")
        self.horizontalLayout_5.addWidget(self.btn_get_data)
        self.btn_del = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout_5.addWidget(self.btn_del)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.url_bar = QtWidgets.QLineEdit(self.groupBox_5)
        self.url_bar.setObjectName("url_bar")
        self.horizontalLayout_6.addWidget(self.url_bar)
        self.go_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.go_btn.setObjectName("go_btn")
        self.horizontalLayout_6.addWidget(self.go_btn)
        self.back_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_6.addWidget(self.back_btn)
        self.for_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.for_btn.setObjectName("for_btn")
        self.horizontalLayout_6.addWidget(self.for_btn)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.browser = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.browser.setMinimumSize(QtCore.QSize(0, 0))
        self.browser.setObjectName("browser")
        self.verticalLayout_4.addWidget(self.browser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 13, 747, 50))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.url_bar_2 = QtWidgets.QLineEdit(self.groupBox_7)
        self.url_bar_2.setObjectName("url_bar_2")
        self.horizontalLayout_7.addWidget(self.url_bar_2)
        self.go_btn_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.go_btn_2.setObjectName("go_btn_2")
        self.horizontalLayout_7.addWidget(self.go_btn_2)
        self.back_btn_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.back_btn_2.setObjectName("back_btn_2")
        self.horizontalLayout_7.addWidget(self.back_btn_2)
        self.for_btn_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.for_btn_2.setObjectName("for_btn_2")
        self.horizontalLayout_7.addWidget(self.for_btn_2)
        self.browser_2 = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.browser_2.setGeometry(QtCore.QRect(10, 70, 747, 418))
        self.browser_2.setMinimumSize(QtCore.QSize(0, 0))
        self.browser_2.setObjectName("browser_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)

        self.verticalLayout_3.addWidget(self.tableWidget)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # non autogenerated code
        # commands cleanup extra aesthetic lines
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setStyleSheet("QGroupBox#groupBox_2 {border:0;}")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setStyleSheet("QGroupBox#groupBox_4 {border:0;}")
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setStyleSheet("QGroupBox#groupBox_5 {border:0;}")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setStyleSheet("QGroupBox#groupBox_3 {border:0;}")
        self.groupBox.setFlat(True)
        self.groupBox.setStyleSheet("QGroupBox#groupBox {border:0;}")
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setStyleSheet("QGroupBox#groupBox_6 {border:0;}")
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setStyleSheet("QGroupBox#groupBox_7 {border:0;}")

        # make browser buttons work
        self.go_btn.clicked.connect(
            lambda: project_methods.navigate(self.url_bar.toPlainText(), self.url_bar, self.browser))
        self.back_btn.clicked.connect(self.browser.back)
        self.for_btn.clicked.connect(self.browser.forward)
        self.go_btn_2.clicked.connect(
            lambda: project_methods.navigate(self.url_bar_2.toPlainText(), self.url_bar_2, self.browser_2))
        self.back_btn_2.clicked.connect(self.browser_2.back)
        self.for_btn_2.clicked.connect(self.browser_2.forward)
        # template handling
        self.tree_template.setColumnCount(1)
        self.tree_template.itemClicked.connect(
            lambda: project_methods.del_temp_item(self.tree_template, self.rb_delete))
        self.btn_add2template.clicked.connect(lambda: self.check_inputs())
        # preview table handling
        self.tableWidget.clicked.connect(lambda: project_methods.table_refresh(self.tableWidget, self.tree_template))
        # back button functionality
        self.tb_home.clicked.connect(lambda: self.openAllProjectWindow())
        self.tb_home.clicked.connect(lambda: MainWindow.close())
        # save button functionality
        self.btn_psave.clicked.connect(lambda: project_methods.make_dict(self.tree_template, temp_dict))
        self.btn_psave.clicked.connect(
            lambda: project_methods.save_click(self.lbl_pname, self.url_bar, self.url_bar_2, temp_dict))
        # get data button functionality
        self.btn_get_data.clicked.connect(lambda: project_methods.make_dict(self.tree_template, temp_dict))
        self.btn_get_data.clicked.connect(lambda: self.open_getData_dialog())
        # delete button
        self.btn_del.clicked.connect(lambda: project_methods.del_project(self.lbl_pname))
        self.btn_del.clicked.connect(lambda: self.openAllProjectWindow())
        self.btn_del.clicked.connect(lambda: MainWindow.close())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # check if inputs are legit
    def check_inputs(self):
        valid = False
        if self.rb_select.isChecked():
            valid = web_scraper.check_inputs(self.url_bar.text(), self.txt_input1.toPlainText(),
                                             self.txt_input2.toPlainText())
        elif self.rb_rel_select.isChecked():
            valid = web_scraper.check_inputs(self.url_bar.text(), self.txt_input1.toPlainText(),
                                             self.txt_input2.toPlainText())
        elif self.rb_second_tab.isChecked():
            valid = web_scraper.check_inputs(self.url_bar_2.text(), self.txt_input1.toPlainText(),
                                             self.txt_input2.toPlainText())
        # what to do depending on whether the inputs are valid
        if valid:
            print("valid")
            project_methods.new_branch(self.rb_select, self.rb_rel_select, self.rb_second_tab, self.tree_template,
                                       self.txt_input1, self.txt_input2, self.tableWidget)
        else:
            self.open_inputNotice_dialog()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tb_home.setText(_translate("MainWindow", "..."))
        self.lbl_pname.setText(_translate("MainWindow", "Project Name"))
        self.lbl_input1.setText(_translate("MainWindow", "Input 1"))
        self.lbl_input2.setText(_translate("MainWindow", "Input 2"))
        self.btn_add2template.setText(_translate("MainWindow", "Add to Template"))
        __sortingEnabled = self.tree_template.isSortingEnabled()
        self.tree_template.setSortingEnabled(False)
        self.tree_template.setSortingEnabled(__sortingEnabled)
        # non autogenerated code
        self.tree_template.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tree_template.setDragEnabled(True)
        self.tree_template.setAcceptDrops(True)
        self.groupBox_6.setTitle(_translate("MainWindow", "Commands"))
        self.rb_second_tab.setText(_translate("MainWindow", "Second Tab"))
        self.rb_select.setText(_translate("MainWindow", "Select"))
        self.rb_rel_select.setText(_translate("MainWindow", "Relative Select"))
        self.rb_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_psave.setText(_translate("MainWindow", "Save"))
        self.btn_get_data.setText(_translate("MainWindow", "Get Data"))
        self.btn_del.setText(_translate("MainWindow", "Delete"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.back_btn.setText(_translate("MainWindow", "<"))
        self.for_btn.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.go_btn_2.setText(_translate("MainWindow", "Go"))
        self.back_btn_2.setText(_translate("MainWindow", "<"))
        self.for_btn_2.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "1"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "2"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "3"))
        # item = self.tableWidget.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "*Double click on the table to update"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
