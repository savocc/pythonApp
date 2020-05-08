
import sqlite3
from contextlib import closing
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from datetime import datetime
import smtplib, ssl
import ast
from email.mime.multipart import MIMEMultipart
from time import gmtime, strftime                                                     
from email.mime.text import MIMEText
import datetime as dt
import time
from selenium import webdriver
from getpass import getpass
from email.mime.base import MIMEBase
from email import encoders
import schedule 
 


conn = None

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 596)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
       # self.setStyleSheet("background-color: white;") 
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("font: 10pt \"Tw Cen MT\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 10, 0, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 11, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 9, 3, 1, 1, QtCore.Qt.AlignTop)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 10, 3, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("font: 10pt \"Tw Cen MT\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 11, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("font: 10pt \"Tw Cen MT\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 11, 4, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addToOrder)
        self.pushButton.clicked.connect(self.get_items)
        self.pushButton_4.clicked.connect(self.delItem)
        self.pushButton_3.clicked.connect(self.findItem)
        self.pushButton_2.clicked.connect(self.defineFilter)
        self.gridLayout_2.addWidget(self.pushButton, 17, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(256, 0))
        self.dateTimeEdit.setStyleSheet("\n"
"font: 12pt \"Arial\";")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 14, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color: rgb(236, 255, 17);\n"
"font: 28pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 6)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 7, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 8, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 9, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 75 18pt \"Tw Cen MT\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_2.addWidget(self.radioButton_6, 5, 3, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 4, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 3, 1, 3, QtCore.Qt.AlignBottom)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_2.addWidget(self.radioButton_7, 5, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(18)
        font.setBold(False)
        
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 75 18pt \"Tw Cen MT\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 3, QtCore.Qt.AlignBottom)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 331, 211))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget, 14, 1, 5, 5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 16, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 13, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 15, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.get_items()
        self.label_12.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.radioButton_3.raise_()
  
        self.label_9.raise_()
        self.dateTimeEdit.raise_()
        self.pushButton_2.raise_()
        self.radioButton.raise_()
        self.label_4.raise_()
        self.radioButton_2.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.lineEdit.raise_()
        self.radioButton_4.raise_()
        self.radioButton_5.raise_()
        self.radioButton_6.raise_()
        self.label_2.raise_()
        self.radioButton_7.raise_()
        self.label_6.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.Events = QtWidgets.QStatusBar(MainWindow)
        self.Events.setObjectName("Events")
        MainWindow.setStatusBar(self.Events)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Применить"))
        self.label_4.setText(_translate("MainWindow", "Содержание"))
        self.label_9.setText(_translate("MainWindow", "Событие"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Заголовок"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_10.setText(_translate("MainWindow", "                                                                    Event Tracker"))
        self.radioButton_3.setText(_translate("MainWindow", "Задание"))
        self.radioButton_2.setText(_translate("MainWindow", "Звонок"))
        self.radioButton.setText(_translate("MainWindow", "Встреча"))
        self.label_12.setText(_translate("MainWindow", "Добавить событие"))
        self.radioButton_6.setText(_translate("MainWindow", "За год"))
        self.radioButton_4.setText(_translate("MainWindow", "Показать все"))
        self.label_3.setText(_translate("MainWindow", "Тип"))
        self.radioButton_5.setText(_translate("MainWindow", "За  месяц"))
        self.label_7.setText(_translate("MainWindow", "Фильтры отображения"))
        self.radioButton_7.setText(_translate("MainWindow", "За  день"))
        self.label_6.setText(_translate("MainWindow", "Список  "))
        self.label_5.setText(_translate("MainWindow", "Дата"))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>Сообщение с напоминанием будет отправлено на указанный адрес</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Электронная почта"))
        item = self.tableWidget.horizontalHeaderItem(0).setText(_translate("MainWindow", "Заголовок"))
        item = self.tableWidget.horizontalHeaderItem(1).setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(2).setText(_translate("MainWindow", "Содержание"))
        item = self.tableWidget.horizontalHeaderItem(3).setText(_translate("MainWindow", "Дата"))

        
    def connect():
        global conn
        if not conn:
            if sys.platform == "win32":
                DB_FILE = "dbPyt.db"
            else:
                HOME = os.environ["HOME"]
                DB_FILE = HOME + "dbPyt.db"
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
        
    def close():
        if conn:
            conn.close()
            
    def get_items(self):
        self.tableWidget.setRowCount(0)
        query = '''SELECT title, type, content,date
               FROM forEvent'''
        with closing(conn.cursor()) as c:
            c.execute(query)
            results = c.fetchall() 
            if len(results) != 0:
                try:
                    for row in results:
                        self.addTable(self.MyConverter(row))
                    c.close()
                except Exception as e:
                    print(type(e), e)
                    # exit the system when exception is raised
            else:
                return ["0"]
                
    def delItem(self):
        lineEdit = self.lineEdit_3.text()
        lineEdit = str(lineEdit)
        query = '''DELETE FROM forEvent
        WHERE title = ?'''
        with closing(conn.cursor()) as c:
            c.execute(query, (lineEdit,))
        self.get_items() 
        
        
        
    def findItem(self):
        self.tableWidget.setRowCount(0)
        lineEdit = self.lineEdit_3.text()
        query = '''Select title, type,content,date  from forEvent WHERE title = ?'''
        with closing(conn.cursor()) as c:
            c.execute(query, (lineEdit,))
            results = c.fetchall() 
        if len(results) != 0:
            try:
                for row in results:
                    self.addTable(self.MyConverter(row))
                c.close()
            except Exception as e:
                print(type(e), e)
                    # exit the system when exception is raised
        else:
            return ["0"] 
        
    def filterOutput(self,dateTimeEdit, ford):
        self.tableWidget.setRowCount(0)
        query = '''Select title, type,content,date from forEvent'''
        with closing(conn.cursor()) as c:
            c.execute(query, ())
            results = c.fetchall() 
        if len(results) != 0:
            try:
                for row in results:
                    fordate = row["date"]
                    fordate =fordate[:ford]
                    if fordate == dateTimeEdit:
                        self.addTable(self.MyConverter(row))
                c.close()
            except Exception as e:
                print(type(e), e)
                    # exit the system when exception is raised
        else:
            return ["0"]
        
    
                  
    def addTable(self,columns):
        rowPosition = 0
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))
            
    def MyConverter(self,mydata):
        def cvt(data):
            try:
                return ast.literal_eval(data)
            except Exception:
                return str(data)
        return tuple(map(cvt,mydata))
            
    def addToOrder(self):
        lineEdit = self.lineEdit.text()
        if self.radioButton_3.isChecked():
            forType = self.radioButton_3.text()
        elif self.radioButton_2.isChecked():
            forType = self.radioButton_2.text()
        elif self.radioButton.isChecked():
            forType = self.radioButton.text()
        lineEdit_4 =  self.lineEdit_4.text()
        dateTimeEdit = self.dateTimeEdit.text()
        lineEdit_2 = self.lineEdit_2.text()
        # we add item to a database table with order information
        dateTimeEdit = dateTimeEdit[0:16]
        send_time = datetime.strptime(dateTimeEdit,"%Y-%m-%d %I:%M")
        now = datetime.now()
        forCheck = send_time.timestamp() -  time.time()
        if forCheck > 0:
            with closing(conn.cursor()) as c:       
                sql = '''INSERT INTO forEvent (title, type,content,date,mail) 
                VALUES (?,?,?,?,?)'''
                c.execute(sql,(lineEdit,forType,lineEdit_4, dateTimeEdit,lineEdit_2))
                conn.commit()
            time.sleep(3)
            self.sendMail()
        else:
            print("error")
            
    def defineFilter(self):
        checked = 0
        dateTimeObj = datetime.now()
        if self.radioButton_4.isChecked():
            checked = 1
            forFilter1 = self.radioButton_4.text()
        elif self.radioButton_6.isChecked():
            checked = 2
            forFilter2 = self.radioButton_6.text()
            dateTimeEdit = dateTimeObj.strftime("%Y")
        elif self.radioButton_5.isChecked():
            checked = 3
            forFilter3 = self.radioButton_5.text()
            dateTimeEdit = dateTimeObj.strftime("%Y-%m")
        elif self.radioButton_7.isChecked():
            checked = 4
            dateTimeEdit =dateTimeObj.strftime("%Y-%m-%d")
        query = '''SELECT id, title, type, content,date
               FROM forEvent'''
        with closing(conn.cursor()) as c:
            c.execute(query)
            results = c.fetchall() 
            if len(results) != 0:
                try:
                    for row in results:
                        fordate = row["date"]
                        if checked == 2:
                            fordate = 4
                            self.filterOutput(dateTimeEdit,fordate)
                            break
                        elif checked == 3:
                            fordate = 7
                            self.filterOutput(dateTimeEdit,fordate)
                            break                   
                        elif checked == 4:
                            fordate = 10
                            self.filterOutput(dateTimeEdit,fordate)
                            break              
                        elif checked == 1:
                            self.get_items()
                            break  
                except Exception as e:
                    print(type(e), e)
                    # exit the system when exception is raised
            else:
                return ["0"]
            
    def sendMail(self):
        query = '''select * from forEvent order by id desc limit 1'''
        with closing(conn.cursor()) as c:
            c.execute(query, ())
            row = c.fetchone()
            forDate = row['date']
            cust = forDate[0:16]
            print(cust," cust")
            forMail = row['mail']
            forTitle = row["title"]
            forContent = row["content"]
            send_time = datetime.strptime(cust,"%Y-%m-%d %I:%M")
            now = datetime.now()
            timePart1 = forDate[0:9]
            timePart2 = forDate[11:16]          
            time.sleep(send_time.timestamp() -  time.time())
            self.sendingInfo(forMail, timePart1,timePart2,forTitle, forContent)

            
    def sendingInfo(self, forMail, timePart1,timePart2,forTitle, forContent):
        linkPart= "https://marsme.000webhostapp.com/?name="
        forName = str(timePart1)+"+"+str(timePart2)+"+"+str(forTitle)+"+"+str(forContent)
        linkPart =linkPart+forName
        print(linkPart)
        f = open("myfile.txt","w")
        f.write(linkPart)
        f.close()
        email = 'marsek201522@gmail.com'
        password = 'Mysoul5813'
        send_to_email = forMail
        subject = 'Уведомление о событии'
        message = "Уведомление о предстоящем событии!  Время:"+str(timePart1)+str(timePart2)+" Тема:  "+str(forTitle)+"  Описание:  "+str(forContent)
        file_location = os.path.abspath("myfile.txt")
        os.path.abspath("myfile.txt")
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject
 
        msg.attach(MIMEText(message, 'plain'))
# Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
 
            
            
            
            
        
         

            
        
        
            
        
        

            
             
        

