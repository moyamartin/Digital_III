#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import os

import design

class App(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        #Super() es usado para referirse a clases padres sin nombrarla explícitamente
        super(self.__class__, self).__init__()
        #Setea el layout y los widgets definidos dentro del ui
        #Está definido automáticamente en design.py
        self.setupUi(self)
        #Esto relaciona el clickeo del botón con una función que definimos más tarde
        #self.btnBrowse.clicked.connect(self.browse_folder)


def main():
    app = QtGui.QApplication(sys.argv)  #Una nueva instancia de la aplicación
    form = App()    #Seteamos la forma para que sea la aplicación que diseñamos
    form.show()     #Muestra la forma
    app.exec_()     #Ejecuta la aplicación

if __name__ == '__main__':
    main()
