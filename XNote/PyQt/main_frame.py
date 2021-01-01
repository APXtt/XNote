import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
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
folder_location = 'C:\\Users\\gbytt\\Dropbox\\[A] 공유폴더\\[E] VScode\\PyQt\\'
logo_img = folder_location + 'logo.png'
exit_img = folder_location + 'exit.png'
##



class Note(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry() #창의 위치와 크기정보 가져옴
        cp = QDesktopWidget().availableGeometry().center() #화면의 가운데 찾음
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle('Note')
        self.setWindowIcon(QIcon(logo_img))
        self.statusBar().showMessage('Hello world!', 1500) #초는 밀리초로 1500=1.5초
        # self.setGeometry(300, 300, 500, 400) #크기랑 위치 지정
        self.resize(800, 650)

        exitAction = QAction(QIcon(exit_img), '&Exit', self) #&는 단축키를 사용할 수 있게 해줌 [alt]+~
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Note')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #MAC운영체제 호환을 위한 것
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.center()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Note()
    sys.exit(app.exec_())