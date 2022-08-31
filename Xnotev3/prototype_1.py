import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
import winsound
import re

### 기본지정 변수들 ###
ui_file = uic.loadUiType("ui/20220812_01.ui")[0]
file_run = False
file_run_path = ''
auto_line = 1 # 1 == auto line True / -1 == auto line False
auto_save = 1 # 1 == auto save True / -1 == auto Save False
auto_save_cycle = 60 # 60s
auto_save_one_run = 1
auto_save_run = False
main_style = """
border: 1px solid rgb(102, 102, 102);
"""


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
    def resume(self):
        self.running = True
    def pause(self):
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

        self.lineEdit.setStyleSheet(main_style)
        self.textEdit.setStyleSheet(main_style)

        ### B ###
        self.lineEdit.returnPressed.connect(self.lineEdit_Enter)
        self.textEdit.textChanged.connect(self.textEdit_Change)
    ### C ###
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
        # elif self.lineEdit.text()[:4] == 'find':
        #     find_value = self.lineEdit.text()[5:]
        #     self.sound_sucess.start()
        #     self.lineEdit.clear()
        #     self.find(find_value)
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

    # def find(self, v):
    #     v_div = []
    #     for i in range(len(v)):
    #         v_div.append(v[i])
    #     t = self.textEdit.toPlainText()
    #     sucess_count = 1
        
    #     for i in range(len(t)):
    #         if v_div[0] == t[i]:
    #             for ii in range(len(v_div)-1):



    #                 if i == 0:
    #                     i = 1
    #                 if v_div[ii+1] == t[ii+i]:
    #                     sucess_count += 1
    #                 print(i, ii, sucess_count)
        
    #     find_count = sucess_count / len(v_div)
    #     print(sucess_count)
    #     print(find_count)









        



            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    app.exec_()