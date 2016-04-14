# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time
import serial


class DataThread(QThread):
    data = []
    serialPort = None
    start_time = 0

    def __init__(self, serialPort):
        QThread.__init__(self)
        self.serialPort = serialPort

    def __del__(self):
        self.wait()

    def setSerialPort(self, serial):
        self.serialPort = serial

    # Override de la funcion terminate
    def terminate(self):
        del self.data[:]

    # Override de la funcion run
    def run(self):
        start_time = time.time()
        while True:
            try:
                self.data.append(long(self.serialPort.readline()))
                self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.data, time.time() - start_time)
            except(OSError, serial.SerialException):
                pass
