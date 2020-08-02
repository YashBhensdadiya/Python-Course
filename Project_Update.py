from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,QInputDialog, QApplication,QMessageBox)
import sys
import mysql.connector
import Model_1 as m1
cn = mysql.connector.connect(user='root',password='',host='localhost',database='project')
command = cn.cursor()

class Ui_DialogUpdate(QWidget):
    selectedRoll=0
    selectedRadio=''
    rollList=[]
    def hideFields(self):
        self.txtStdCity.setEnabled(False)
        self.txtStdName.setEnabled(False)
        #self.btnCancel3.setEnabled(False)
        self.radiobtnFemale.setEnabled(False)
        self.txtStdRoll.setEnabled(False)
        self.radiobtnMale.setEnabled(False)
        self.dropDownSemester.setEnabled(False)
        self.dropDownBranch.setEnabled(False)
        self.txtStdGrade.setEnabled(False)
        self.txtStdMobile.setEnabled(False)
        self.radiobtnOther.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnUpdateSave.setEnabled(False)

    def showFields(self):
        self.txtStdCity.setEnabled(True)
        self.txtStdName.setEnabled(True)
        #self.btnCancel3.setEnabled(True)
        self.radiobtnFemale.setEnabled(True)
        self.txtStdRoll.setEnabled(True)
        self.radiobtnMale.setEnabled(True)
        self.dropDownSemester.setEnabled(True)
        self.dropDownBranch.setEnabled(True)
        self.txtStdGrade.setEnabled(True)
        self.txtStdMobile.setEnabled(True)
        self.radiobtnOther.setEnabled(True)
        self.btnDelete.setEnabled(True)
        self.btnUpdateSave.setEnabled(True)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(841, 700)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.dropDownRoll = QtWidgets.QComboBox(Dialog)
        self.dropDownRoll.setGeometry(QtCore.QRect(420, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dropDownRoll.setFont(font)
        self.dropDownRoll.setObjectName("dropDownRoll")
        self.btnSelectRoll = QtWidgets.QPushButton(Dialog)
        self.btnSelectRoll.setGeometry(QtCore.QRect(700, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnSelectRoll.setFont(font)
        self.btnSelectRoll.setObjectName("btnSelectRoll")
        
        self.btnUpdateSave = QtWidgets.QPushButton(Dialog)
        self.btnUpdateSave.setGeometry(QtCore.QRect(610, 200, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdateSave.setFont(font)
        self.btnUpdateSave.setObjectName("btnUpdateSave")
        self.txtStdCity = QtWidgets.QLineEdit(Dialog)
        self.txtStdCity.setGeometry(QtCore.QRect(210, 470, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdCity.setFont(font)
        self.txtStdCity.setObjectName("txtStdCity")
        self.txtStdName = QtWidgets.QLineEdit(Dialog)
        self.txtStdName.setGeometry(QtCore.QRect(210, 200, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdName.setFont(font)
        self.txtStdName.setObjectName("txtStdName")
        self.btnCancel3 = QtWidgets.QPushButton(Dialog)
        self.btnCancel3.setGeometry(QtCore.QRect(610, 440, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel3.setFont(font)
        self.btnCancel3.setObjectName("btnCancel3")
        self.radiobtnFemale = QtWidgets.QRadioButton(Dialog)
        self.radiobtnFemale.setGeometry(QtCore.QRect(300, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnFemale.setFont(font)
        self.radiobtnFemale.setObjectName("radiobtnFemale")
        self.txtStdRoll = QtWidgets.QLineEdit(Dialog)
        self.txtStdRoll.setGeometry(QtCore.QRect(210, 130, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdRoll.setFont(font)
        self.txtStdRoll.setObjectName("txtStdRoll")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radiobtnMale = QtWidgets.QRadioButton(Dialog)
        self.radiobtnMale.setGeometry(QtCore.QRect(210, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnMale.setFont(font)
        self.radiobtnMale.setObjectName("radiobtnMale")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dropDownSemester = QtWidgets.QComboBox(Dialog)
        self.dropDownSemester.setGeometry(QtCore.QRect(210, 400, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropDownSemester.setFont(font)
        self.dropDownSemester.setObjectName("dropDownSemester")
        self.dropDownBranch = QtWidgets.QComboBox(Dialog)
        self.dropDownBranch.setGeometry(QtCore.QRect(210, 330, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dropDownBranch.setFont(font)
        self.dropDownBranch.setObjectName("dropDownBranch")
        self.txtStdGrade = QtWidgets.QLineEdit(Dialog)
        self.txtStdGrade.setGeometry(QtCore.QRect(210, 610, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdGrade.setFont(font)
        self.txtStdGrade.setText("")
        self.txtStdGrade.setObjectName("txtStdGrade")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 550, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 340, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtStdMobile = QtWidgets.QLineEdit(Dialog)
        self.txtStdMobile.setGeometry(QtCore.QRect(210, 540, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStdMobile.setFont(font)
        self.txtStdMobile.setObjectName("txtStdMobile")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 480, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radiobtnOther = QtWidgets.QRadioButton(Dialog)
        self.radiobtnOther.setGeometry(QtCore.QRect(410, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiobtnOther.setFont(font)
        self.radiobtnOther.setObjectName("radiobtnOther")
        self.btnDelete = QtWidgets.QPushButton(Dialog)
        self.btnDelete.setGeometry(QtCore.QRect(610, 320, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        


        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #################
        self.hideFields()
        self.DisplayRollNo()
        self.btnSelectRoll.clicked.connect(self.onSelect)
        self.btnUpdateSave.clicked.connect(self.onSave)
        self.btnCancel3.clicked.connect(self.onCancel3)
        self.btnDelete.clicked.connect(self.onDelete)
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update or Delete"))
        self.label_10.setText(_translate("Dialog", "Select  Roll No. for Update or Delete"))
        self.btnUpdateSave.setText(_translate("Dialog", "Save"))
        self.btnCancel3.setText(_translate("Dialog", "Cancel"))
        self.radiobtnFemale.setText(_translate("Dialog", "Female"))
        self.label_7.setText(_translate("Dialog", "Gender"))
        self.label.setText(_translate("Dialog", "Roll No."))
        self.radiobtnMale.setText(_translate("Dialog", "Male"))
        self.label_8.setText(_translate("Dialog", "Grade"))
        self.label_5.setText(_translate("Dialog", "Mobile No."))
        self.label_3.setText(_translate("Dialog", "Branch"))
        self.label_6.setText(_translate("Dialog", "Semester"))
        self.label_4.setText(_translate("Dialog", "City"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.radiobtnOther.setText(_translate("Dialog", "Other"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.btnSelectRoll.setText(_translate("Dialog", "Select"))

    def DisplayRollNo(self):
        
        myquery = ("select * from student")
        command.execute(myquery)
        self.dropDownRoll.clear()
        for rec in command:
            if(m1.Data.currLogin_id == int(rec[8])):
                self.dropDownRoll.addItem(str(rec[0]))
        
    def onSelect(self):
        self.selectedRoll=int(self.dropDownRoll.currentText())
        self.showFields()
        
        myquery = "select * from student"
        command.execute(myquery)
        for rec in command:
            if(self.selectedRoll == int(rec[0])):
                self.txtStdRoll.setText(str(rec[0]))
                self.txtStdName.setText(str(rec[1]))
                self.selectedRadio=str(rec[2])
                self.selectedBranch=str(rec[3])
                self.selectedSemester=int(rec[4])
                
                
                print(rec[2])
                if (rec[2]=='Male'):
                    self.radiobtnMale.setChecked(True)
                if (rec[2]=='Female'):
                    self.radiobtnFemale.setChecked(True)
                if (rec[2]=='Other'):
                    self.radiobtnOther.setChecked(True)
                for item in m1.Data.branchList:
                    self.dropDownBranch.addItem(item)
                for item in m1.Data.SemesterList:
                    self.dropDownSemester.addItem(str(item))
                self.dropDownBranch.setCurrentText(str(rec[3]))
                self.dropDownSemester.setCurrentText(str(rec[4]))
                
                self.txtStdCity.setText(str(rec[5]))
                self.txtStdMobile.setText(str(rec[6]))
                self.txtStdGrade.setText(str(rec[7]))
                
        
    def onSave(self):
        branch=''
        semester=''
        stdRoll=(self.txtStdRoll.text())
        stdName=self.txtStdName.text()
        stdCity=self.txtStdCity.text()
        stdMobile=(self.txtStdMobile.text())
        stdGrade=self.txtStdGrade.text()
        if (self.radiobtnMale.isChecked()):
            self.selectedRadio='Male'
        elif (self.radiobtnFemale.isChecked()):
            self.selectedRadio='Female'
        elif (self.radiobtnOther.isChecked()):
            self.selectedRadio='Other'
        
        branch=self.dropDownBranch.currentText()
        branch=self.dropDownBranch.currentText()
        semester=int(self.dropDownSemester.currentText())
        
        try:
            myquery = "update student set roll={},name='{}',gender='{}',branch='{}',semester={},city='{}',mobile={},grade={} where roll={};".format(stdRoll,stdName,self.selectedRadio,branch,semester,stdCity,stdMobile,stdGrade,self.selectedRoll)
            command.execute(myquery)
            cn.commit()
            self.DisplayRollNo()
            print("Updated Successfully")
            QMessageBox.information(self,"Success ","Updated SuccessFully!!", QMessageBox.Ok)
        except Exception as err:
            print("Error!! {}".format(err))
            QMessageBox.information(self,"Error!!!" ,str(err),QMessageBox.Ok)
        
    def onDelete(self):
        result = QMessageBox.question(self, "Delete Data", "Are You Sure ?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(result == QMessageBox.Yes): 
            try:
                myquery = "delete from student where roll={};".format(self.selectedRoll)
                command.execute(myquery)
                cn.commit()
                self.DisplayRollNo()
                stdRoll=(self.txtStdRoll.setText(""))
                stdName=self.txtStdName.setText("")
                stdCity=self.txtStdCity.setText("")
                stdMobile=(self.txtStdMobile.setText(""))
                stdGrade=self.txtStdGrade.setText("")
                print("Deleted Successfully")
            except Exception as err:
                print("Error!! {}".format(err))
        else:
            pass
        
    def onCancel3(self):
        sys.exit(exec_())
        #Dialog.close()
    
'''           
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogUpdate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''
