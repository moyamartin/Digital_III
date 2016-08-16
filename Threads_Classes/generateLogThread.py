# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time


# Generates data file after connection or if the internal buffer is big enough
class GenerateLogThread(QThread):
    actualTime = None
    f = None
    data_temp = None
    data_error = None
    data_pid = None
    data_ref = None
    data_time = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def set_data(self, temp, error, pid, ref, tiempo):
        self.data_temp = temp
        self.data_error = error
        self.data_pid = pid
        self.data_ref = ref
        self.data_time = tiempo

    def run(self):
        self.actualTime = time.strftime("%d-%m-%y-%H-%M-%S")
        f = open('dataplot - ' + self.actualTime + '.data', 'w')

        for i in range(0, len(self.data_time)):
            f.write(str(self.data_time[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_temp)):
            f.write(str(self.data_temp[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_error)):
            f.write(str(self.data_error[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_pid)):
            f.write(str(self.data_pid[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_ref)):
            f.write(str(self.data_ref[i]) + ',')

        f.close()
