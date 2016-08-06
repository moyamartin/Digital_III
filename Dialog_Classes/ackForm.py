# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ackdesign
from Threads_Classes import dataThread


# La clase respectiva a la ventana de autenticación
class AckForm(QtGui.QMainWindow, ackdesign.Ui_AckDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushOk.clicked.connect(self.close)
