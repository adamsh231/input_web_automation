# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpeg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#%%

from PyQt5 import QtCore, QtGui, QtWidgets

from simpeg import loginSimpeg, tambahJabatanByNIP
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnOpenChrome = QtWidgets.QPushButton(Dialog)
        self.btnOpenChrome.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.btnOpenChrome.setObjectName("btnOpenChrome")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 50, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.inputUser = QtWidgets.QLineEdit(Dialog)
        self.inputUser.setGeometry(QtCore.QRect(10, 70, 271, 31))
        self.inputUser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inputUser.setText("")
        self.inputUser.setAlignment(QtCore.Qt.AlignCenter)
        self.inputUser.setClearButtonEnabled(False)
        self.inputUser.setObjectName("inputUser")
        self.inputPassword = QtWidgets.QLineEdit(Dialog)
        self.inputPassword.setGeometry(QtCore.QRect(10, 110, 271, 31))
        self.inputPassword.setText("")
        self.inputPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPassword.setObjectName("inputPassword")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(290, 70, 101, 71))
        self.btnLogin.setObjectName("btnLogin")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 411, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.inputNIP = QtWidgets.QLineEdit(Dialog)
        self.inputNIP.setGeometry(QtCore.QRect(10, 160, 321, 31))
        self.inputNIP.setAlignment(QtCore.Qt.AlignCenter)
        self.inputNIP.setObjectName("inputNIP")
        self.btnCari = QtWidgets.QPushButton(Dialog)
        self.btnCari.setGeometry(QtCore.QRect(340, 160, 51, 31))
        self.btnCari.setObjectName("btnCari")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        ## BEGIN HERE
        self.btnLogin.clicked.connect(self.login)
        self.btnOpenChrome.clicked.connect(self.openChrome)
        self.btnCari.clicked.connect(self.cariNIP)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entry"))
        self.btnOpenChrome.setText(_translate("Dialog", "Open Chrome Browser"))
        self.inputUser.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.inputUser.setPlaceholderText(_translate("Dialog", "Username"))
        self.inputPassword.setPlaceholderText(_translate("Dialog", "Password"))
        self.btnLogin.setText(_translate("Dialog", "Login Simpeg"))
        self.inputNIP.setPlaceholderText(_translate("Dialog", "NIP"))
        self.btnCari.setText(_translate("Dialog", "Cari"))

    ## BEGIN HERE
    def openChrome(self):
        try :
            self.driver = webdriver.Chrome("./chromedriver.exe")
        except :
            print("Something Went Wrong")
            
    def login(self):
        try :
            loginSimpeg(self.driver, self.inputUser.text(), self.inputPassword.text())
        except :
            print("Something Went Wrong")
            
    def cariNIP(self):
        try :
            tambahJabatanByNIP(time=time, driver=self.driver, nip=self.inputNIP.text())
        except :
            print("Something Went Wrong")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# %%
