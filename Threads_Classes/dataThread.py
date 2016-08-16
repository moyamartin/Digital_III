# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import serial


class DataThread(QThread):
    temp = []
    pid = []
    ref = []
    error = []
    tiempo = []
    tiempo_t = []
    tiempo_pid = []
    tiempo_error = []
    tiempo_ref = []

    serial_port = serial.Serial()

    start_time = 0
    actual_time = 0
    actual_time_e = 0
    actual_time_pid = 0
    actual_time_ref = 0

    non_stop = True

    aux_1 = []
    aux_2 = []

    aux_temp = []
    aux_error = []
    aux_ref = []
    aux_pid = []

    flag_temp = False
    flag_error = False
    flag_ref = False
    flag_pid = False
    flag_ready = False
    flag_updating = False

    temp_h = 0
    temp_l = 0
    i = 0
    aux_cadena = []

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
        self.actual_time_e = 0
        self.actual_time_pid = 0
        self.actual_time_ref = 0

    def flush(self):
        del self.temp[:]
        del self.tiempo[:]
        del self.pid[:]
        del self.ref[:]
        del self.error[:]
        del self.tiempo_t[:]
        del self.tiempo_pid[:]
        del self.tiempo_error[:]
        del self.tiempo_ref[:]

    def set_stop(self):
        self.non_stop = False

    # Override de la funcion run
    def run(self):
        self.non_stop = True
        while self.non_stop:
            if self.non_stop:
                try:
                    self.aux = self.serial_port.read()
                    if self.flag_temp or self.flag_pid or self.flag_ref or self.flag_error:
                        self.aux_cadena.append(self.aux)
                        self.i += 1
                        if self.i == 2:
                            self.i = 0

                            try:
                                if self.flag_temp:
                                    self.flag_temp = False
                                    self.temp.append(float(self.to_integer(self.aux_cadena)) / 20.000)
                                    self.tiempo_t.append(self.actual_time)
                                    self.actual_time += 0.01

                                elif self.flag_pid:
                                    self.flag_pid = False
                                    self.pid.append(float(self.to_integer(self.aux_cadena)) / 20.000)
                                    self.tiempo_pid.append(self.actual_time_pid)
                                    self.actual_time_pid += 0.01

                                elif self.flag_error:
                                    self.flag_error = False
                                    self.error.append(float(self.to_integer(self.aux_cadena)) / 20.000)
                                    self.tiempo_error.append(self.actual_time_e)
                                    self.actual_time_e += 0.01

                                else:
                                    self.flag_ref = False
                                    self.ref.append(float(self.to_integer(self.aux_cadena)) / 20.000)
                                    self.tiempo_ref.append(self.actual_time_ref)
                                    self.actual_time_ref += 0.01
                                    self.flag_ready = True

                                del self.aux_cadena[:]
                                if self.flag_ready:

                                    self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject,'
                                                     ' PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject,'
                                                     ' PyQt_PyObject)'), self.temp, self.error, self.pid, self.ref,
                                              self.tiempo_t, self.tiempo_error, self.tiempo_pid, self.tiempo_ref)
                                    self.msleep(10)
                                    self.flag_ready = False


                                #if len(self.temp) % 300 == 0:
                                #    self.aux_tiempo = self.tiempo
                                #    self.aux_temp = self.temp
                                #    self.aux_error = self.error
                                #    self.aux_pid = self.pid
                                #    self.aux_ref = self.ref

                                #    self.emit(SIGNAL('clear_plot(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject,'
                                #                     ' PyQt_PyObject, PyQt_PyObject)'), self.aux_temp, self.aux_error,
                                #              self.aux_pid, self.aux_ref, self.aux_tiempo)
                            except ValueError:
                                pass
                    elif self.aux is 'T':
                        self.flag_temp = True
                    elif self.aux is 'E':
                        self.flag_error = True
                    elif self.aux is 'R':
                        self.flag_ref = True
                    elif self.aux is 'P':
                        self.flag_pid = True
                except(OSError, serial.SerialException):
                    pass

            else:
                self.serial_port.close()


    def to_integer(self, cadena):
        to_bits = (ord(cadena[0]) << 8) | ord(cadena[1])
        return to_bits
