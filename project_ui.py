# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 839)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QSize(300, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setStyleSheet("QGroupBox#groupBox_2 {border:0;}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(0, 100))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")        
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setStyleSheet("QGroupBox#groupBox_4 {border:0;}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tb_home = QToolButton(self.groupBox_4)
        self.tb_home.setMinimumSize(QSize(50, 50))
        self.tb_home.setObjectName("tb_home")
        self.horizontalLayout_4.addWidget(self.tb_home)
        self.lbl_pname = QLabel(self.groupBox_4)
        font = QFont()
        font.setPointSize(20)
        self.lbl_pname.setFont(font)
        self.lbl_pname.setObjectName("lbl_pname")
        self.horizontalLayout_4.addWidget(self.lbl_pname)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.lbl_input1 = QLabel(self.groupBox_2)
        self.lbl_input1.setObjectName("lbl_input1")
        self.verticalLayout_2.addWidget(self.lbl_input1)
        self.txt_input1 = QTextEdit(self.groupBox_2)
        self.txt_input1.setMaximumSize(QSize(16777215, 50))
        self.txt_input1.setObjectName("txt_input1")
        self.verticalLayout_2.addWidget(self.txt_input1)
        self.lbl_input2 = QLabel(self.groupBox_2)
        self.lbl_input2.setObjectName("lbl_input2")
        self.verticalLayout_2.addWidget(self.lbl_input2)
        self.txt_input2 = QTextEdit(self.groupBox_2)
        self.txt_input2.setMaximumSize(QSize(16777215, 50))
        self.txt_input2.setObjectName("txt_input2")
        self.verticalLayout_2.addWidget(self.txt_input2)
        self.tree_template = QTreeWidget(self.groupBox_2)
        self.tree_template.setMinimumSize(QSize(0, 0))
        self.tree_template.setObjectName("tree_template")
        self.tree_template.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.tree_template)
        self.lbl_commands = QLabel(self.groupBox_2)
        self.lbl_commands.setObjectName("lbl_commands")
        self.verticalLayout_2.addWidget(self.lbl_commands)
        self.rb_select = QRadioButton(self.groupBox_2)
        self.rb_select.setObjectName("rb_select")
        self.verticalLayout_2.addWidget(self.rb_select)
        self.rb_rel_select = QRadioButton(self.groupBox_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_rel_select.sizePolicy().hasHeightForWidth())
        self.rb_rel_select.setSizePolicy(sizePolicy)
        self.rb_rel_select.setObjectName("rb_rel_select")
        self.verticalLayout_2.addWidget(self.rb_rel_select)
        self.tb_delete = QRadioButton(self.groupBox_2)
        self.tb_delete.setObjectName("tb_delete")
        self.verticalLayout_2.addWidget(self.tb_delete)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setFlat(True)
        self.groupBox.setStyleSheet("QGroupBox#groupBox {border:0;}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.groupBox_3.setMaximumSize(QSize(16777215, 100))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setStyleSheet("QGroupBox#groupBox_3 {border:0;}")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_psave = QPushButton(self.groupBox_3)
        font = QFont()
        font.setPointSize(12)
        self.btn_psave.setFont(font)
        self.btn_psave.setObjectName("btn_psave")
        self.horizontalLayout_5.addWidget(self.btn_psave)
        self.btn_ = QPushButton(self.groupBox_3)
        font = QFont()
        font.setPointSize(12)
        self.btn_.setFont(font)
        self.btn_.setObjectName("btn_")
        self.horizontalLayout_5.addWidget(self.btn_)
        self.pushButton_2 = QPushButton(self.groupBox_3)
        font = QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setMaximumSize(QSize(16777215, 50))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setStyleSheet("QGroupBox#groupBox_5 {border:0;}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.url_bar = QLineEdit(self.groupBox_5)
        self.url_bar.setObjectName("url_bar")
        self.horizontalLayout_6.addWidget(self.url_bar)
        self.go_btn = QPushButton(self.groupBox_5)
        self.go_btn.setObjectName("go_btn")
        self.horizontalLayout_6.addWidget(self.go_btn)
        self.back_btn = QPushButton(self.groupBox_5)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_6.addWidget(self.back_btn)
        self.for_btn = QPushButton(self.groupBox_5)
        self.for_btn.setObjectName("for_btn")
        self.horizontalLayout_6.addWidget(self.for_btn)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.browser = QWebEngineView(self.tab)
        self.browser.setMinimumSize(QSize(0, 0))
        self.browser.setObjectName("browser")
        self.verticalLayout_4.addWidget(self.browser)
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tb_home.setText(_translate("MainWindow", "..."))
        self.lbl_pname.setText(_translate("MainWindow", "Project Name"))
        self.lbl_input1.setText(_translate("MainWindow", "Input 1"))
        self.lbl_input2.setText(_translate("MainWindow", "Input 2"))
        self.lbl_commands.setText(_translate("MainWindow", "Commands"))
        self.rb_select.setText(_translate("MainWindow", "Select"))
        self.rb_rel_select.setText(_translate("MainWindow", "Relative Select"))
        self.tb_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_psave.setText(_translate("MainWindow", "Save"))
        self.btn_.setText(_translate("MainWindow", "Get Data"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.back_btn.setText(_translate("MainWindow", "<"))
        self.for_btn.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
