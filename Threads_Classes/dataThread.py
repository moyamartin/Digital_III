# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time
import serial


class DataThread(QThread):
    data = []
    serial_port = serial.Serial()
    start_time = 0
    actual_time = 0
    non_stop = True

    def __init__(self, serial_port):
        QThread.__init__(self)
        self.serial_port = serial_port

    def __del__(self):
        self.wait()

    def set_serial_port(self, serial_p):
        self.serial_port = serial_p

    def set_timer(self):
        self.start_time = 0
        self.actual_time = 0

    def flush(self):
        del self.data[:]

    def set_stop(self):
        self.non_stop = False

    # Override de la funcion run
    def run(self):
        self.start_time = time.time()
        self.non_stop = True
        while self.non_stop:
            if self.non_stop:
                try:
                    self.data.append(int(self.serial_port.readline()))
                    if self.actual_time == 0:
                        self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.data, self.actual_time)
                        self.actual_time = time.time() - self.start_time
                    else:
                        self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.data, self.actual_time)
                        self.actual_time = time.time() - self.start_time
                except(OSError, serial.SerialException):
                    pass
            else:
                self.serial_port.close()
