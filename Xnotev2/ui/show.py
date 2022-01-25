import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
dir = 'C:\\Users\\HW\\Documents\\git\\XNote\\Xnotev2\\ui\\find_change\\'
form_class = uic.loadUiType(dir + 'first.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()