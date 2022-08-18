# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import project_ui
import web_scraper

results = {}


class Ui_Dialog(object):
    my_url = ""
    my_url_2 = ""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 430)
        self.lbl_download_data = QtWidgets.QLabel(Dialog)
        self.lbl_download_data.setGeometry(QtCore.QRect(80, 50, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_download_data.setFont(font)
        self.lbl_download_data.setObjectName("lbl_download_data")
        self.rb_json = QtWidgets.QRadioButton(Dialog)
        self.rb_json.setGeometry(QtCore.QRect(100, 130, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_json.setFont(font)
        self.rb_json.setObjectName("rb_json")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_json)
        self.rb_csv = QtWidgets.QRadioButton(Dialog)
        self.rb_csv.setGeometry(QtCore.QRect(100, 170, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_csv.setFont(font)
        self.rb_csv.setObjectName("rb_csv")
        self.buttonGroup.addButton(self.rb_csv)
        self.btn_generate = QtWidgets.QPushButton(Dialog)
        self.btn_generate.setGeometry(QtCore.QRect(80, 300, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_generate.setFont(font)
        self.btn_generate.setObjectName("btn_generate")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 300, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 250, 371, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 210, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(240, 210, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")

        # close dialog button
        self.btn_cancel.clicked.connect(lambda: Dialog.close())

        # generate button
        # self.btn_generate.clicked.connect(lambda: self.web_scrape(project_ui.temp_dict))
        self.btn_generate.clicked.connect(lambda: self.get_data())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def web_scrape(self, diction):
        for key in diction:
            values = web_scraper.scrape(self.my_url, diction[key][0], diction[key][1], 1)
            results[key] = values
            for item in diction[key]:
                if type(item) is dict:
                    self.web_scrape(item)

    def get_data(self):
        if len(results) == 0:
            self.web_scrape(project_ui.temp_dict)
            if self.rb_csv.isChecked():
                web_scraper.get_data_csv_json("csv", results, self.lineEdit.text())
            elif self.rb_json.isChecked():
                web_scraper.get_data_csv_json("json", results, self.lineEdit.text())
        else:
            if self.rb_csv.isChecked():
                web_scraper.get_data_csv_json("csv", results, self.lineEdit.text())
            elif self.rb_json.isChecked():
                web_scraper.get_data_csv_json("json", results, self.lineEdit.text())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_download_data.setText(_translate("Dialog", "Download Data"))
        self.rb_json.setText(_translate("Dialog", "JSON"))
        self.rb_csv.setText(_translate("Dialog", "CSV"))
        self.btn_generate.setText(_translate("Dialog", "Generate"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "File Name :"))
        self.label_2.setText(_translate("Dialog", "No. of result pages :"))