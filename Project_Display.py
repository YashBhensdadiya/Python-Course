from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import Model_1 as m1
cn = mysql.connector.connect(user='root',password='',host='localhost',database='project')
command = cn.cursor()
import sys
class Ui_DialogDisplay(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1028, 684)
        self.btnDisplayAll = QtWidgets.QPushButton(Dialog)
        self.btnDisplayAll.setGeometry(QtCore.QRect(20, 80, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnDisplayAll.setFont(font)
        self.btnDisplayAll.setObjectName("btnDisplayAll")
        self.btnDisplaySpecific = QtWidgets.QPushButton(Dialog)
        self.btnDisplaySpecific.setGeometry(QtCore.QRect(630, 130, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnDisplaySpecific.setFont(font)
        self.btnDisplaySpecific.setObjectName("btnDisplaySpecific")
        self.comboBoxRoll = QtWidgets.QComboBox(Dialog)
        self.comboBoxRoll.setGeometry(QtCore.QRect(710, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxRoll.setFont(font)
        self.comboBoxRoll.setObjectName("comboBoxRoll")
        self.dataTable = QtWidgets.QTableWidget(Dialog)
        self.dataTable.setGeometry(QtCore.QRect(10, 220, 991, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataTable.setFont(font)
        self.dataTable.setRowCount(20)
        self.dataTable.setColumnCount(10)
        self.dataTable.setObjectName("dataTable")
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(840, 620, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 60, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #######Listnere
        self.btnDisplayAll.clicked.connect(self.displayAll)
        self.btnDisplaySpecific.clicked.connect(self.displaySpecific)
        self.btnClose.clicked.connect(self.onClose)
        #self.btnClose.clicked.connect(lambda:self.close())
        self.displayRollNo()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Display"))
        self.btnClose.setText(_translate("Dialog", "Close"))
        self.btnDisplayAll.setText(_translate("Dialog", "Display All Records"))
        self.btnDisplaySpecific.setText(_translate("Dialog", "Display "))
        self.label.setText(_translate("Dialog", "Select Rol No. for Display Data"))

    def displayAll(self):
        myquery = ("select * from student")
        command.execute(myquery)
        self.dataTable.setRowCount(0)
        row_num=0
        col_num=0
        
        for row_data in command:
            col_num=0
            self.dataTable.insertRow(row_num)
            for col_data in row_data:
                self.dataTable.setItem(row_num ,col_num ,QtWidgets.QTableWidgetItem(str(col_data)))
                col_num+=1
            row_num+=1

    def displaySpecific(self):
        while(self.dataTable.rowCount() >0):
            self.dataTable.removeRow(0)
        roll=int(self.comboBoxRoll.currentText())
        myquery = "select * from student"
        command.execute(myquery)
        self.dataTable.setRowCount(0)
        row_num=0
        col_num=0
        
        for row_data in command:
            if(roll == int(row_data[0])):
                col_num=0
                self.dataTable.insertRow(row_num)
                for col_data in row_data:
                    self.dataTable.setItem(row_num ,col_num ,QtWidgets.QTableWidgetItem(str(col_data)))
                    col_num+=1
                row_num+=1

    def displayRollNo(self):
        
        myquery = ("select * from student")
        command.execute(myquery)
        
        self.comboBoxRoll.clear()
        for rec in command:
            self.comboBoxRoll.addItem(str(rec[0]))
    
    def onClose(self):
        Dialog.close()
    
if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogDisplay()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
