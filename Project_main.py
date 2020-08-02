from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QAction,QApplication, QPushButton, QLineEdit,QInputDialog, QApplication,QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import Model_1 as m1

from Project_Insert import Ui_DialogInsert
from Project_Display import Ui_DialogDisplay
from Project_Update import Ui_DialogUpdate

import mysql.connector
cn = mysql.connector.connect(user='root',password='',host='localhost',database='project')
command = cn.cursor()
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #self.setWindowIcon(QIcon('icon/add1.jpg'))
        MainWindow.resize(817, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ######
        '''
        self.addAction = QAction(QIcon("add1.jpg"), 'add', self)
        #fileMenu.addAction(copyAction)
        self.saveAction = QAction(QIcon("delete.png"), 'delete', self.centralwidget)
        #fileMenu.addAction(saveAction)
        self.pasteAction = QAction(QIcon("display.png"), 'display', self.centralwidget)
        #fileMenu.addAction(pasteAction)
        self.exiteAction = QAction(QIcon("update.jpg"), 'update', self.centralwidget)
        #exiteAction.triggered.connect(self.exitWindow)
        #fileMenu.addAction(exiteAction)
        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(self.addAction)
        self.toolbar.addAction(self.deleteAction)
        self.toolbar.addAction(self.displayAction)
        self.toolbar.addAction(self.updateAction)
        
        '''
        ########
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 260, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.txtFacultyName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFacultyName.setGeometry(QtCore.QRect(300, 90, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtFacultyName.setFont(font)
        self.txtFacultyName.setObjectName("txtFacultyName")
        
        self.txtFacultyId = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFacultyId.setGeometry(QtCore.QRect(300, 170, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtFacultyId.setFont(font)
        self.txtFacultyId.setObjectName("txtFacultyId")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(300, 250, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.btnSignUp1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignUp1.setGeometry(QtCore.QRect(340, 360, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignUp1.setFont(font)
        self.btnSignUp1.setObjectName("btnSignUp1")
        self.btnLogin1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin1.setGeometry(QtCore.QRect(340, 490, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin1.setFont(font)
        self.btnLogin1.setObjectName("btnLogin1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 440, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 21))
        self.menubar.setObjectName("menubar")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDisplay = QtWidgets.QAction(MainWindow)
        self.actionDisplay.setObjectName("actionDisplay")
        self.actionLogOut = QtWidgets.QAction(MainWindow)
        self.actionLogOut.setObjectName("actionLogOut")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuOperations.addAction(self.actionInsert)
        self.menuOperations.addAction(self.actionUpdate)
        self.menuOperations.addAction(self.actionDelete)
        self.menuOperations.addAction(self.actionDisplay)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.actionLogOut)
        self.menuOperations.addAction(self.actionClose)
        self.menubar.addAction(self.menuOperations.menuAction())


        ##############
        self.labelLogin_3  = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin_3 .setGeometry(QtCore.QRect(180, 155, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLogin_3 .setFont(font)
        self.labelLogin_3 .setObjectName("labelLogin_3 ")
        self.txtLoginId = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLoginId.setGeometry(QtCore.QRect(300, 150, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtLoginId.setFont(font)
        self.txtLoginId.setObjectName("txtLoginId")

        self.labelLogin_6  = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin_6 .setGeometry(QtCore.QRect(180, 250, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLogin_6 .setFont(font)
        self.labelLogin_6 .setObjectName("labelLogin_6 ")
        self.txtLoginPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLoginPassword.setGeometry(QtCore.QRect(300, 245, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtLoginPassword.setFont(font)
        self.txtLoginPassword.setObjectName("txtLoginPassword")

        self.btnLogin2 = QtWidgets.QPushButton(self.centralwidget)
        
        self.btnLogin2.setGeometry(QtCore.QRect(300, 370, 151, 61))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin2.setFont(font)
        self.btnLogin2.setObjectName("btnLogin2")
        self.btnCancel2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel2.setGeometry(QtCore.QRect(540, 370, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel2.setFont(font)
        self.btnCancel2.setObjectName("btnCancel2")
        #############
        ##
        self.labelInfo_3  = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo_3 .setGeometry(QtCore.QRect(180, 135, 800, 200))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfo_3 .setFont(font)
        self.labelInfo_3 .setObjectName("labelInfo_3 ")
        self.btnLogOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogOut.setGeometry(QtCore.QRect(330, 360, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogOut.setFont(font)
        self.btnLogOut.setText('LogOut')
        self.btnLogOut.setObjectName("btnLogOut")
        ##
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #listners
        self.showSignUp()
        self.btnCancel2.clicked.connect(self.showSignUp)
        self.btnLogin2.clicked.connect(self.onLogin2)
        
        self.btnLogin1.clicked.connect(self.showLogin)
        self.btnSignUp1.clicked.connect(self.onSignUp)
        self.actionInsert.triggered.connect(self.openInsertWindow)
        self.actionUpdate.triggered.connect(self.openUpdateWindow)
        self.actionDelete.triggered.connect(self.openUpdateWindow)
        self.actionDisplay.triggered.connect(self.openDisplayWindow)
        self.actionLogOut.triggered.connect(self.onActionLogOut)
        self.actionClose.triggered.connect(self.onActionClose)
        self.btnLogOut.clicked.connect(self.onLogOut)
        
        self.actionInsert.setEnabled(False)
        self.actionUpdate.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.actionDisplay.setEnabled(False)
        
        
        if(m1.Data.isLogin):
            self.showMenu()
        #self.show()
    def showMenu(self):
        self.actionInsert.setEnabled(True)
        self.actionUpdate.setEnabled(True)
        self.actionDelete.setEnabled(True)
        self.actionDisplay.setEnabled(True)
    def showSignUp(self):
        self.btnLogin2.hide()
        self.btnCancel2.hide()
        self.txtLoginId.hide()
        self.txtLoginPassword.hide()
        self.labelLogin_6.hide()
        self.labelLogin_3.hide()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()
        self.txtFacultyName.show()
        self.txtFacultyId.show()
        self.txtPassword.show()
        self.btnLogin1.show()
        self.btnSignUp1.show()
        self.labelInfo_3.hide()
        self.btnLogOut.hide()
    def hideAll(self):
        self.btnLogin2.hide()
        self.btnCancel2.hide()
        self.txtLoginId.hide()
        self.txtLoginPassword.hide()
        self.labelLogin_6.hide()
        self.labelLogin_3.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.txtFacultyName.hide()
        self.txtFacultyId.hide()
        self.txtPassword.hide()
        self.btnLogin1.hide()
        self.btnSignUp1.hide()
        self.labelInfo_3.show()
        self.btnLogOut.show()
    def showLogin(self):
        self.btnLogin2.show()
        self.btnCancel2.show()
        self.txtLoginId.show()
        self.txtLoginPassword.show()
        self.labelLogin_6.show()
        self.labelLogin_3.show()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.txtFacultyName.hide()
        self.txtFacultyId.hide()
        self.txtPassword.hide()
        self.btnLogin1.hide()
        self.btnSignUp1.hide()
        self.labelInfo_3.hide()
        self.btnLogOut.hide()
    def openInsertWindow(self):        
        widget = QtWidgets.QDialog()
        ui=Ui_DialogInsert()
        ui.setupUi(widget)
        widget.exec_()

    def openUpdateWindow(self):
        myquery = ("select * from student")
        command.execute(myquery)
        isDataAvailable=False
        for rec in command:
            print("for")
            if(m1.Data.currLogin_id == int(rec[8]) and  (len(str(rec[0])) != 0)):
                print("if")
                isDataAvailable=True
                
        if(isDataAvailable):
            widget = QtWidgets.QDialog()
            ui=Ui_DialogUpdate()
            ui.setupUi(widget)
            widget.exec_()
        else:
            QMessageBox.information(self,"Message ","Sorry You Don't Have Any Data!!", QMessageBox.Ok)

    def openDisplayWindow(self):
        widget = QtWidgets.QDialog()
        ui=Ui_DialogDisplay()
        ui.setupUi(widget)
        widget.exec_()
    def onActionLogOut(self):
        self.showSignUp()
        m1.Data.isLogin=False
        self.actionInsert.setEnabled(False)
        self.actionUpdate.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.actionDisplay.setEnabled(False)
    def onActionClose(self):
        MainWindow.close()
    def onLogin2(self):
        enteredId=self.txtLoginId.text()
        enteredPassword=self.txtLoginPassword.text()
        myquery = ("SELECT * FROM faculty")
        command.execute(myquery)
        count=0
        for rec in command:
            if((int(rec[1])==int(enteredId)) and (rec[2]==enteredPassword)):
                count+=1
                m1.Data.currLogin_id=int(enteredId)
                m1.Data.currLogin_password=enteredPassword
                print("Login Successfull")
                QMessageBox.information(self,"Success " " ","Login SuccessFull!!", QMessageBox.Ok)
               
                print(m1.Data.currLogin_id)
                print(m1.Data.currLogin_password)
                self.txtLoginId.setText(" ")
                self.txtLoginPassword.setText(" ")
                #Dialog.hide()
                m1.Data.isLogin=True
                self.txtLoginId.setText(" ")
                self.txtLoginPassword.setText(" ")
                self.showMenu()
                self.hideAll()
                self.labelInfo_3.setText("You Are Login As "+str(rec[0]))
                #self.closeWindow()
                #break
             
        if(count==0):
            print("Wrong Id or Password")
            QMessageBox.information(self,"Error " " ","Wrong Id or Password!!", QMessageBox.Ok)

            m1.Data.currLogin_id=0
            m1.Data.currLogin_password=' '
            self.txtLoginId.setText(" ")
            self.txtLoginPassword.setText(" ")
        
    def onSignUp(self):
        o1=m1.Faculty(self.txtFacultyName.text(),int(self.txtFacultyId.text()),self.txtPassword.text())
        print(o1.getName(),o1.getId(),o1.getPassword())
        
        try:
            myquery = ("insert into faculty values ('"+o1.getName()+"',"+str(o1.getId())+",'"+o1.getPassword()+"')")
            command.execute(myquery)
            print("Inserted Successfully")
            cn.commit()
            QMessageBox.information(self,"Success " " ","Sign Up SuccessFull!!", QMessageBox.Ok)
            self.showLogin()
            '''
            m1.Data.isLogin=True
            self.menuInsert.setEnabled(True)
            self.menuUpdate.setEnabled(True)
            self.menuDelete.setEnabled(True)
            self.menuDisplay.setEnabled(True)
            
            self.hideAll()
            '''
            #self.txtFacultyName.setText("")
            #self.txtFacultyId.setText("")
            #self.txtPassword.setText("")
        except Exception as err:
            QMessageBox.information(self,"Error!" " ","Internal Server Error!!", QMessageBox.Ok)
            print("Error!! {}".format(err))
            
        
 
    def onLogOut(self):
        self.showSignUp()
        m1.Data.isLogin=False
        self.actionInsert.setEnabled(False)
        self.actionUpdate.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.actionDisplay.setEnabled(False)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management System"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.btnSignUp1.setText(_translate("MainWindow", "Sign Up"))
        self.label_3.setText(_translate("MainWindow", "User Id "))
        self.label_5.setText(_translate("MainWindow", "OR"))
        self.btnLogin1.setText(_translate("MainWindow", "Login"))
        self.menuOperations.setTitle(_translate("MainWindow", "Data"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDisplay.setText(_translate("MainWindow", "Display"))
        self.actionLogOut.setText(_translate("MainWindow", "Log Out"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        ###############
        self.labelLogin_6 .setText(_translate("MainWindow", "Password"))
        self.labelLogin_3 .setText(_translate("MainWindow", "User Id "))
        self.btnLogin2.setText(_translate("MainWindow", "Login"))
        self.btnCancel2.setText(_translate("MainWindow", "Cancel"))
        ####
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
