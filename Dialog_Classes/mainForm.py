# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from Threads_Classes import checkPortsThread, dataThread, generateLogThread
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

    # Datos a plotear
    datos_tiempo = []
    datos_temp = []
    datos_error = []
    datos_ref = []
    datos_pid = []

    # Buffer interno de 300 valores
    buffer_tiempo = []
    buffer_temp = []
    buffer_ref = []
    buffer_error = []
    buffer_pid = []

    # Colores de las señales
    color_temp = (255, 0, 0)
    color_error = (0, 255, 0)
    color_ref = (0, 0, 255)
    color_pid = (255, 255, 0)

    curve_temp = None
    curve_error = None
    curve_ref = None
    curve_pid = None

    brush_temp = None
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
        self.connect(self.readThread, SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject,'
                                             ' PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'),
                     self.update_plot)
        self.connect(self.readThread, SIGNAL('finished()'), self.close_port)

        # Instanciamos el objeto de la clase CheckPortsThread()
        # Esta se encarga de detectar los puertos abiertos de los dispositivos conectados por USB
        self.setDevices = checkPortsThread.CheckPortsThread()
        self.connect(self.setDevices, SIGNAL('update_ports(PyQt_PyObject)'), self.update_combo)
        self.connect(self.setDevices, SIGNAL('finished()'), self.conectar_dispositivo)

        # Otorgamos función a los botones conectar y desconectar
        # Su función es bastante intuitiva
        self.pushConectar.clicked.connect(self.conectar_dispositivo)

        # Al iniciar la aplicación queremos que comienze a detectar los dispositivos automáticamente
        self.setDevices.start()

        self.writeFileThread = generateLogThread.GenerateLogThread()

        self.plot_1.setLabel('left', 'Temperatura', 'C')
        self.plot_1.setLabel('bottom', 'Tiempo', 'S')
        self.plot_1.setXRange(0, 3, 0.05)
        self.plot_1.setYRange(0, 100, 0.05)
        self.plot_1.addLegend()
        self.curve_temp = self.plot_1.plot(pen=(self.color_temp[0], self.color_temp[1], self.color_temp[2]),
                                           name="Temperatura")
        self.curve_error = self.plot_1.plot(pen=(self.color_error[0], self.color_error[1], self.color_error[2]),
                                            name="Error")
        self.curve_ref = self.plot_1.plot(pen=(self.color_ref[0], self.color_ref[1], self.color_ref[2]),
                                          name="Referencia")
        self.curve_pid = self.plot_1.plot(pen=(self.color_pid[0], self.color_pid[1], self.color_pid[2]),
                                          name="PID")




        self.actionAbout.triggered.connect(self.open_about)
        self.actionAbrir_datos.triggered.connect(self.open_plot)

        self.checkBox_datos.setChecked(True)
        self.checkBox_error.setChecked(True)
        self.checkBox_patron.setChecked(True)
        self.checkBox_pid.setChecked(True)

        self.checkBox_datos.clicked.connect(self.modify_plot)
        self.checkBox_error.clicked.connect(self.modify_plot)
        self.checkBox_pid.clicked.connect(self.modify_plot)
        self.checkBox_patron.clicked.connect(self.modify_plot)

        

    def modify_plot(self):
        aux_datos = self.datos_temp
        aux_error = self.datos_error
        aux_pid = self.datos_pid
        aux_patron = self.datos_ref
        if self.checkBox_datos.isChecked() is False:
            aux_datos = []
        if self.checkBox_error.isChecked() is False:
            aux_error = []
        if self.checkBox_patron.isChecked() is False:
            aux_patron = []
        if self.checkBox_pid.isChecked() is False:
            aux_pid = []

        self.curve_ref.setData([], [])
        self.curve_error.setData([], [])
        self.curve_pid.setData([], [])
        self.curve_temp.setData([], [])
        self.update_plot(aux_datos, aux_error, aux_pid, aux_patron, self.datos_tiempo, self.datos_tiempo,
                         self.datos_tiempo, self.datos_tiempo)

        del aux_datos
        del aux_error
        del aux_pid
        del aux_patron

    def open_plot(self):

        del self.datos_tiempo[:]
        del self.datos_temp[:]
        del self.datos_error[:]
        del self.datos_pid[:]
        del self.datos_ref[:]

        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo de datos', '/home')
        try:
            f = open(file_name, 'r')

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_tiempo.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_temp.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_error.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_pid.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_ref.append(float(aux[i]))

            f.close()

            self.curve_ref.setData([], [])
            self.curve_error.setData([], [])
            self.curve_pid.setData([], [])
            self.curve_temp.setData([], [])
            self.update_plot(self.datos_temp, self.datos_error, self.datos_pid, self.datos_ref, self.datos_tiempo,
                             self.datos_tiempo, self.datos_tiempo, self.datos_tiempo)
            self.plot_1.setXRange(0, self.datos_tiempo[len(self.datos_tiempo) - 1])

            self.checkBox_datos.setEnabled(True)
            self.checkBox_datos.setChecked(True)
            self.checkBox_error.setEnabled(True)
            self.checkBox_error.setChecked(True)
            self.checkBox_patron.setEnabled(True)
            self.checkBox_patron.setChecked(True)
            self.checkBox_pid.setEnabled(True)
            self.checkBox_pid.setChecked(True)

        except IOError:
            pass

    def open_about(self):
        if self.dialogAbout is None:
            self.dialogAbout = aboutForm.AboutForm()
        self.dialogAbout.show()

    def close_port(self):
        self.datos_tiempo.extend(self.buffer_tiempo)
        self.datos_temp.extend(self.buffer_temp)
        self.datos_pid.extend(self.buffer_pid)
        self.datos_error.extend(self.buffer_error)
        self.datos_ref.extend(self.buffer_ref)

        self.writeFileThread.set_data(self.datos_temp, self.datos_error, self.datos_pid, self.datos_ref,
                                      self.datos_tiempo)
        self.writeFileThread.start()

        self.readThread.flush()
        self.serialPort.close()

        if len(self.datos_temp) > 0:
            self.update_plot(self.datos_temp, self.datos_error, self.datos_pid, self.datos_ref, self.datos_tiempo,
                             self.datos_tiempo, self.datos_tiempo, self.datos_tiempo)
            self.plot_1.setXRange(0, self.datos_tiempo[len(self.datos_tiempo) - 1])
        else:
            self.curve_ref.setData([], [])
            self.curve_error.setData([], [])
            self.curve_pid.setData([], [])
            self.curve_temp.setData([], [])

        self.plot_1.setMouseEnabled(True, True)

        self.comboPorts.setEnabled(True)
        self.pushConectar.setEnabled(True)
        self.setDevices.start()

    def end_readings(self):
        self.pushConectar.setText("Conectar")
        self.pushConectar.clicked.disconnect()
        self.pushConectar.clicked.connect(self.conectar_dispositivo)

        self.readThread.set_stop()
        self.readThread.quit()

    def kill_set_devices(self):
        # Queremos terminar la detección de los dispositivos porque ya se eligió a cual conectarse
        self.setDevices.set_stop()
        self.setDevices.quit()

    # conectar_dispositivo() es llamado al pulsar el botón conectar
    def conectar_dispositivo(self):

        del self.datos_tiempo[:]
        del self.datos_temp[:]
        del self.datos_error[:]
        del self.datos_pid[:]
        del self.datos_ref[:]

        self.plot_1.setYRange(0, 100, 0.01)
        self.plot_1.setXRange(0, 3, 0.01)

        self.readThread.set_timer()

        self.curve_ref.setData([], [])
        self.curve_error.setData([], [])
        self.curve_pid.setData([], [])
        self.curve_temp.setData([], [])
        self.plot_1.setMouseEnabled(False, False)

        # PUERTO_DISPOSITIVO contiene el nombre del puerto serie referida al dispositivo
        # Se obtiene a través del comboBox donde se presentan los puertos disponibles
        # Windows: \\PORTX (1 - X - 255)
        # Unix: /tty[A-Z][a-z]
        PUERTO_DISPOSITIVO = str(self.comboPorts.itemText(self.comboPorts.currentIndex()))

        # PUERTO_BAUDRATE contiene el baudrate que seleccionamos dentro del comboBox del baudrate
        PUERTO_BAUDRATE = 115200

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

            self.checkBox_datos.setEnabled(False)
            self.checkBox_error.setEnabled(False)
            self.checkBox_pid.setEnabled(False)
            self.checkBox_patron.setEnabled(False)

            self.comboPorts.setEnabled(False)

            self.checkBox_datos.setChecked(True)
            self.checkBox_error.setChecked(True)
            self.checkBox_patron.setChecked(True)
            self.checkBox_pid.setChecked(True)

            self.pushConectar.setText("Desconectar")
            self.pushConectar.clicked.disconnect()
            self.pushConectar.clicked.connect(self.end_readings)
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
    def update_plot(self, temp, error, pid, ref, tiempo_t, tiempo_e, tiempo_p, tiempo_r):  # , patron, signal):
        self.buffer_error = error
        self.buffer_pid = pid
        self.buffer_ref = ref
        self.buffer_tiempo = tiempo_t
        self.buffer_temp = temp

        if len(self.buffer_temp) != 0: #and len(self.buffer_temp) is len(self.buffer_tiempo):
            #self.fix_matrix(self.buffer_temp)
            #self.curve_temp.setData(x=self.buffer_tiempo, y=self.buffer_temp)
            self.curve_temp.setData(x=tiempo_t, y=self.buffer_temp, antialias=True)
        else:
            self.curve_temp.setData([], [])

        if len(self.buffer_error) != 0: #and len(self.buffer_error) is len(self.buffer_tiempo):
            #self.fix_matrix(self.buffer_error)
            #self.curve_error.setData(x=self.buffer_tiempo, y=self.buffer_error)
            self.curve_error.setData(x=tiempo_e, y=self.buffer_error, antialias=True)
        else:
            self.curve_error.setData([], [])

        if len(self.buffer_pid) != 0:
            #and len(self.buffer_pid) is len(self.buffer_tiempo):
            #self.fix_matrix(self.buffer_pid)
            #self.curve_pid.setData(x=self.buffer_tiempo, y=self.buffer_pid)
            self.curve_pid.setData(x=tiempo_p,y=self.buffer_pid, antialias=True)
        else:
            self.curve_pid.setData([], [])

        if len(self.buffer_ref) != 0: #and len(self.buffer_ref) is len(self.buffer_tiempo):
            #self.fix_matrix(self.buffer_ref)
            #self.curve_ref.setData(x=self.buffer_tiempo, y=self.buffer_ref)
            self.curve_ref.setData(x=tiempo_r,y=self.buffer_ref, antialias=True )
        else:
            self.curve_ref.setData([], [])

        if len(self.buffer_tiempo) >= 300:
            self.plot_1.setXRange(self.buffer_tiempo[len(self.buffer_tiempo) - 1] - 3,
                                  self.buffer_tiempo[len(self.buffer_tiempo) - 1], 0.05)
