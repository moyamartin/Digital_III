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
        MainWindow.resize(734, 459)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(67, 17))
        self.label.setMaximumSize(QtCore.QSize(67, 17))
        self.label.setSizeIncrement(QtCore.QSize(67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.comboPorts = QtGui.QComboBox(self.centralwidget)
        self.comboPorts.setMinimumSize(QtCore.QSize(250, 25))
        self.comboPorts.setMaximumSize(QtCore.QSize(250, 25))
        self.comboPorts.setObjectName(_fromUtf8("comboPorts"))
        self.comboPorts.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboPorts)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(67, 17))
        self.label_2.setMaximumSize(QtCore.QSize(67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboData = QtGui.QComboBox(self.centralwidget)
        self.comboData.setMinimumSize(QtCore.QSize(100, 25))
        self.comboData.setMaximumSize(QtCore.QSize(100, 25))
        self.comboData.setObjectName(_fromUtf8("comboData"))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.comboData.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboData)
        self.pushConectar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushConectar.sizePolicy().hasHeightForWidth())
        self.pushConectar.setSizePolicy(sizePolicy)
        self.pushConectar.setMinimumSize(QtCore.QSize(100, 25))
        self.pushConectar.setMaximumSize(QtCore.QSize(100, 25))
        self.pushConectar.setSizeIncrement(QtCore.QSize(80, 0))
        self.pushConectar.setObjectName(_fromUtf8("pushConectar"))
        self.horizontalLayout_3.addWidget(self.pushConectar)
        self.pushDesconectar = QtGui.QPushButton(self.centralwidget)
        self.pushDesconectar.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushDesconectar.sizePolicy().hasHeightForWidth())
        self.pushDesconectar.setSizePolicy(sizePolicy)
        self.pushDesconectar.setMinimumSize(QtCore.QSize(100, 25))
        self.pushDesconectar.setMaximumSize(QtCore.QSize(100, 25))
        self.pushDesconectar.setFlat(False)
        self.pushDesconectar.setObjectName(_fromUtf8("pushDesconectar"))
        self.horizontalLayout_3.addWidget(self.pushDesconectar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.plot_1 = PlotWidget(self.centralwidget)
        self.plot_1.setObjectName(_fromUtf8("plot_1"))
        self.verticalLayout.addWidget(self.plot_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 734, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuHerramientas = QtGui.QMenu(self.menuBar)
        self.menuHerramientas.setObjectName(_fromUtf8("menuHerramientas"))
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionConfiguraci_n = QtGui.QAction(MainWindow)
        self.actionConfiguraci_n.setObjectName(_fromUtf8("actionConfiguraci_n"))
        self.actionNinguno = QtGui.QAction(MainWindow)
        self.actionNinguno.setCheckable(False)
        self.actionNinguno.setEnabled(True)
        self.actionNinguno.setObjectName(_fromUtf8("actionNinguno"))
        self.actionSearchPorts = QtGui.QAction(MainWindow)
        self.actionSearchPorts.setCheckable(False)
        self.actionSearchPorts.setObjectName(_fromUtf8("actionSearchPorts"))
        self.actionConectar_dispositivo = QtGui.QAction(MainWindow)
        self.actionConectar_dispositivo.setObjectName(_fromUtf8("actionConectar_dispositivo"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionContenido = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Assets/Help_mark_query_question_support-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContenido.setIcon(icon)
        self.actionContenido.setObjectName(_fromUtf8("actionContenido"))
        self.actionSalir = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Assets/cross_close_quit-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionNueva_ventana = QtGui.QAction(MainWindow)
        self.actionNueva_ventana.setObjectName(_fromUtf8("actionNueva_ventana"))
        self.actionAbrir_datos = QtGui.QAction(MainWindow)
        self.actionAbrir_datos.setObjectName(_fromUtf8("actionAbrir_datos"))
        self.menuArchivo.addAction(self.actionAbrir_datos)
        self.menuArchivo.addAction(self.actionNueva_ventana)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionConfiguraci_n)
        self.menuAyuda.addAction(self.actionAbout)
        self.menuAyuda.addAction(self.actionContenido)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuHerramientas.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.comboData.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ADN - Plot", None))
        self.label.setText(_translate("MainWindow", "Puerto:", None))
        self.comboPorts.setItemText(0, _translate("MainWindow", "No hay dispositivos conectados", None))
        self.label_2.setText(_translate("MainWindow", "Baudrate:", None))
        self.comboData.setItemText(0, _translate("MainWindow", "110", None))
        self.comboData.setItemText(1, _translate("MainWindow", "300", None))
        self.comboData.setItemText(2, _translate("MainWindow", "600", None))
        self.comboData.setItemText(3, _translate("MainWindow", "1200", None))
        self.comboData.setItemText(4, _translate("MainWindow", "2400", None))
        self.comboData.setItemText(5, _translate("MainWindow", "4800", None))
        self.comboData.setItemText(6, _translate("MainWindow", "9600", None))
        self.comboData.setItemText(7, _translate("MainWindow", "14400", None))
        self.comboData.setItemText(8, _translate("MainWindow", "19200", None))
        self.comboData.setItemText(9, _translate("MainWindow", "38400", None))
        self.comboData.setItemText(10, _translate("MainWindow", "57600", None))
        self.comboData.setItemText(11, _translate("MainWindow", "115200", None))
        self.comboData.setItemText(12, _translate("MainWindow", "128000", None))
        self.comboData.setItemText(13, _translate("MainWindow", "256000", None))
        self.pushConectar.setText(_translate("MainWindow", "Conectar", None))
        self.pushDesconectar.setText(_translate("MainWindow", "Desconectar", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionConfiguraci_n.setText(_translate("MainWindow", "Configuracion", None))
        self.actionNinguno.setText(_translate("MainWindow", "Ninguno", None))
        self.actionSearchPorts.setText(_translate("MainWindow", "Buscar puertos", None))
        self.actionConectar_dispositivo.setText(_translate("MainWindow", "Conectar dispositivo", None))
        self.actionAbout.setText(_translate("MainWindow", "Acerca de ADN-Plot", None))
        self.actionContenido.setText(_translate("MainWindow", "Contenido", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionNueva_ventana.setText(_translate("MainWindow", "Nueva ventana", None))
        self.actionAbrir_datos.setText(_translate("MainWindow", "Abrir datos", None))

from pyqtgraph import PlotWidget
