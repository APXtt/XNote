import sys
import os
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QIcon, QTextCursor
import winsound


### 기본 지정 변수
ui_file = uic.loadUiType('/'.join(sys.argv[0].split('\\')[:-1])+'/' + 'ui/main.ui')[0]
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

### 효과음
class sound_error(QThread):
    def run(self):
        winsound.PlaySound('/'.join(sys.argv[0].split('\\')[:-1])+'/' + 'sound/lineedit_error.wav', winsound.SND_ASYNC)
class sound_sucess(QThread):
    def run(self):
        winsound.PlaySound('/'.join(sys.argv[0].split('\\')[:-1])+'/' + 'sound/lineedit_sucess.wav', winsound.SND_ASYNC)
### 자동 저장 기능
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
        ### 기본 지정값
        self.setWindowIcon(QIcon('/'.join(sys.argv[0].split('\\')[:-1])+'/' + 'img/icon.png'))
        self.sound_error = sound_error()
        self.sound_sucess = sound_sucess()
        self.auto_save_signal = auto_save_signal()
        self.bCtrl = False # Ctrl이 활성화 되어 있는가 (기본 False)
        self.cursor = self.textEdit.textCursor()

        ### 위젯 스타일 지정
        self.lineEdit.setStyleSheet('border: 0.5px solid rgb(66, 133, 91)')
        self.textEdit.setStyleSheet('border: 0.5px solid rgb(66, 133, 91);'
                                    'selection-background-color: rgb(0, 0, 0);'
                                    'selection-color: rgb(14, 171, 0);')

        ### 위젯 매소드 연결
        self.lineEdit.returnPressed.connect(self.lineEdit_Enter)
        self.textEdit.textChanged.connect(self.textEdit_Change)

    ### 단축키 기능
    def keyPressEvent(self, e):
        self.bCtrl = True
        self.update()

        if e.key() == Qt.Key_S:
            self.savefile()
        elif e.key() == Qt.Key_O:
            self.openfile()
        elif e.key() == Qt.Key_Tab:
            self.lineEdit.setFocus()

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

    ### 명령어 입력창
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
    
    ### 메모장에 변경이 있을 경우
    """
    활성화된 파일이 없을 때 변경이 있을 때 -> 대기
    활성화된 파일이 있을 때 변경이 있을 때 -> 타이틀 이름에 수정됨(*) 표시, 저장이 가능하게 함
    """
    def textEdit_Change(self):
        global file_run
        global auto_save
        global file_run_path
        global auto_save_one_run

        # 수정 시 WindowTitle 변경
        if file_run == True:
            self.setWindowTitle(file_run_path + ' *')
        # 수정 시 auto_save 시작
        if file_run == True and auto_save == 1 and auto_save_one_run == 1:
            self.auto_save_signal.start()
            auto_save_one_run *= -1

    ### 파일 저장
    """
    새로운 저장을 할 경우 -> 새로운 저장 -> QFileDialog 실행하고 저장해야 함
    다른 파일을 열어서 수정했을 경우 -> 다시 저장
    """
    def savefile(self):
        global file_run
        global file_run_path
        text = self.textEdit.toPlainText() # 저장할 text

        def save_f(self):
            with open(file_run_path, 'w', encoding='UTF-8') as f:
                f.write(text)
            self.setWindowTitle(file_run_path)
            self.statusbar.showMessage('Save', 1000)

        # 1) 새로운 저장
        if file_run == False: 
            try:
                file_run_path = QFileDialog.getSaveFileName(self, 'Save File', 'C:\\')[0] # 경로 + 이름
                save_f(self)
                file_run = True
            except:
                pass
        # 2) 다시 저장
        else:
            save_f(self)
    
    ### 파일 열기
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
    
    ### 자동 줄바꿈
    def auto_line(self):
        global auto_line

        auto_line *= -1

        if auto_line == -1:
            self.textEdit.setLineWrapMode(self.textEdit.NoWrap)
            self.statusbar.showMessage('Auto line = False', 1000)
        else:
            self.textEdit.setLineWrapMode(self.textEdit.WidgetWidth)
            self.statusbar.showMessage('Auto line = True', 1000)

    ### 자동 저장
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


    ### 찾기 기능
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



                    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    app.exec_()