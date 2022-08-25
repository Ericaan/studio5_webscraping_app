# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectReport.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import all_projects_ui
import constructReportui
import pandas as pd
import numpy as np

class Ui_SelectReport(object):
    def choose_file(self):
        file, check = QFileDialog.getOpenFileName(
            None,
            "Choose File",
            "",
            "CSV Files (*.csv);;Excel Worksheet (*.xlsx)"
        )
        if check:
            self.file_name_lbl.setText(file)
            print(file)

    def cancel(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = all_projects_ui.Ui_Project_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.userId_label.setText(self.id_lbl.text())

    def select_report(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = constructReportui.Ui_ConstructReport()
        self.ui.setupUi(self.window)
        self.window.show()
        report_name = self.report_name_text.text()
        file_name = self.file_name_lbl.text()
        self.ui.lblHidden.setText(file_name)
        data_frame = pd.read_csv(file_name)
        df = data_frame.dropna(how='all')
        rows = len(df)
        columns = len(df.columns)
        header_labels = df.columns

        # set the table widget in construct report
        self.ui.table_show_report.setRowCount(rows)
        self.ui.table_show_report.setColumnCount(columns)
        self.ui.table_show_report.setHorizontalHeaderLabels(header_labels)

        # put the data in table widget item
        for i in range(rows):
            for j in range(columns):
                self.ui.table_show_report.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))

        # unable user to edit the table
        self.ui.table_show_report.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.report_name_label.setText(report_name)
        self.ui.lbl_id.setText(self.id_lbl.text())

    def setupUi(self, SelectReport):
        SelectReport.setObjectName("SelectReport")
        SelectReport.resize(613, 499)
        self.centralwidget = QtWidgets.QWidget(SelectReport)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignVCenter)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_lbl = QtWidgets.QLabel(self.widget_4)
        self.name_lbl.setObjectName("name_lbl")
        self.horizontalLayout.addWidget(self.name_lbl)
        self.report_name_text = QtWidgets.QLineEdit(self.widget_4)
        self.report_name_text.setObjectName("report_name_text")
        self.horizontalLayout.addWidget(self.report_name_text)
        self.verticalLayout_3.addWidget(self.widget_4, 0, QtCore.Qt.AlignLeft)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.choose_file_button = QtWidgets.QPushButton(self.widget_5)
        self.choose_file_button.setObjectName("choose_file_button")
        self.horizontalLayout_2.addWidget(self.choose_file_button)
        self.file_name_lbl = QtWidgets.QLabel(self.widget_5)
        self.file_name_lbl.setText("")
        self.file_name_lbl.setObjectName("file_name_lbl")
        self.horizontalLayout_2.addWidget(self.file_name_lbl)
        self.verticalLayout_3.addWidget(self.widget_5, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.select_btn = QtWidgets.QPushButton(self.widget_3)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout_3.addWidget(self.select_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.widget_3)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        SelectReport.setCentralWidget(self.centralwidget)

        self.id_lbl = QtWidgets.QLabel(self.widget_3)
        self.horizontalLayout_3.addWidget(self.id_lbl)
        self.id_lbl.setHidden(True)

        self.choose_file_button.clicked.connect(lambda: self.choose_file())
        self.select_btn.clicked.connect(lambda: self.select_report())
        self.select_btn.clicked.connect(lambda: SelectReport.close())
        self.cancel_btn.clicked.connect(lambda :self.cancel())
        self.cancel_btn.clicked.connect(lambda :SelectReport.close())

        self.retranslateUi(SelectReport)
        QtCore.QMetaObject.connectSlotsByName(SelectReport)

    def retranslateUi(self, SelectReport):
        _translate = QtCore.QCoreApplication.translate
        SelectReport.setWindowTitle(_translate("SelectReport", "MainWindow"))
        self.label.setText(_translate("SelectReport", "Select New Report "))
        self.name_lbl.setText(_translate("SelectReport", "Name"))
        self.choose_file_button.setText(_translate("SelectReport", "Choose File"))
        self.select_btn.setText(_translate("SelectReport", "Select"))
        self.cancel_btn.setText(_translate("SelectReport", "Cancel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SelectReport = QtWidgets.QMainWindow()
    ui = Ui_SelectReport()
    ui.setupUi(SelectReport)
    SelectReport.show()
    sys.exit(app.exec_())
