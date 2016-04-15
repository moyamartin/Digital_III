# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time
import serial


class DataThread(QThread):
    data = []
    serial_port = None
    start_time = 0

    def __init__(self, serial_port):
        QThread.__init__(self)
        self.serial_port = serial_port

    def __del__(self):
        self.wait()

    def set_serial_port(self, serial_p):
        self.serial_port = serial_p

    def quit(self):
        del self.serial_port

    def flush(self):
        del self.data[:]

    # Override de la funcion run
    def run(self):
        start_time = time.time()
        while True:
            try:
                self.data.append(float(self.serial_port.readline()))
                self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.data, time.time() - start_time)
            except(OSError, serial.SerialException):
                pass
