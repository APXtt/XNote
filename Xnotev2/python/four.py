import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import threading

dir = 'C:\\Users\\HW\\Documents\\git\\XNote\\Xnotev2\\'

background = QtGui.QImage(dir + 'img\\background.png')
background_pt = QtGui.QPalette()
background_pt.setBrush(10, QtGui.QBrush(background))

main_style = """
background-color : #000;
color : #79F140;
selection-background-color: #79F140; 
selection-color: #000;
border-style : solid;
border-width : 1px;
border-color : #79F140;
"""

### file save/open 관련 variable
file_run = False
file_run2 = False
file_run_name = ''
file_run_name2 = ''
### 입력중... 관련 variable
show_input_message = True


### 찾기 & 바꾸기 창 시작 ###
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(550, 100)
        Form.setMouseTracking(False)
        Form.setTabletTracking(True)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAutoFillBackground(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "찾기"))
        self.pushButton_2.setText(_translate("Form", "바꾸기"))
        self.label.setText(_translate("Form", "찾기"))
        self.label_2.setText(_translate("Form", "바꾸기"))
        self.pushButton_3.setText(_translate("Form", "모두 바꾸기"))
### 찾기 & 바꾸기 창 종료 ###

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("XNote")
        MainWindow.resize(500, 500)
        MainWindow.setWindowIcon(QtGui.QIcon(dir + 'img\\logo3.png'))
        #MainWindow.setPalette(background_pt)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # textEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setStyleSheet(main_style)
        self.textEdit.textChanged.connect(self.textEdit_change)

        # lineEdit
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit.setStyleSheet(main_style)
        self.lineEdit.returnPressed.connect(self.command)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        # 상태바
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet(main_style)

        # 저장
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave.triggered.connect(self.file_save)

        # 열기
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen.triggered.connect(self.file_open)

        # 폰트
        self.actionfont = QtWidgets.QAction(MainWindow)
        self.actionfont.setObjectName("actionfont")
        self.actionfont.triggered.connect(self.font_change)

        # 줄바꿈
        self.actionline = QtWidgets.QAction(MainWindow)
        self.actionline.setObjectName("actionline")
        self.actionline.setCheckable(True)
        self.actionline.triggered.connect(self.auto_line_enter)

        # 찾고 바꾸기
        self.actionfind = QtWidgets.QAction(MainWindow)
        self.actionfind.setObjectName("actionfind")
        self.actionfind.triggered.connect(self.find_change)

        self.menu_F.addAction(self.actionsave)
        self.menu_F.addAction(self.actionopen)
        self.menu_S.addAction(self.actionfont)
        self.menu_S.addAction(self.actionline)
        self.menu.addAction(self.actionfind)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XNote"))
        self.menu_F.setTitle(_translate("MainWindow", "파일(&F)"))
        self.menu_S.setTitle(_translate("MainWindow", "설정(&S)"))
        self.menu.setTitle(_translate("MainWindow", "기능(&Q)"))
        self.actionsave.setText(_translate("MainWindow", "저장(&S)"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionopen.setText(_translate("MainWindow", "열기(&O)"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionfont.setText(_translate("MainWindow", "폰트"))
        self.actionline.setText(_translate("MainWindow", "줄바꿈"))
        self.actionfind.setText(_translate("MainWindow", "찾고 바꾸기(&H)"))
        self.actionfind.setShortcut(_translate("MainWindow", "Ctrl+H"))

    def find_change(self):
        pass

    def font_change(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
            self.lineEdit.setFont(font)
            font.setPointSize(10)
            self.lineEdit.setFont(font)

    def command(self):
        global show_input_message

        input = self.lineEdit.text()
        vi_input = input.split()
        if input == '':
            pass
        elif input == '입력중 끄기':
            show_input_message = False
            self.lineEdit.clear()
            self.statusbar.showMessage('입력중 모드를 끄기로 변경!', 1000)
        elif input == '입력중 켜기':
            show_input_message = True
            self.lineEdit.clear()
            self.statusbar.showMessage('입력중 모드를 켜기로 변경!', 1000)
        elif input == 'python':
            self.statusbar.showMessage('개발중...', 1000)
            self.lineEdit.clear()
        #elif vi_input[0] == 'vi':   
        else:
            try:
                os.popen(input).read()
                self.statusbar.showMessage('명령어를 실행합니다.', 1000)
                self.lineEdit.clear()
            except:
                pass

    def textEdit_change(self):
        global file_run
        global file_run_name
        if show_input_message == True:
            self.statusbar.showMessage('입력중...', 500)

        if file_run == True:
            tmp_title = file_run_name + ' ^^/'
            MainWindow.setWindowTitle(tmp_title)
        elif file_run2 == True:
            tmp_title = file_run_name2 + ' ^^/'
            MainWindow.setWindowTitle(tmp_title)

    def file_save(self):
        global file_run
        global file_run2
        global file_run_name2

        if file_run == True:
            text = self.textEdit.toPlainText()
            with open(file_run_name, 'w', encoding='UTF-8') as f:
                f.write(text)
                MainWindow.setWindowTitle(f.name)
                self.statusbar.showMessage('저장!', 1000)
        elif file_run2 == True:
            text = self.textEdit.toPlainText()
            with open(file_run_name2, 'w', encoding='UTF-8') as f:
                f.write(text)
                MainWindow.setWindowTitle(f.name)
                self.statusbar.showMessage('저장!', 1000)
        else:
            try:
                file_run_name2_tmp = QtWidgets.QFileDialog.getSaveFileName(MainWindow)
                file_run_name2 = list(file_run_name2_tmp)[0].split('/')[-1]
                text = self.textEdit.toPlainText()
                with open(file_run_name2, 'w', encoding='UTF-8') as f:
                    f.write(text)
                    MainWindow.setWindowTitle(f.name)
                    self.statusbar.showMessage('새로운 저장!', 1000)
                    file_run2 = True
            except:
                pass

    def file_open(self):
        global file_run_name
        global file_run

        file_run_name_tmp = QtWidgets.QFileDialog.getOpenFileName(MainWindow)
        file_run_name = list(file_run_name_tmp)[0].split('/')[-1]
        with open(file_run_name, 'r', encoding='UTF-8') as f:
            data = f.read()
            self.textEdit.setText(data)
            MainWindow.setWindowTitle(f.name)
            self.statusbar.showMessage('열기!', 1000)
            file_run = True

    def auto_line_enter(self):
        if self.actionline.isChecked() == True:
                self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
                self.statusbar.showMessage('줄바꿈 모드를 켜기로 변경!', 1000)
        else:
            self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
            self.statusbar.showMessage('줄바꿈 모드를 끄기로 변경!', 1000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())