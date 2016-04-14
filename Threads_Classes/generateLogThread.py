# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time


# Generates data file after connection or if the internal buffer is big enough
class GenerateLogThread(QThread):
    actualTime = None
    f = None
    data = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def setData(self, data):
        self.data = data

    def run(self):
        self.actualTime = time.strftime("%dd-%mm-%yyyy-%hh-%mm-%ss")
        f = open('dataplot - ' + self.actualTime, w)
        f.write(str(self.data))
        f.close()
