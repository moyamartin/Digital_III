# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(614, 416)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_subreddits = QtGui.QLabel(self.centralwidget)
        self.label_subreddits.setObjectName(_fromUtf8("label_subreddits"))
        self.horizontalLayout_2.addWidget(self.label_subreddits)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_submissions = QtGui.QLabel(self.centralwidget)
        self.label_submissions.setObjectName(_fromUtf8("label_submissions"))
        self.verticalLayout.addWidget(self.label_submissions)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget.raise_()
        self.progressBar.raise_()
        self.lineEdit.raise_()
        self.label_subreddits.raise_()
        self.label_submissions.raise_()
        self.btnStop.raise_()
        self.btnStart.raise_()
        self.btnStop.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_subreddits.setText(_translate("MainWindow", "Subreddits:", None))
        self.lineEdit.setText(_translate("MainWindow", "python, programming, linux, etc (comma separated)", None))
        self.label_submissions.setText(_translate("MainWindow", "Submissions:", None))
        self.btnStart.setText(_translate("MainWindow", "Start", None))
        self.btnStop.setText(_translate("MainWindow", "Pick a folder", None))

