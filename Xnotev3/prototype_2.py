import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QIcon, QTextCursor
import winsound

### 기본지정 변수들 ###
ui_file = uic.loadUiType("ui/20220812_01.ui")[0]
file_run = False
file_run_path = ''
auto_line = 1 # 1 == auto line True / -1 == auto line False
auto_save = 1 # 1 == auto save True / -1 == auto Save False
auto_save_cycle = 60 # 60s
auto_save_one_run = 1
auto_save_run = False
n = 100 # 기본 textEdit 화면 사이즈 100%
find_count = 0

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class sound_error(QThread):
    def run(self):
        winsound.PlaySound("sound/lineedit_error.wav", winsound.SND_ASYNC)
class sound_sucess(QThread):
    def run(self):
        winsound.PlaySound("sound/lineedit_sucess.wav", winsound.SND_ASYNC)
class auto_save_signal(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        global auto_save_cycle
        global file_run_path

        while self.running:
            if file_run == True:
                text = Window.textEdit.toPlainText()
                with open(file_run_path, 'w', encoding='UTF-8') as f:
                    f.write(text)
                    Window.setWindowTitle(file_run_path)
                self.sleep(auto_save_cycle)
    def resume(self): # 재가동
        self.running = True
    def pause(self): # 멈춤
        self.running = False

class Window(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ### A ###
        self.setWindowIcon(QIcon('img/XNotev3 icon.png'))
        self.sound_error = sound_error()
        self.sound_sucess = sound_sucess()
        self.auto_save_signal = auto_save_signal()

        # styleSheet Start #
        self.lineEdit.setStyleSheet('border: 0.5px solid rgb(66, 133, 91)')
        self.textEdit.setStyleSheet('border: 0.5px solid rgb(66, 133, 91)')
        # styleSheet End #

        self.bCtrl = False # Ctrl이 활성화 되어 있는가 (기본 False)

        self.cursor = self.textEdit.textCursor() 

        ### B ###
        self.lineEdit.returnPressed.connect(self.lineEdit_Enter)
        self.textEdit.textChanged.connect(self.textEdit_Change)

    ### C ###

    # [Ctrl]+[Mouse wheel up/down], [Ctrl]+[s, o] Start #
    def keyPressEvent(self, e):
        self.bCtrl = True
        self.update()

        if e.key() == Qt.Key_S:
            self.savefile()
        elif e.key() == Qt.Key_O:
            self.openfile()

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Control:
            self.bCtrl = False
        self.update()

    def wheelEvent(self, e):
        global n

        if self.bCtrl:
            if e.angleDelta().y() > 0 and n < 300:
                self.textEdit.zoomIn(2)
                n += 10
                self.statusBar().showMessage('{0}%'.format(n), 400)
            elif e.angleDelta().y() < 0 and n > 70:
                self.textEdit.zoomIn(-2)
                n -= 10
                self.statusBar().showMessage('{0}%'.format(n), 400)
        self.update()
    # [Ctrl]+[Mouse wheel up/down], [Ctrl]+[s, o] End #


    def lineEdit_Enter(self):
        if self.lineEdit.text() == 'cmd':
            self.sound_sucess.start()
            self.lineEdit.clear()
            self.statusBar().showMessage('Run cmd', 500)
            os.system('start')
        elif self.lineEdit.text() == 'save':
            self.sound_sucess.start()
            self.lineEdit.clear()
            self.savefile()
        elif self.lineEdit.text() == 'open':
            self.sound_sucess.start()
            self.lineEdit.clear()
            self.openfile()
        elif self.lineEdit.text() == 'auto line':
            self.sound_sucess.start()
            self.lineEdit.clear()
            self.auto_line()
        elif self.lineEdit.text() == 'auto save':
            self.sound_sucess.start()
            self.lineEdit.clear()
            self.auto_save()
        elif ' '.join(self.lineEdit.text().split(' ')[:-1]) == 'auto save cycle':
            global auto_save_cycle
            cycle_value = self.lineEdit.text().split(' ')[-1]
            self.sound_sucess.start()
            self.lineEdit.clear()
            auto_save_cycle = int(cycle_value)
        elif self.lineEdit.text() == 'clear':
            self.textEdit.clear()
            self.sound_sucess.start()
            self.lineEdit.clear()
        elif self.lineEdit.text()[:4] == 'find':
            find_value = self.lineEdit.text()[5:]
            if find_value != '' and len(find_value) != 1:
                find_list = self.find(find_value)
                if find_list != []:
                    self.sound_sucess.start()
                    self.find_textEdit_change(find_list)
        else:
            self.sound_error.start()
            self.lineEdit.clear()
            self.statusBar().showMessage('Unknown command', 500)
    
    def textEdit_Change(self):
        global file_run
        global auto_save
        global file_run_path
        global auto_save_one_run

        # 수정 시 WindowTitle 변경
        if file_run == True:
            f = file_run_path + ' *'
            self.setWindowTitle(f)
        # 수정 시 auto_save 시작
        if file_run == True and auto_save == 1 and auto_save_one_run == 1:
            self.auto_save_signal.start()
            auto_save_one_run *= -1

    def savefile(self):
        global file_run
        global file_run_path

        text = self.textEdit.toPlainText() # 저장할 text

        # 1) 새로운 저장
        if file_run == False: 
            try:
                file_run_path = QFileDialog.getSaveFileName(self, 'Save File', 'C:\\')[0] # 경로 + 이름
                # file_run_name = list(file_run_path).split('/')[-1] # 이름
                with open(file_run_path, 'w', encoding='UTF-8') as f:
                    f.write(text)
                self.setWindowTitle(file_run_path)
                self.statusbar.showMessage('New Save', 1000)
                file_run = True
            except:
                pass
        # 2) 다시 저장
        else:
            with open(file_run_path, 'w', encoding='UTF-8') as f:
                f.write(text)
                self.setWindowTitle(file_run_path)
                self.statusbar.showMessage('Save', 1000)
        
    def openfile(self):
        global file_run
        global file_run_path

        try:
            file_run_path = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\')[0]
            with open(file_run_path, 'r', encoding='UTF-8') as f:
                data = f.read()
                self.textEdit.setText(data)
            self.setWindowTitle(file_run_path)
            self.statusbar.showMessage('Open', 1000)
            file_run = True
        except:
            pass
    
    def auto_line(self):
        global auto_line

        auto_line *= -1

        if auto_line == -1:
            self.textEdit.setLineWrapMode(self.textEdit.NoWrap)
            self.statusbar.showMessage('Auto line = False', 1000)
        else:
            self.textEdit.setLineWrapMode(self.textEdit.WidgetWidth)
            self.statusbar.showMessage('Auto line = True', 1000)

    def auto_save(self):
        global auto_save
        global auto_save_cycle

        auto_save *= -1

        if auto_save == -1:
            self.auto_save_signal.pause()
            self.statusbar.showMessage('Auto save = False', 1000)
        else:
            self.auto_save_signal.start()
            self.auto_save_signal.resume()
            self.statusbar.showMessage('Auto save = True', 1000)


### Find Start ###
    def find(self, find_value):
        find_target = self.textEdit.toPlainText()
        find_end = 0
        find_count = 0
        find_return = []

        while True:
            try:
                find_st = find_target.index(find_value, find_end)
                find_end = find_st+(len(find_value)-1)
                find_count += 1
                find_return.append([find_count, find_st, find_end])
            except:
                break

        return find_return

    def find_textEdit_change(self, find_list):
        global find_count

        if find_list != []:
            if find_count < len(find_list):
                self.setCursor(find_list[find_count][1], find_list[find_count][2]+1)
                find_count += 1
            elif find_count == len(find_list):
                find_count = 0
                self.setCursor(find_list[find_count][1], find_list[find_count][2]+1)
                find_count = 1
            elif find_count > len(find_list):
                find_count = 0
                self.setCursor(find_list[find_count][1], find_list[find_count][2]+1)
                find_count = 1 
    
    def setCursor(self, start, end):
        self.cursor.setPosition(start)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start)
        self.textEdit.setTextCursor(self.cursor)
### Find End ###



        
        









        



            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    app.exec_()