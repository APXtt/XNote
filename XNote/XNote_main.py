import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from os import environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

###
filepath = 'C:\\Users\\gbytt\\Dropbox\\[A] 공유폴더\\[E] VScode\\XNote\\'
ui_file = uic.loadUiType(filepath + 'XNote_main.ui')[0]
###

def Changename(fn_finename):
    fn_path = fn_finename.translate(str.maketrans('\\', '/'))
    fn = os.path.basename(fn_path)
    return(fn)



class XNote(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.actionOpen.triggered.connect(self.ActionOpen)
        self.actionSave.triggered.connect(self.ActionSave)


    def ActionOpen(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', './')
        
        if filename[0]:
            with open(filename[0], 'r+', encoding='utf-8') as f:
                d = f.read()
                self.textEdit.setText(d)

                fn = Changename(filename[0])
                self.setWindowTitle('XNote - {}'.format(fn))

    #             self.textEdit.textChanged.connect(self.ActionOpen_Save)
    # def ActionOpen_Save(self):
    #     self.windowTitle.
    
    def ActionSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', './')
        
        if filename[0]:
            with open(filename[0], 'w', encoding='utf-8') as f:
                f.write(self.textEdit.toPlainText())

                fn = Changename(filename[0])
                self.setWindowTitle('XNote - {}'.format(fn))
                



        


if __name__ in '__main__':
    app = QApplication(sys.argv)
    w = XNote()
    w.show()
    sys.exit(app.exec_())



print('hello world')