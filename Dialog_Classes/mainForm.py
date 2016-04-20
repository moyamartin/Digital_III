# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from Threads_Classes import checkPortsThread, dataThread, generateLogThread
import time
import maindesign
import errorForm
import ackForm
import aboutForm
import serial


class MainForm(QtGui.QMainWindow, maindesign.Ui_MainWindow):
    serialPort = None
    actionPuertos = []

    dialogErrorForm = None
    dialogAckForm = None
    dialogAbout = None

    readThread = None
    writeFileThread = None

    datos_x = []
    datos_y = []
    start_time = 0

    def __init__(self):
        # Super() es usado para referirse a clases padres sin nombrarla explícitamente
        super(self.__class__, self).__init__()

        # Setea el layout y los widgets definidos dentro del ui
        # Está definido automáticamente en maindesign.py
        self.setupUi(self)

        # Creamos un puerto serie vacío así más tarde en la conexión setea las variables
        # Y podemos pasarlo como parámetro al thread de lectura
        self.serialPort = serial.Serial()

        # Creamos un objeto del hilo de lectura de datos
        self.readThread = dataThread.DataThread(self.serialPort)
        self.connect(self.readThread, SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject)'), self.update_plot)
        self.connect(self.readThread, SIGNAL('finished()'), self.close_port)

        # Instanciamos el objeto de la clase CheckPortsThread()
        # Esta se encarga de detectar los puertos abiertos de los dispositivos conectados por USB
        self.setDevices = checkPortsThread.CheckPortsThread()
        self.connect(self.setDevices, SIGNAL('update_ports(PyQt_PyObject)'), self.update_combo)
        self.connect(self.setDevices, SIGNAL('finished()'), self.conectar_dispositivo)

        # Otorgamos función a los botones conectar y desconectar
        # Su función es bastante intuitiva
        self.pushDesconectar.clicked.connect(self.end_readings)
        self.pushConectar.clicked.connect(self.conectar_dispositivo)

        # Al iniciar la aplicación queremos que comienze a detectar los dispositivos automáticamente
        self.setDevices.start()

        self.writeFileThread = generateLogThread.GenerateLogThread()

        self.plot_1.setLabel('left', 'Temperatura', 'C')

        self.plot_1.setLabel('bottom', 'Tiempo', 'S')

        self.actionAbout.triggered.connect(self.open_about)

    def open_about(self):
        if self.dialogAbout is None:
            self.dialogAbout = aboutForm.AboutForm()
        self.dialogAbout.show()

    def close_port(self):
        self.serialPort.close()

        self.pushConectar.setEnabled(True)
        self.pushDesconectar.setEnabled(False)
        self.setDevices.start()

    def end_readings(self):
        self.writeFileThread.set_data(self.datos_y, self.datos_x)
        self.writeFileThread.start()

        self.readThread.set_stop()
        self.readThread.quit()

    def kill_set_devices(self):
        # Queremos terminar la detección de los dispositivos porque ya se eligió a cual conectarse
        self.setDevices.set_stop()
        self.setDevices.quit()

    # conectar_dispositivo() es llamado al pulsar el botón conectar
    def conectar_dispositivo(self):

        self.readThread.set_timer()

        del self.datos_y[:]
        del self.datos_x[:]

        self.plot_1.clear()

        # PUERTO_DISPOSITIVO contiene el nombre del puerto serie referida al dispositivo
        # Se obtiene a través del comboBox donde se presentan los puertos disponibles
        # Windows: \\PORTX (1 - X - 255)
        # Unix: /tty[A-Z][a-z]
        PUERTO_DISPOSITIVO = str(self.comboPorts.itemText(self.comboPorts.currentIndex()))

        # PUERTO_BAUDRATE contiene el baudrate que seleccionamos dentro del comboBox del baudrate
        PUERTO_BAUDRATE = int(self.comboData.itemText(self.comboData.currentIndex()))

        # Se intenta conectar al dispositivo, como puede llegar a devolver una excepción se procede de la siguiente
        # manera
        # ERROR: presenta una ventana de error (errorForm.ErrorForm()
        # CORRECTO: presenta una ventana de autenticación (ackForm) y ejecuta el thread de lectura (readThread.Start())
        try:
            # Definimos constantes del puerto seria (puerto, baudrate, bytesize, paridad, bits de stop, timeout)
            self.serialPort = serial.Serial(PUERTO_DISPOSITIVO, PUERTO_BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE,
                                            serial.STOPBITS_ONE, 10, 10)
            # Muestra la ventana de autenticación
            if self.dialogAckForm is None:
                self.dialogAckForm = ackForm.AckForm()
            self.dialogAckForm.show()

            # Setea el puerto serie
            self.readThread.set_serial_port(self.serialPort)

            # Inicializa el hilo de lectura
            self.readThread.start()

            self.pushConectar.setEnabled(False)
            self.pushDesconectar.setEnabled(True)
            self.start_time = time.time()
        except (OSError, serial.SerialException):
            if self.dialogErrorForm is None:
                self.dialogErrorForm = errorForm.ErrorForm()

            # Re-inicializa el thread de detección
            # Muestra la ventana de error
            self.dialogErrorForm.show()
            self.setDevices.start()

    # updateCombo(deviceText): actualiza la lista de puertos disponibles
    # recibe como parámetro un String correspondiente a la dirección de los dispositivos
    def update_combo(self, device_text):
        if device_text == 'No hay dispositivos conectados':
            if self.comboPorts.itemText(0) != 'No hay dispositivos conectados':
                self.comboPorts.setItemText(0, device_text)
                self.remove_extra_items()
        else:
            if self.comboPorts.itemText(0) != device_text[0]:
                self.comboPorts.setItemText(0, device_text[0])
            else:
                if len(device_text) > 1:
                    for k in range(1, len(device_text)):
                        if self.comboPorts.findText(device_text[k]) == -1:
                            self.comboPorts.addItem(device_text[k])
                else:
                    self.remove_extra_items()

    # Remueve valores extras del comboPorts
    def remove_extra_items(self):
        if self.comboPorts.count() >= 1:
            for k in range(1, self.comboPorts.count()):
                self.comboPorts.removeItem(k)

    # Actualiza la gráfica
    def update_plot(self, temp, tiempo):
        self.datos_y = temp
        self.datos_x.append(tiempo)
        self.plot_1.plot(self.datos_x, self.datos_y, pen=(255, 0, 0), symbol=None)
