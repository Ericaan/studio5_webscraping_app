# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import crud
import re
import loginui

class Ui_SIGNUP(object):
    def email_validation(self, email_input):
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pattern, email_input):
            return True
        else:
            return False

    def go_to_login_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = loginui.Ui_LOGIN()
        self.ui.setupUi(self.window)
        self.window.show()
        SIGNUP.close()

    def empty_fields(self):
        self.email_text.setText("")
        self.pass_text.setText("")

    def signup(self):
        message = QtWidgets.QMessageBox()
        # checking empty fields
        if self.email_text.text() != "" and self.pass_text.text() != "":
            user_email_firestore = crud.checking_user_email(self.email_text.text())
            user_pass_firestore = crud.checking_user_pass(self.email_text.text())
            # checking whether email that user inputted exists in database
            if user_email_firestore == "Exists":
                # check whether email in database has the same password
                # direct user to go to login window
                if user_pass_firestore == self.pass_text.text():
                    message.setText("User has already existed. Please go to LOGIN window")
                    message.exec_()
                    self.empty_fields()
                else:
                    message.setText("User with this email has already registered!")
                    message.exec_()
                    self.empty_fields()
            # if it does not exist, check whether email is valid (pattern)
            else:
                if self.email_validation(self.email_text.text()):
                    # if email's valid = register user
                    crud.create_user(self.email_text.text(), self.pass_text.text())
                    message.setText("Registered")
                    message.exec_()
                    self.go_to_login_window()
                else:
                    message.setText("Email is not valid")
                    message.exec_()
                    self.empty_fields()

        else:
            message.setText("Please enter both fields!")
            message.exec_()


    def setupUi(self, SIGNUP):
        SIGNUP.setObjectName("SIGNUP")
        SIGNUP.resize(660, 470)
        self.centralwidget = QtWidgets.QWidget(SIGNUP)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.email_lbl = QtWidgets.QLabel(self.widget_5)
        self.email_lbl.setObjectName("email_lbl")
        self.horizontalLayout_3.addWidget(self.email_lbl)
        self.email_text = QtWidgets.QLineEdit(self.widget_5)
        self.email_text.setObjectName("email_text")
        self.horizontalLayout_3.addWidget(self.email_text)
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.frame_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pass_lbl = QtWidgets.QLabel(self.widget_6)
        self.pass_lbl.setObjectName("pass_lbl")
        self.horizontalLayout_4.addWidget(self.pass_lbl)
        self.pass_text = QtWidgets.QLineEdit(self.widget_6)
        self.pass_text.setObjectName("pass_text")
        self.horizontalLayout_4.addWidget(self.pass_text)
        #hide the password
        self.pass_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.signup_button = QtWidgets.QPushButton(self.widget_4)
        self.signup_button.setMinimumSize(QtCore.QSize(100, 0))
        self.signup_button.setObjectName("signup_button")
        self.verticalLayout_6.addWidget(self.signup_button)
        self.signup_button.clicked.connect(lambda :self.signup())

        self.verticalLayout_4.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.login_button = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.verticalLayout_5.addWidget(self.login_button)
        self.login_button.clicked.connect(lambda :self.go_to_login_window())
        self.verticalLayout_4.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        SIGNUP.setCentralWidget(self.centralwidget)



        self.retranslateUi(SIGNUP)
        QtCore.QMetaObject.connectSlotsByName(SIGNUP)

    def retranslateUi(self, SIGNUP):
        _translate = QtCore.QCoreApplication.translate
        SIGNUP.setWindowTitle(_translate("SIGNUP", "MainWindow"))
        self.label.setText(_translate("SIGNUP", "SIGNUP"))
        self.email_lbl.setText(_translate("SIGNUP", "Email"))
        self.pass_lbl.setText(_translate("SIGNUP", "Password"))
        self.signup_button.setText(_translate("SIGNUP", "SIGNUP"))
        self.login_button.setText(_translate("SIGNUP", "Already have an account?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIGNUP = QtWidgets.QMainWindow()
    ui = Ui_SIGNUP()
    ui.setupUi(SIGNUP)
    SIGNUP.show()
    sys.exit(app.exec_())
