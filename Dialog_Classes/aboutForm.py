# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import aboutdesign


# La clase respectiva a la ventana de autenticación
class AboutForm(QtGui.QMainWindow, aboutdesign.Ui_AboutDialog):

    image_1 = None
    image_2 = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
