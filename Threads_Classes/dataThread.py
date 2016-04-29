# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time
import serial
import string


class DataThread(QThread):
    data = []
    signal = []
    patron = []
    time = []
    serial_port = serial.Serial()
    start_time = 0
    actual_time = 0
    non_stop = True
    aux_1 = []
    aux_2 = []
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
        del self.time[:]
        del self.signal[:]
        del self.patron[:]

    def set_stop(self):
        self.non_stop = False

    # Override de la funcion run
    def run(self):
        self.non_stop = True
        while self.non_stop:
            if self.non_stop:
                try:
                    self.aux = self.serial_port.read()
                    try:
                        self.data.append(int(self.aux))
                        self.actual_time += 0.01
                        self.time.append(self.actual_time)
                        self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.data, self.time)
                        if len(self.data) % 300 == 0:
                            self.aux_x = self.time
                            self.aux_y = self.data
                            self.emit(SIGNAL('clear_plot(PyQt_PyObject, PyQt_PyObject)'), self.aux_y, self.aux_x)
                    except ValueError:
                        pass
                except(OSError, serial.SerialException):
                    pass
            else:
                self.serial_port.close()
