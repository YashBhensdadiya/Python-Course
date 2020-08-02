from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,QInputDialog, QApplication,QMessageBox)
import Model_1 as m1

import mysql.connector
cn = mysql.connector.connect(user='root',password='',host='localhost',database='project')
command = cn.cursor()
import sys
class Ui_DialogInsert(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(676, 716)
        self.txtStdRoll = QtWidgets.QLineEdit(Dialog)
        self.txtStdRoll.setGeometry(QtCore.QRect(250, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdRoll.setFont(font)
        self.txtStdRoll.setObjectName("txtStdRoll")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.txtStdName = QtWidgets.QLineEdit(Dialog)
        self.txtStdName.setGeometry(QtCore.QRect(250, 120, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdName.setFont(font)
        self.txtStdName.setObjectName("txtStdName")
        
        self.radiobtnMale = QtWidgets.QRadioButton(Dialog)
        self.radiobtnMale.setGeometry(QtCore.QRect(250, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnMale.setFont(font)
        self.radiobtnMale.setObjectName("radiobtnMale")
        self.radiobtnFemale = QtWidgets.QRadioButton(Dialog)
        self.radiobtnFemale.setGeometry(QtCore.QRect(340, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnFemale.setFont(font)
        self.radiobtnFemale.setObjectName("radiobtnFemale")
        self.radiobtnOther = QtWidgets.QRadioButton(Dialog)
        self.radiobtnOther.setGeometry(QtCore.QRect(450, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnOther.setFont(font)
        self.radiobtnOther.setObjectName("radiobtnOther")
        
        self.dropDownBranch = QtWidgets.QComboBox(Dialog)
        self.dropDownBranch.setGeometry(QtCore.QRect(250, 250, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropDownBranch.setFont(font)
        self.dropDownBranch.setObjectName("dropDownBranch")
        
        self.dropDownSemester = QtWidgets.QComboBox(Dialog)
        self.dropDownSemester.setGeometry(QtCore.QRect(250, 320, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropDownSemester.setFont(font)
        self.dropDownSemester.setObjectName("dropDownSemester")
        self.txtStdCity = QtWidgets.QLineEdit(Dialog)
        self.txtStdCity.setGeometry(QtCore.QRect(250, 390, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdCity.setFont(font)
        self.txtStdCity.setObjectName("txtStdCity")
        self.txtStdMobile = QtWidgets.QLineEdit(Dialog)
        self.txtStdMobile.setGeometry(QtCore.QRect(250, 460, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdMobile.setFont(font)
        self.txtStdMobile.setObjectName("txtStdMobile")
        self.txtStdGrade = QtWidgets.QLineEdit(Dialog)
        self.txtStdGrade.setGeometry(QtCore.QRect(250, 530, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdGrade.setFont(font)
        self.txtStdGrade.setText("")
        self.txtStdGrade.setObjectName("txtStdGrade")
        self.btnSave3 = QtWidgets.QPushButton(Dialog)
        self.btnSave3.setGeometry(QtCore.QRect(160, 610, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave3.setFont(font)
        self.btnSave3.setObjectName("btnSave3")
        self.btnCancel3 = QtWidgets.QPushButton(Dialog)
        self.btnCancel3.setGeometry(QtCore.QRect(370, 610, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel3.setFont(font)
        self.btnCancel3.setObjectName("btnCancel3")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 400, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 470, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 330, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 200, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 540, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ################## listener
        self.btnSave3.clicked.connect(self.onSave3)
        self.btnCancel3.clicked.connect(self.onCancel3)
        #self.btnCancel3.clicked.connect(lambda:self.close())
        #self.btnCancel3.clicked.connect(QtWidgets.QApplication.instance().quit)
        #self.btnCancel3.clicked.connect(app.close())
        ####### ComboBox or DropDown
        
        for item in m1.Data.branchList:
            self.dropDownBranch.addItem(item)
        for item in m1.Data.SemesterList:
            self.dropDownSemester.addItem(str(item))
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert"))
        self.label.setText(_translate("Dialog", "Roll No."))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Branch"))
        self.label_4.setText(_translate("Dialog", "City"))
        self.label_5.setText(_translate("Dialog", "Mobile No."))
        self.btnSave3.setText(_translate("Dialog", "Save"))
        self.btnCancel3.setText(_translate("Dialog", "Cancel"))
        self.label_6.setText(_translate("Dialog", "Semester"))
        self.label_7.setText(_translate("Dialog", "Gender"))
        self.radiobtnMale.setText(_translate("Dialog", "Male"))
        self.radiobtnFemale.setText(_translate("Dialog", "Female"))
        self.radiobtnOther.setText(_translate("Dialog", "Other"))
        self.label_8.setText(_translate("Dialog", "Grade"))
       

    def onSave3(self):
        selectedradio=''
        stdRoll=(self.txtStdRoll.text())
        stdName=self.txtStdName.text()
        stdCity=self.txtStdCity.text()
        stdMobile=(self.txtStdMobile.text())
        stdGrade=self.txtStdGrade.text()
        if (self.radiobtnMale.isChecked()):
            selectedradio='Male'
        if (self.radiobtnFemale.isChecked()):
            selectedradio='Female'
        if (self.radiobtnOther.isChecked()):
            selectedradio='Other'
        
        selectedBranch=self.dropDownBranch.currentText()
        selectedSem=int(self.dropDownSemester.currentText())
        f_id=m1.Data.currLogin_id
        try:
            myquery = "insert into student values("+(stdRoll)+",'"+stdName+"','"+selectedradio+"','"+selectedBranch+"',"+str(selectedSem)+",'"+stdCity+"',"+str(stdMobile)+","+str(stdGrade)+","+str(f_id)+")"
            command.execute(myquery)
            cn.commit()
            QMessageBox.information(self,"Success ","Inserted SuccessFull!!", QMessageBox.Ok)

            print("Data Inserted Successfully")
        except Exception as err:
            QMessageBox.information(self,"Error!!!" ,str(err),QMessageBox.Ok)

            print("Error!! {}".format(err))
    def onCancel3(self):
        print("")
        #self.hide()
        
'''       
if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogInsert()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

'''



    
