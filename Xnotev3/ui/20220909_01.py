# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '20220909_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XNote(object):
    def setupUi(self, XNote):
        XNote.setObjectName("XNote")
        XNote.setEnabled(True)
        XNote.resize(500, 600)
        XNote.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(XNote)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        XNote.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(XNote)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        XNote.setStatusBar(self.statusbar)
        self.actionZ = QtWidgets.QAction(XNote)
        self.actionZ.setCheckable(False)
        self.actionZ.setObjectName("actionZ")
        self.actionX = QtWidgets.QAction(XNote)
        self.actionX.setObjectName("actionX")
        self.actionC = QtWidgets.QAction(XNote)
        self.actionC.setObjectName("actionC")
        self.actionZ_2 = QtWidgets.QAction(XNote)
        self.actionZ_2.setObjectName("actionZ_2")
        self.actionX_2 = QtWidgets.QAction(XNote)
        self.actionX_2.setObjectName("actionX_2")
        self.actionC_2 = QtWidgets.QAction(XNote)
        self.actionC_2.setObjectName("actionC_2")
        self.actionZ_3 = QtWidgets.QAction(XNote)
        self.actionZ_3.setObjectName("actionZ_3")
        self.actionX_3 = QtWidgets.QAction(XNote)
        self.actionX_3.setObjectName("actionX_3")
        self.actionC_3 = QtWidgets.QAction(XNote)
        self.actionC_3.setObjectName("actionC_3")

        self.retranslateUi(XNote)
        QtCore.QMetaObject.connectSlotsByName(XNote)
        XNote.setTabOrder(self.textEdit, self.lineEdit)

    def retranslateUi(self, XNote):
        _translate = QtCore.QCoreApplication.translate
        XNote.setWindowTitle(_translate("XNote", "XNote"))
        self.actionZ.setText(_translate("XNote", "Z"))
        self.actionX.setText(_translate("XNote", "X"))
        self.actionC.setText(_translate("XNote", "C"))
        self.actionZ_2.setText(_translate("XNote", "Z"))
        self.actionX_2.setText(_translate("XNote", "X"))
        self.actionC_2.setText(_translate("XNote", "C"))
        self.actionZ_3.setText(_translate("XNote", "Z"))
        self.actionX_3.setText(_translate("XNote", "X"))
        self.actionC_3.setText(_translate("XNote", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    XNote = QtWidgets.QMainWindow()
    ui = Ui_XNote()
    ui.setupUi(XNote)
    XNote.show()
    sys.exit(app.exec_())
