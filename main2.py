from typing import Union
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from Base_Consulta_Registros import *
from crear_base import *
from ui_Interfaz import *
import datetime


class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__ (self, *args):

        QtWidgets.QMainWindow.__init__ (self, *args)
        self.setupUi (self)
        self.tableWidget_Registros_Alumno.setHorizontalHeaderLabels (
            ['ID', 'Nombre', 'Apellido', 'DNI', 'Correo', 'Número Telefónico', 'Fecha Nacimiento', 'Ciudad',
             'Direccion', 'Codigo Postal', 'Ingreso'])
        self.actualizar_Alumno ()
        for i in range (11):
            self.tableWidget_Registros_Alumno.resizeColumnToContents (i)
        self.pushButton_RegistrarAlumno.clicked.connect (self.registro_Alumno)
        self.pushButton_ActualizarAlumno.clicked.connect (self.actualizar_Alumno)
        self.pushButto_BuscarAlumno.clicked.connect (self.buscar_Alumnos)
        self.pushButton_cargarAlumno.clicked.connect (self.buscarModificar_Alumno)
        self.pushButton_modificarAlumno.clicked.connect (self.modificar_Alumno)
        self.pushButton_borrarAlumno.clicked.connect (self.borrar_Alumno)

    #################--Alumno--####################
    def registro_Alumno (self):
        ahora = datetime.date.today ()
        nombreAlumno = self.lineEdit_nombreAlumno.text ()
        apellidoAlumno = self.lineEdit_apellidoAlumno.text ()
        dniAlumno = self.lineEdit_dniAlumno.text ()
        correoAlumno = self.lineEdit_correoAlumno.text ()
        numTelAlumno = self.lineEdit_numTelAlumno.text ()
        fechaNacimientoAlumno = self.dateEdit_nacimientoAlumno.dateTime ().date ().toPyDate ().isoformat ()
        fechaIngresoAlumno = self.dateEdit_ingresoAlumno.dateTime ().date ().toPyDate ().isoformat ()
        ciudadAlumno = self.lineEdit_ciudadAlumno.text ()
        direccionAlumno = self.lineEdit_direccionAlumno.text ()
        codPostalAlumno = self.lineEdit_codigoPostalAlumno.text ()
        estado = 'cursando'
        if nombreAlumno.strip () == '' or apellidoAlumno.strip () == '' or dniAlumno.strip () == '' or ciudadAlumno.strip () == '' or direccionAlumno.strip () == '' or codPostalAlumno.strip () == '':
            pass
        else:
            if correoAlumno == '':
                correoAlumno = "No ingresado"
            if numTelAlumno == '':
                numTelAlumno = "No ingresado"
            dato = [nombreAlumno, apellidoAlumno, dniAlumno, correoAlumno, numTelAlumno, fechaNacimientoAlumno,
                    ciudadAlumno, direccionAlumno, codPostalAlumno, fechaIngresoAlumno, estado]
            conn = conexion ()
            IngresarAlumno (conn, dato)
            conn.close ()
            self.actualizar_Alumno ()
            self.lineEdit_nombreAlumno.setText ('')
            self.lineEdit_apellidoAlumno.setText ('')
            self.lineEdit_dniAlumno.setText ('')
            self.lineEdit_correoAlumno.setText ('')
            self.lineEdit_numTelAlumno.setText ('')
            self.dateEdit_nacimientoAlumno.setDate (ahora)
            self.dateEdit_ingresoAlumno.setDate (ahora)
            self.lineEdit_ciudadAlumno.setText ('')
            self.lineEdit_direccionAlumno.setText ('')
            self.lineEdit_codigoPostalAlumno.setText ('')
            self.actualizar_Alumno ()

    def buscar_Alumnos (self):
        nombreAlumno = self.lineEdit_nombreAlumno.text ().strip ()
        apellidoAlumno = self.lineEdit_apellidoAlumno.text ().strip ()
        dniAlumno = self.lineEdit_dniAlumno.text ().strip ()
        correoAlumno = self.lineEdit_correoAlumno.text ().strip ()
        numTelAlumno = self.lineEdit_numTelAlumno.text ().strip ()
        ciudadAlumno = self.lineEdit_ciudadAlumno.text ().strip ()
        direccionAlumno = self.lineEdit_direccionAlumno.text ().strip ()
        codPostalAlumno = self.lineEdit_codigoPostalAlumno.text ().strip ()
        dato = [nombreAlumno + '%', apellidoAlumno + '%', dniAlumno + '%', correoAlumno + '%', numTelAlumno + '%',
                ciudadAlumno + '%', direccionAlumno + '%', codPostalAlumno + '%']
        if dato != ['%', '%', '%', '%', '%', '%', '%', '%']:
            conn = conexion ()
            info = BuscarAlumno (conn, dato)
            self.tableWidget_Registros_Alumno.setRowCount (0)
            for row_number, row_data in enumerate (info):
                self.tableWidget_Registros_Alumno.insertRow (row_number)
                for column_number, data in enumerate (row_data):
                    self.tableWidget_Registros_Alumno.setItem (row_number, column_number,
                                                               QtWidgets.QTableWidgetItem (str (data)))
            conn.close ()
        else:
            pass

    def buscarModificar_Alumno (self):  # Boton CARGAR
        idBuscarAlumnoModificar = self.lineEdit_idAlumno.text ().strip ()
        if idBuscarAlumnoModificar == '':
            idBuscarAlumnoModificar = '0'
        conn = conexion ()
        try:
            dato = BuscarAlumnoModificar (conn, idBuscarAlumnoModificar)
            conn.close ()
            self.lineEdit_nombreAlumno_2.setText (dato[0][1])
            self.lineEdit_apellidoAlumno_2.setText (dato[0][2])
            self.lineEdit_dniAlumno_2.setText (dato[0][3])
            self.lineEdit_correoAlumno_2.setText (dato[0][4])
            self.lineEdit_numTelAlumno_2.setText (dato[0][5])
            self.label.setText (dato[0][6])
            self.lineEdit_ciudadAlumno_2.setText (dato[0][7])
            self.lineEdit_direccionAlumno_2.setText (dato[0][8])
            self.lineEdit_codigoPostalAlumno_2.setText (dato[0][9])
            self.label_2.setText (dato[0][10])
            if dato == [('', '', '', '', '', '', '', '', '', '', '')]:
                self.lineEdit_idAlumno.setText ('')
        except IndexError:
            print ("fuera de rango")

    def modificar_Alumno (self):
        ahora = QDate.currentDate ()
        nombreAlumno = self.lineEdit_nombreAlumno_2.text ()
        apellidoAlumno = self.lineEdit_apellidoAlumno_2.text ()
        dniAlumno = self.lineEdit_dniAlumno_2.text ()
        correoAlumno = self.lineEdit_correoAlumno_2.text ()  # No esencial
        numTelAlumno = self.lineEdit_numTelAlumno_2.text ()  # No esencial
        ciudadAlumno = self.lineEdit_ciudadAlumno_2.text ()
        direccionAlumno = self.lineEdit_direccionAlumno_2.text ()
        codPostalAlumno = self.lineEdit_codigoPostalAlumno_2.text ()

        #       fechaNacimientoAlumno = self.dateEdit_nacimientoAlumno_2.date ().toPyDate ().strftime ("%d/%m/%y")
        #        fechaIngresoAlumno = self.dateEdit_ingresoAlumno_2.date ().toPyDate ().strftime ("%d/%m/%y")

        fechaNacimientoAlumno = self.dateEdit_nacimientoAlumno_2.dateTime ().date ().toPyDate ().isoformat ()
        fechaIngresoAlumno = self.dateEdit_ingresoAlumno_2.dateTime ().date ().toPyDate ().isoformat ()

        # fechaNacimientoAlumno = self.dateEdit_nacimientoAlumno.dateTime ().date ().toPyDate ().isoformat ()
        # fechaIngresoAlumno = self.dateEdit_ingresoAlumno.dateTime ().date ().toPyDate ().isoformat ()

        idModificar = self.lineEdit_idAlumno.text ().strip ()
        dato = [nombreAlumno, apellidoAlumno, dniAlumno, correoAlumno, numTelAlumno, fechaNacimientoAlumno,
                ciudadAlumno, direccionAlumno, codPostalAlumno, fechaIngresoAlumno]
        conn = conexion ()
        ModificarAlumno (conn, dato, idModificar)
        conn.close ()

        self.actualizar_Alumno ()

        self.lineEdit_nombreAlumno_2.setText ('')
        self.lineEdit_apellidoAlumno_2.setText ('')
        self.lineEdit_dniAlumno_2.setText ('')
        self.lineEdit_correoAlumno_2.setText ('')
        self.lineEdit_numTelAlumno_2.setText ('')
        self.dateEdit_nacimientoAlumno_2.setDate (ahora)
        self.lineEdit_ciudadAlumno_2.setText ('')
        self.lineEdit_direccionAlumno_2.setText ('')
        self.lineEdit_codigoPostalAlumno_2.setText ('')
        self.dateEdit_ingresoAlumno_2.setDate (ahora)
        self.lineEdit_idAlumno.setText ('')

    def actualizar_Alumno (self):
        conn = sqlite3.connect ('Base_de_Datos.db')
        consulta = "SELECT idAlumno,nombre,apellido,dni,correo,numTel,fechaNacimiento,ciudad,direccion,codigoPostal,fechaIngreso FROM alumnos WHERE estado=='cursando'"
        cursor = conn.cursor ()
        resultado = cursor.execute (consulta)
        for i in range (11):
            self.tableWidget_Registros_Alumno.resizeColumnToContents (i)
        self.tableWidget_Registros_Alumno.setRowCount (0)
        for row_number, row_data in enumerate (resultado):
            self.tableWidget_Registros_Alumno.insertRow (row_number)
            for column_number, data in enumerate (row_data):
                self.tableWidget_Registros_Alumno.setItem (row_number, column_number,
                                                           QtWidgets.QTableWidgetItem (str (data)))
        conn.close ()

    def borrar_Alumno (self):
        idborrar = self.lineEdit_idAlumno.text ().lstrip ()
        if not (idborrar.isspace () or idborrar == ''):
            conn = conexion ()
            BorrarAlumno (conn, idborrar)
            conn.close ()
            self.actualizar_Alumno ()
            self.lineEdit_idAlumno.setText ('')
            self.lineEdit_nombreAlumno_2.setText ('')
            self.lineEdit_apellidoAlumno_2.setText ('')
            self.lineEdit_dniAlumno_2.setText ('')
            self.lineEdit_correoAlumno_2.setText ('')
            self.lineEdit_numTelAlumno_2.setText ('')
            self.lineEdit_ciudadAlumno_2.setText ('')
            self.lineEdit_direccionAlumno_2.setText ('')
            self.lineEdit_codigoPostalAlumno_2.setText ('')
            self.label.setText ('')
            self.label_2.setText ('')

    #################--Matriculas--####################

    def registro_Matriculas(self, radioBox_PagoSemanal_Matriculas=None):
        if radioBox_PagoSemanal_Matriculas:
            pago = "Semanal"
        else:
            pago = "Anual"

        #numeroAlumno

    """

    def buscar_Matriculas(self):
        pass

    def borrar_Matriculas(self):
        pass

    def registro_Asistencias(self, checkBox_Clases=None):
        N_Alumno = self.lineEdit_Numero_Asistencias.text()
        Nombre = self.lineEdit_Nombre_Asistencias.text()
        Apellido = self.lineEdit_Apellido_Asistencias.text()
        Materias = self.lineEdit_Materias_Asistencias.text()
        Fechas = self.lineEdit_Fechas_Asistencias.text()
        if checkBox_Clases:
            clase = "Estuvo"
        else:
            clase = "No estuvo"

        self.lineEdit_Numero_Asistencias.setText("")
        self.lineEdit_Nombre_Asistencias.setText("")
        self.lineEdit_Apellido_Asistencias.setText("")
        self.lineEdit_Materias_Asistencias.setText("")
        self.lineEdit_Fechas_Asistencias.setText("")
        pass

    def buscar_Asistencias(self):
        # idborrar = self.lineEdit_Numero_Alumnos.text()
        # borrar_base_estudiante(conn, idborrar)
        # self.actualizarAlumno()
        # self.lineEdit_Numero_Alumnos.setText("")
        pass

    def borrar_Asistencias(self):
        pass

        """


conn = conexion ()
db_alumno (conn)
conn.close ()

app: Union[QApplication, QApplication] = QApplication ([])

main = MainWindow ()
# main.showMaximized()
main.show ()
app.exec_ ()
