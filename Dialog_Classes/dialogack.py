# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogerror.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName(_fromUtf8("ErrorDialog"))
        ErrorDialog.resize(293, 95)
        self.label_2 = QtGui.QLabel(ErrorDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 241, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushOk = QtGui.QPushButton(ErrorDialog)
        self.pushOk.setGeometry(QtCore.QRect(100, 50, 89, 25))
        self.pushOk.setObjectName(_fromUtf8("pushOk"))

        self.retranslateUi(ErrorDialog)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Error", None))
        self.label_2.setText(_translate("ErrorDialog", "Error en la conexión, revise el cable ", None))
        self.pushOk.setText(_translate("ErrorDialog", "Ok", None))

