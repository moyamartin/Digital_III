#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    -- Company: ADNerd SRL
#    -- Engineers: Moya, Martín; Santos, Lucio; Soria, Leandro
#    --
#    -- Create Date:    10:46:25 03/28/2016
#    -- Project Name: ADNerd - Plot
#    -- Target Devices: OSX, Windows, Linux (Unix based Systems)
#    -- Tool versions: Python 2.7, Qt 3.6.1
#    --
#    -- Dependencies: PyQt4, PySerial, Pyqtgraph
#    --
#    -- Revision: 1.00
#    -- Additional Comments: For further information contact moyamartin1@gmail.com

from PyQt4 import QtGui
from Dialog_Classes import mainForm
import sys


def main():
    app = QtGui.QApplication(sys.argv)  # Una nueva instancia de la aplicación
    form = mainForm.MainForm()  # Seteamos la forma para que sea la aplicación que diseñamos
    form.show()  # Muestra la forma
    app.exec_()  # Ejecuta la aplicación


if __name__ == '__main__':
    main()
