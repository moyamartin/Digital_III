# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(470, 301)
        AboutDialog.setMinimumSize(QtCore.QSize(470, 301))
        AboutDialog.setMaximumSize(QtCore.QSize(470, 301))
        self.layoutWidget = QtGui.QWidget(AboutDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 446, 281))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 50))
        self.label_3.setMaximumSize(QtCore.QSize(120, 50))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Assets/FCEIA_logo.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(190, 20))
        self.label.setMaximumSize(QtCore.QSize(190, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_4.setMaximumSize(QtCore.QSize(60, 60))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("Assets/LOGO_UNR.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(444, 187))
        self.label_2.setMaximumSize(QtCore.QSize(444, 187))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Acerca de", None))
        self.label.setText(_translate("AboutDialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">ADNerd SRL - Plot</span></p></body></html>", None))
        self.label_2.setText(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Este software fue desarrollado para la materia Digital III de la carrera de Ingeniería Electrónica por los estudiantes:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Moya, Martín    Legajo: M - 6132/8</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Santos, Lucio    Legajo: S - 4966/2</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Soria, Leandro    Legajo: S - 4971/9</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">El mismo consiste en comunicarse a un termociclador de ADN implementando el protocolo RS2332, a su vez, lee los datos del dispositivos actuando como un adquisidor de datos</p></body></html>", None))

