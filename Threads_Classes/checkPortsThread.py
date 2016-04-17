# -*- coding: utf-8 -*-


from PyQt4.QtCore import QThread, SIGNAL
import serial
import sys
import glob


class CheckPortsThread(QThread):

    non_stop = True

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    # search_ports() Se encarga de detectar que puertos están disponibles (Abiertos en este caso)
    # se modularizó para diferentes OS (OSX, Windows, Linux)
    @staticmethod
    def search_ports():

        # Si la plataforma es de windows ("win") toma los puertos de COMi para i entre 1 y 256
        if sys.platform.startswith("win"):
            ports = ['COM%s' % (i + 1) for i in range(256)]

        # Si es de linux o cygwin, lee /dev/tty[A-Z][a-z]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # Esto excluye la actual terminal /dev/tty
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:

            # En caso de que la plataforma no esté soportada, tira error por la línea de comandos
            raise EnvironmentError('Unsupported platform')

        # Loop que abre los puertos series en la lista que devuelve el flujo de control anterior
        # En caso de abrirlos exitosamente los guarda en el arreglo result[]
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def set_stop(self):
        self.non_stop = False



    # Esta es la lógica de thread
    def run(self):
        self.non_stop = True

        # La idea es que se corra constantemente y nunca se termine automáticamente el proceso
        # Por eso se puso en un thread para no tildar la aplicación
        while self.non_stop:
            if self.non_stop:
                puertos = self.search_ports()

                # Si no hay puertos disponibles devuelve "No hay dispositivos conectados"
                if not puertos:
                    puerto = 'No hay dispositivos conectados'
                    self.emit(SIGNAL('update_ports(PyQt_PyObject)'), puerto)

                # Caso opuesto: devuelve la lista de los puertos disponibles
                else:
                    self.emit(SIGNAL('update_ports(PyQt_PyObject)'), puertos)
