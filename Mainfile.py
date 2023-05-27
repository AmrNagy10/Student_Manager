from PyQt5 import QtWidgets
from PyQt5 import uic , QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import os
import sys
import shutil
import time
import sqlite3
import dataBase
from playsound import playsound

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
playsound('mohammed_enhanced.wav')

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.show()
        pygame.init()
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        uic.loadUi('Student_manager.ui', self)
        self.setWindowTitle("Student Manager")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.move(-1, 1)
        self.show_data()
        self.radioButton.setChecked(1)
        self.button()
        self.set_mnon()
        self.warning_box = None

    def button(self):
        self.pushButton_4.clicked.connect(self.set_student)
        self.pushButton_14.clicked.connect(self.empty_fields)
        self.tableView.clicked.connect(self.table_clicked)
        self.pushButton_7.clicked.connect(self.search)
        self.pushButton_11.clicked.connect(self.show_data)
        self.pushButton_8.clicked.connect(self.modifying)
        self.pushButton_5.clicked.connect(self.delete_student)
        self.pushButton_13.clicked.connect(self.backup)

    def table_clicked(self, index):
        row = index.row()
        data = []
        model = self.tableView.model()
        for column in range(model.columnCount()):
            index = model.index(row, column)
            data.append(model.data(index))
        if data[4] == 'Male':
            st = 0
        elif data[4] == 'Female':
            st = 1
        else:
            st = 0
        self.spinBox_3.setValue(int(data[0]))
        self.spinBox_2.setValue(int(data[7]))
        self.lineEdit.setText(data[1])
        self.lineEdit_2.setText(data[2])
        self.lineEdit_3.setText(data[3])
        self.lineEdit_7.setText(data[8])
        self.lineEdit_8.setText(data[9])
        self.comboBox.setCurrentIndex(st)
        st = None

        def redio__button():
            if data[5] == 'In Group':
                self.radioButton.setChecked(1)
            elif data[5] == 'private':
                self.radioButton_2.setChecked(1)

        def check():
            if data[6] == 'True':
                self.checkBox_2.setChecked(True)
            elif data[6] == 'False':
                self.checkBox_2.setChecked(False)

        check()
        redio__button()

    def sender(self):
        self.id = self.spinBox_3.value()
        self.Student_Name = self.lineEdit.text()
        self.Father_Name = self.lineEdit_2.text()
        self.Family_Name = self.lineEdit_3.text()
        self.Gender = self.comboBox.currentText()
        self.Status = self.radioButton.isChecked()
        self.Status_2 = self.radioButton_2.isChecked()
        self.payed = self.checkBox_2.isChecked()
        self.Age = self.spinBox_2.value()
        self.Father_Number = self.lineEdit_7.text()
        self.Student_Number = self.lineEdit_8.text()
        self.Search_data = self.lineEdit_4.text()
        self.itisitis_ingrup_or_private = True
        self.payedornot = True

    def set_student(self):
        self.show_data()
        self.errors()
        self.sender()
        if self.radioButton.isChecked():
            self.itisitis_ingrup_or_private = "In Group"
        else:
            self.itisitis_ingrup_or_private = "private"

        if self.checkBox_2.isChecked():
            self.payedornot = "True"
        else:
            self.payedornot = "False"
        conn = sqlite3.connect("Student_Manager.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM studentData WHERE Student_Name LIKE ''")
        conn.commit()
        try:
            dataBase.Set_data(
                self.id,
                self.Student_Name,
                self.Father_Name,
                self.Family_Name,
                self.Gender,
                self.itisitis_ingrup_or_private,
                self.payedornot,
                self.Age,
                self.Father_Number,
                self.Student_Number,
            )
        except:
            conn = sqlite3.connect("Student_Manager.db")
            cursor = conn.cursor()
            ids = int((list(cursor.execute('select id from studentData'))[-1][0]) + 1)
            conn.commit()
            conn.close()
            dataBase.Set_data(
                ids,
                self.Student_Name,
                self.Father_Name,
                self.Family_Name,
                self.Gender,
                self.itisitis_ingrup_or_private,
                self.payedornot,
                self.Age,
                self.Father_Number,
                self.Student_Number,
            )
            ids = None
            self.payedornot = None
            self.itisitis_ingrup_or_private = None
            self.show_data()
        conn = sqlite3.connect("Student_Manager.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM studentData WHERE Student_Name LIKE ''")
        conn.commit()

    def errors(self):
        if self.lineEdit.text() == '' and self.lineEdit_2.text() == '' and self.lineEdit_3 == '':
            conn = sqlite3.connect("Student_Manager.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM studentData WHERE Student_Name LIKE ''")
            conn.commit()
            self.warning_box = QMessageBox()
            self.warning_box.setIcon(QMessageBox.Warning)
            self.warning_box.setWindowTitle("An error has occurred")
            self.warning_box.setText('make sure you entered all Required data')
            self.warning_box.setStandardButtons(QMessageBox.Ok)
            self.warning_box.exec_()


        elif self.lineEdit.text() == '' or self.lineEdit_3 == '':
            conn = sqlite3.connect("Student_Manager.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM studentData WHERE Student_Name LIKE ''")
            conn.commit()
            self.warning_box = QMessageBox()
            self.warning_box.setIcon(QMessageBox.Warning)
            self.warning_box.setWindowTitle("An error has occurred")
            self.warning_box.setText('make sure you entered all Required data')
            self.warning_box.setStandardButtons(QMessageBox.Ok)
            self.warning_box.exec_()

    def empty_fields(self):
        self.show_data()
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_7.setText('+20')
        self.lineEdit_8.setText('+20')
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.removeItem(-1)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_2.removeItem(-1)
        self.radioButton.setChecked(1)
        self.radioButton_2.setChecked(0)
        self.checkBox_2.setChecked(False)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.lineEdit_4.setText('')

    def show_data(self):
        dataBase.__init__()
        conn = sqlite3.connect("Student_Manager.db")
        cursor = conn.cursor()
        # execute a query to retrieve data from the database
        cursor.execute("SELECT * FROM studentData")
        rows = cursor.fetchall()
        # create a standard item model and set the number of rows and columns
        model = QStandardItemModel()

        if len(rows) > 0:
            model.setColumnCount(len(rows[0]))
        else:
            model.setColumnCount(0)
        for row in rows:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Student Name')
        model.setHeaderData(2, Qt.Horizontal, 'Father Name')
        model.setHeaderData(3, Qt.Horizontal, 'Family Name')
        model.setHeaderData(4, Qt.Horizontal, 'Gender')
        model.setHeaderData(5, Qt.Horizontal, 'Status')
        model.setHeaderData(6, Qt.Horizontal, 'Payed')
        model.setHeaderData(7, Qt.Horizontal, 'Age')
        model.setHeaderData(8, Qt.Horizontal, 'Father Number')
        model.setHeaderData(9, Qt.Horizontal, 'Student Number')
        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.show()
        row = 0
        rows = 0
        item = 0
        items = 0
        model = None
        conn.commit()
        conn.close()

    def modifying(self):
        data = sqlite3.connect('Student_Manager.db')
        con = data.cursor()

        if (list(con.execute(f"select Student_Name from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.lineEdit.text():
            con.execute("UPDATE studentData SET Student_Name = ? WHERE id = ?",
                        (self.lineEdit.text(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Father_Name from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.lineEdit_2.text():
            con.execute("UPDATE studentData SET Father_Name = ? WHERE id = ?",
                        (self.lineEdit_2.text(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Family_Name from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.lineEdit_3.text():
            con.execute("UPDATE studentData SET Family_Name = ? WHERE id = ?",
                        (self.lineEdit_3.text(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Gender from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.comboBox.currentText():
            con.execute("UPDATE studentData SET Gender = ? WHERE id = ?",
                        (self.comboBox.currentText(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Father_Number from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.lineEdit_7.text():
            con.execute("UPDATE studentData SET Father_Number = ? WHERE id = ?",
                        (self.lineEdit_7.text(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Student_Number from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.lineEdit_8.text():
            con.execute("UPDATE studentData SET Student_Number = ? WHERE id = ?",
                        (self.lineEdit_8.text(), self.spinBox_3.value()))
            data.commit()

        if (list(con.execute(f"select Age from studentData WHERE id = {self.spinBox_3.value()}"))[0][
            0]) != self.spinBox_2.value():
            con.execute("UPDATE studentData SET Age = ? WHERE id = ?", (self.spinBox_2.value(), self.spinBox_3.value()))
            data.commit()

        if self.radioButton.isChecked():
            con.execute("UPDATE studentData SET Status = ? WHERE id = ?", ('In Group', self.spinBox_3.value()))
            data.commit()

        if self.radioButton_2.isChecked():
            con.execute("UPDATE studentData SET Status = ? WHERE id = ?", ('private', self.spinBox_3.value()))
            data.commit()

        if self.checkBox_2.isChecked():
            con.execute("UPDATE studentData SET payed = ? WHERE id = ?", ('True', self.spinBox_3.value()))
            data.commit()

        if self.checkBox_2.isChecked() == False:
            con.execute("UPDATE studentData SET payed = ? WHERE id = ?", ('False', self.spinBox_3.value()))
            data.commit()
        self.show_data()

    def delete_student(self):
        conn = sqlite3.connect("Student_Manager.db")
        cursor = conn.cursor()
        id = self.spinBox_3.value()
        cursor.execute("DELETE FROM studentData WHERE id = ?", (id,))
        conn.commit()
        self.show_data()

    def search(self):
        data = None
        using = None
        using = self.lineEdit_4.text()
        data = sqlite3.connect('Student_Manager.db')
        con = data.cursor()
        if using == '':
            self.warning_box = QMessageBox()
            self.warning_box.setIcon(QMessageBox.Warning)
            self.warning_box.setWindowTitle("Search using what")
            self.warning_box.setText('What do you want to search for and how')
            self.warning_box.setStandardButtons(QMessageBox.Ok)
            self.warning_box.exec_()

        if self.comboBox_2.currentText() == 'ID':
            at = list(con.execute(f'SELECT * FROM studentData WHERE id = {using}'))
            ids = int((list(con.execute('select id from studentData'))[-1][0])+1)
            if int(using) <= ids:
                try:
                    if at is not None:
                        model = QStandardItemModel()
                        if len(at) > 0:
                            model.setColumnCount(len(at[0]))
                        else:
                            model.setColumnCount(0)
                        for row in at:
                            items = [QStandardItem(str(item)) for item in row]
                            model.appendRow(items)
                        model.setHeaderData(0, Qt.Horizontal, 'ID')
                        model.setHeaderData(1, Qt.Horizontal, 'Student Name')
                        model.setHeaderData(2, Qt.Horizontal, 'Father Name')
                        model.setHeaderData(3, Qt.Horizontal, 'Family Name')
                        model.setHeaderData(4, Qt.Horizontal, 'Gender')
                        model.setHeaderData(5, Qt.Horizontal, 'Status')
                        model.setHeaderData(6, Qt.Horizontal, 'Payed')
                        model.setHeaderData(7, Qt.Horizontal, 'Age')
                        model.setHeaderData(8, Qt.Horizontal, 'Father Number')
                        model.setHeaderData(9, Qt.Horizontal, 'Student Number')
                        self.tableView.setModel(model)
                        self.tableView.setSortingEnabled(True)
                        self.tableView.setSelectionBehavior(QTableView.SelectRows)
                        self.tableView.horizontalHeader().setStretchLastSection(True)
                        self.tableView.show()

                    else:
                        self.warning_box = QMessageBox()
                        self.warning_box.setIcon(QMessageBox.Warning)
                        self.warning_box.setWindowTitle("Search")
                        self.warning_box.setText('ID Not found')
                        self.warning_box.setStandardButtons(QMessageBox.Ok)
                        self.warning_box.exec_()
                except:
                    self.warning_box = QMessageBox()
                    self.warning_box.setIcon(QMessageBox.Warning)
                    self.warning_box.setWindowTitle("Search")
                    self.warning_box.setText("Somthing is't true")
                    self.warning_box.setStandardButtons(QMessageBox.Ok)
                    self.warning_box.exec_()

        elif self.comboBox_2.currentText() == 'Name':
            at = list(con.execute("SELECT * FROM studentData WHERE Student_Name LIKE ?", (using,)))
            try:
                    if at is not None:
                        model = QStandardItemModel()
                        if len(at) > 0:
                            model.setColumnCount(len(at[0]))
                        else:
                            model.setColumnCount(0)
                        for row in at:
                            items = [QStandardItem(str(item)) for item in row]
                            model.appendRow(items)
                        model.setHeaderData(0, Qt.Horizontal, 'ID')
                        model.setHeaderData(1, Qt.Horizontal, 'Student Name')
                        model.setHeaderData(2, Qt.Horizontal, 'Father Name')
                        model.setHeaderData(3, Qt.Horizontal, 'Family Name')
                        model.setHeaderData(4, Qt.Horizontal, 'Gender')
                        model.setHeaderData(5, Qt.Horizontal, 'Status')
                        model.setHeaderData(6, Qt.Horizontal, 'Payed')
                        model.setHeaderData(7, Qt.Horizontal, 'Age')
                        model.setHeaderData(8, Qt.Horizontal, 'Father Number')
                        model.setHeaderData(9, Qt.Horizontal, 'Student Number')
                        self.tableView.setModel(model)
                        self.tableView.setSortingEnabled(True)
                        self.tableView.setSelectionBehavior(QTableView.SelectRows)
                        self.tableView.horizontalHeader().setStretchLastSection(True)
                        self.tableView.show()
                    else:
                        self.warning_box = QMessageBox()
                        self.warning_box.setIcon(QMessageBox.Warning)
                        self.warning_box.setWindowTitle("Search")
                        self.warning_box.setText('Name Not found')
                        self.warning_box.setStandardButtons(QMessageBox.Ok)
                        self.warning_box.exec_()
            except:
                    self.warning_box = QMessageBox()
                    self.warning_box.setIcon(QMessageBox.Warning)
                    self.warning_box.setWindowTitle("Search")
                    self.warning_box.setText("Somthing is't true")
                    self.warning_box.setStandardButtons(QMessageBox.Ok)
                    self.warning_box.exec_()

        elif self.comboBox_2.currentText() == 'Age':
            at = list(con.execute("SELECT * FROM studentData WHERE Age LIKE ?", (using,)))
            try:
                    if at is not None:
                        model = QStandardItemModel()
                        if len(at) > 0:
                            model.setColumnCount(len(at[0]))
                        else:
                            model.setColumnCount(0)
                        for row in at:
                            items = [QStandardItem(str(item)) for item in row]
                            model.appendRow(items)
                        model.setHeaderData(0, Qt.Horizontal, 'ID')
                        model.setHeaderData(1, Qt.Horizontal, 'Student Name')
                        model.setHeaderData(2, Qt.Horizontal, 'Father Name')
                        model.setHeaderData(3, Qt.Horizontal, 'Family Name')
                        model.setHeaderData(4, Qt.Horizontal, 'Gender')
                        model.setHeaderData(5, Qt.Horizontal, 'Status')
                        model.setHeaderData(6, Qt.Horizontal, 'Payed')
                        model.setHeaderData(7, Qt.Horizontal, 'Age')
                        model.setHeaderData(8, Qt.Horizontal, 'Father Number')
                        model.setHeaderData(9, Qt.Horizontal, 'Student Number')
                        self.tableView.setModel(model)
                        self.tableView.setSortingEnabled(True)
                        self.tableView.setSelectionBehavior(QTableView.SelectRows)
                        self.tableView.horizontalHeader().setStretchLastSection(True)
                        self.tableView.show()
                    else:
                        self.warning_box = QMessageBox()
                        self.warning_box.setIcon(QMessageBox.Warning)
                        self.warning_box.setWindowTitle("Search")
                        self.warning_box.setText('Age Not found')
                        self.warning_box.setStandardButtons(QMessageBox.Ok)
                        self.warning_box.exec_()
            except:
                    self.warning_box = QMessageBox()
                    self.warning_box.setIcon(QMessageBox.Warning)
                    self.warning_box.setWindowTitle("Search")
                    self.warning_box.setText("Somthing is't true")
                    self.warning_box.setStandardButtons(QMessageBox.Ok)
                    self.warning_box.exec_()
        else:
            self.warning_box = QMessageBox()
            self.warning_box.setIcon(QMessageBox.Warning)
            self.warning_box.setWindowTitle("Search using what")
            self.warning_box.setText('')
            self.warning_box.setStandardButtons(QMessageBox.Ok)
            self.warning_box.exec_()

    def backup(self):
        directory_path = "Backup"
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        source_file = "Student_Manager.db"
        destination_file = "Backup/DataBase.db"
        shutil.copyfile(source_file, destination_file)

    def set_mnon(self):
        aynum = time.localtime().tm_mday
        monnum = time.localtime().tm_mon
        with open('monoseters.txt', 'a') as fil:
            fil.write(f"{str(monnum)} \n")
        if aynum == 1:
            print('hello man')
            self.reset()

    def reset(self):
        daynum = time.localtime().tm_mday
        monnum = time.localtime().tm_mon
        if daynum == 1:
            with open('monoseters.txt', 'r') as f:
                text = f.readlines()[2]
            print(text)
            if text != monnum:
                con = sqlite3.connect("Student_Manager.db")
                Curso = con.cursor()
                ids = int((list(Curso.execute('select id from studentData'))[-1][0]) + 1)
                for i in range(0 , ids+1):
                    Curso.execute("UPDATE studentData SET payed = ? WHERE id = ?",('False', i))
                con.commit()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
