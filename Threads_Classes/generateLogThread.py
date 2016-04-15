# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time


# Generates data file after connection or if the internal buffer is big enough
class GenerateLogThread(QThread):
    actualTime = None
    f = None
    data_y = None
    data_x = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def set_data(self, datay, datax):
        self.data_y = datay
        self.data_x = datax

    def run(self):
        self.actualTime = time.strftime("%d-%m-%y-%H-%M-%S")
        f = open('dataplot - ' + self.actualTime, 'w')
        f.write(str(self.data_y) + '\n' + str(self.data_x))
        f.close()
