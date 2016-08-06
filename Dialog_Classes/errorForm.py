# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import errordesign


# Clase de la ventana de error
class ErrorForm(QtGui.QMainWindow, errordesign.Ui_ErrorDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Conecta el botón de ok para cerrar la ventana
        self.pushOk.clicked.connect(self.close)
