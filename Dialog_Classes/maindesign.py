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
        MainWindow.resize(740, 463)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(67, 17))
        self.label.setMaximumSize(QtCore.QSize(67, 17))
        self.label.setSizeIncrement(QtCore.QSize(67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboPorts = QtGui.QComboBox(self.centralwidget)
        self.comboPorts.setMinimumSize(QtCore.QSize(250, 25))
        self.comboPorts.setMaximumSize(QtCore.QSize(250, 25))
        self.comboPorts.setObjectName(_fromUtf8("comboPorts"))
        self.comboPorts.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboPorts)
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
        self.horizontalLayout_2.addWidget(self.pushConectar)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 23))
        self.label_3.setSizeIncrement(QtCore.QSize(60, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.checkBox_datos = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_datos.setEnabled(False)
        self.checkBox_datos.setMinimumSize(QtCore.QSize(50, 23))
        self.checkBox_datos.setMaximumSize(QtCore.QSize(50, 23))
        self.checkBox_datos.setObjectName(_fromUtf8("checkBox_datos"))
        self.horizontalLayout.addWidget(self.checkBox_datos)
        self.checkBox_error = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_error.setEnabled(False)
        self.checkBox_error.setMinimumSize(QtCore.QSize(50, 23))
        self.checkBox_error.setMaximumSize(QtCore.QSize(50, 23))
        self.checkBox_error.setObjectName(_fromUtf8("checkBox_error"))
        self.horizontalLayout.addWidget(self.checkBox_error)
        self.checkBox_pid = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_pid.setEnabled(False)
        self.checkBox_pid.setMinimumSize(QtCore.QSize(70, 23))
        self.checkBox_pid.setMaximumSize(QtCore.QSize(70, 23))
        self.checkBox_pid.setObjectName(_fromUtf8("checkBox_pid"))
        self.horizontalLayout.addWidget(self.checkBox_pid)
        self.checkBox_patron = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_patron.setEnabled(False)
        self.checkBox_patron.setMinimumSize(QtCore.QSize(120, 23))
        self.checkBox_patron.setMaximumSize(QtCore.QSize(120, 23))
        self.checkBox_patron.setObjectName(_fromUtf8("checkBox_patron"))
        self.horizontalLayout.addWidget(self.checkBox_patron)
        spacerItem1 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plot_1 = PlotWidget(self.centralwidget)
        self.plot_1.setMinimumSize(QtCore.QSize(720, 360))
        self.plot_1.setObjectName(_fromUtf8("plot_1"))
        self.verticalLayout.addWidget(self.plot_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menuBar)
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
        self.menuAyuda.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ADN - Plot", None))
        self.label.setText(_translate("MainWindow", "Puerto:", None))
        self.comboPorts.setItemText(0, _translate("MainWindow", "No hay dispositivos conectados", None))
        self.pushConectar.setText(_translate("MainWindow", "Conectar", None))
        self.label_3.setText(_translate("MainWindow", "Mostrar:", None))
        self.checkBox_datos.setText(_translate("MainWindow", "Datos", None))
        self.checkBox_error.setText(_translate("MainWindow", "Error", None))
        self.checkBox_pid.setText(_translate("MainWindow", "Señal PID", None))
        self.checkBox_patron.setText(_translate("MainWindow", "Temperatura Patrón", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
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
