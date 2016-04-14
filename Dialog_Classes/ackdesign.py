# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogack.ui'
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

class Ui_AckDialog(object):
    def setupUi(self, AckDialog):
        AckDialog.setObjectName(_fromUtf8("AckDialog"))
        AckDialog.resize(232, 80)
        AckDialog.setMinimumSize(QtCore.QSize(232, 80))
        AckDialog.setMaximumSize(QtCore.QSize(232, 80))
        AckDialog.setSizeIncrement(QtCore.QSize(232, 0))
        self.pushOk = QtGui.QPushButton(AckDialog)
        self.pushOk.setGeometry(QtCore.QRect(70, 40, 89, 25))
        self.pushOk.setObjectName(_fromUtf8("pushOk"))
        self.label_2 = QtGui.QLabel(AckDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(AckDialog)
        QtCore.QMetaObject.connectSlotsByName(AckDialog)

    def retranslateUi(self, AckDialog):
        AckDialog.setWindowTitle(_translate("AckDialog", "Estado de conexión", None))
        self.pushOk.setText(_translate("AckDialog", "Ok", None))
        self.label_2.setText(_translate("AckDialog", "Conectado exitosamente", None))

