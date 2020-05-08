"""
Created on Sat May  2 12:43:52 2020

@author: savoc
"""
import sys  
from PyQt5 import QtWidgets
import forapp
from forapp import Ui_MainWindow

class ExampleApp(QtWidgets.QMainWindow, forapp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

def main():
    Ui_MainWindow.connect()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()   
    window.show()  
    app.exec_()   
    
if __name__ == '__main__':  
    main()  # то запускаем функцию main()
