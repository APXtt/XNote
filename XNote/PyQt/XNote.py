import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, qApp, QDesktopWidget
                            , QTextEdit, QFileDialog)
from PyQt5.QtGui import QIcon
from os import environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()



##
XNote_folder_path = 'C:\\Users\\gbytt\\Dropbox\\[A] 공유폴더\\[E] VScode\\PyQt\\'
XNote_logo = XNote_folder_path + 'XNote_logo.png'
XNote_exit = XNote_folder_path + 'exit.png'
##



class XNote(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle('XNote')
        self.setWindowIcon(QIcon(XNote_logo))
        self.statusBar().showMessage('Hi', 1500)
        self.resize(500, 400)

        # filemenu1
        newtab = QAction(QIcon(XNote_exit), 'New Tab (&W)', self)
        newtab.setShortcut('Ctrl+W')
        newtab.setStatusTip('New Tab')
        newtab.triggered.connect(qApp.quit)
        openfile = QAction(QIcon(XNote_exit), 'Open (&O)', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open XNote')
        openfile.triggered.connect(self.openfile)
        savefile = QAction(QIcon(XNote_exit), 'Save (&S)', self)
        savefile.setShortcut('Ctrl+S')
        savefile.setStatusTip('Save XNote')
        savefile.triggered.connect(self.savefile)
        fileexit = QAction(QIcon(XNote_exit), 'Exit (&E)', self)
        fileexit.setShortcut('Ctrl+E')
        fileexit.setStatusTip('Exit XNote')
        fileexit.triggered.connect(qApp.quit)

        # filemenu2
        filecolor = QAction(QIcon(XNote_exit), 'Color', self)
        #filecolor.setShortcut('Ctrl+?')
        filecolor.setStatusTip('Change color')
        filecolor.triggered.connect(qApp.quit)
        textsize = QAction(QIcon(XNote_exit), 'Size', self)
        #textsize.setShortcut('Ctrl+?')
        textsize.setStatusTip('Change size')
        textsize.triggered.connect(qApp.quit)
        textundo = QAction(QIcon(XNote_exit), 'Undo (&Z)', self)
        textundo.setShortcut('Ctrl+Z')
        textundo.setStatusTip('Undo')
        textundo.triggered.connect(qApp.quit)
        textredo = QAction(QIcon(XNote_exit), 'Redo (&A)', self)
        textredo.setShortcut('Ctrl+A')
        textredo.setStatusTip('Redo')
        textredo.triggered.connect(qApp.quit)

        # filemenu3

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu1 = menubar.addMenu('&File')
        filemenu2 = menubar.addMenu('&Edit')
        filemenu3 = menubar.addMenu('&Setting')

        filemenu1.addAction(newtab)
        filemenu1.addAction(openfile)
        filemenu1.addAction(savefile)
        filemenu1.addAction(fileexit)

        filemenu2.addAction(filecolor)
        filemenu2.addAction(textsize)
        filemenu2.addAction(textundo)
        filemenu2.addAction(textredo)
        
        self.center()
        self.show()




    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r+')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def savefile(self):
        fname = QFileDialog.getSaveFileName(self, 'Save File', './' )

        self.textEdit.setText(fname)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = XNote()
    sys.exit(app.exec_())
