def IngresarAlumno(conn,data):
    cursor = conn.cursor()
    print("data",data)
    cursor.execute("INSERT INTO alumnos (nombre,apellido,dni,correo,numTel,fechaNacimiento,ciudad,direccion,codigoPostal,fechaIngreso,estado) VALUES  (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)",data)
    conn.commit()

def BuscarAlumno(conn,dato):  #Buscar determinados Alumnos
    cursor=conn.cursor()
    cursor.execute ("SELECT * FROM alumnos WHERE nombre like ? and apellido like ? and dni like ? and correo like ? and numTel like ? and ciudad like ? and direccion like ? and codigoPostal like ?",dato)
    return cursor

def BuscarAlumnoModificar(conn,idAlumnoModificar):
    if idAlumnoModificar=='' or idAlumnoModificar.strip()=='':
        idAlumnoModificar='0'
    cursor=conn.cursor()
    cursor.execute("SELECT idAlumno,nombre,apellido,dni,correo,numTel,fechaNacimiento,ciudad,direccion,codigoPostal,fechaIngreso FROM alumnos WHERE idAlumno=(?) and EXISTS (SELECT * FROM alumnos WHERE idAlumno=(?))",(idAlumnoModificar,idAlumnoModificar))
    alumno = cursor.fetchall()
    if not alumno:
        alumno = [('','','','','','','','','','','')]
    elif alumno == []:
        alumno = [('', '', '', '', '', '', '', '', '', '', '')]
    else:pass
    return alumno

def extraer_base_registro(conn):
    cursor = conn.cursor()
    cursor.execute("ID_Alumnos, Nombre, Apellido, DNI, Fecha_Nacimiento, Ciudad, Codigo_Postal, Fecha_de_Ingreso, "
                   "Fecha_de_Salida, Direccion, Correo, NumeroTelefonoCelular FROM Registros")
    return cursor

def ModificarAlumno(conn,dato,idmod):
    cursor=conn.cursor()
    actualizanombreAlumno=[dato[0],idmod]
    actualizaapellidoAlumno=[dato[1],idmod]
    actualizadniAlumno=[dato[2],idmod]
    actualizacorreoAlumno=[dato[3],idmod]
    actualizanumTelAlumno=[dato[4],idmod]
    actualizafechaNacimientoAlumno=[dato[5],idmod]   ######
    actualizaciudadAlumno=[dato[6],idmod]
    actualizadireccionAlumno=[dato[7],idmod]
    actualizacodPostalAlumno=[dato[8],idmod]
    actualizafechaIngresoAlumno=[dato[9],idmod]    ########
    cursor.execute ("UPDATE alumnos SET nombre=(?) WHERE idAlumno=(?);",actualizanombreAlumno)
    cursor.execute ("UPDATE alumnos SET apellido=(?) WHERE idAlumno=(?);", actualizaapellidoAlumno)
    cursor.execute ("UPDATE alumnos SET dni=(?) WHERE idAlumno=(?);", actualizadniAlumno)
    cursor.execute ("UPDATE alumnos SET correo=(?) WHERE idAlumno=(?);", actualizacorreoAlumno)
    cursor.execute ("UPDATE alumnos SET numTel=(?) WHERE idAlumno=(?);", actualizanumTelAlumno)
    cursor.execute ("UPDATE alumnos SET fechaNacimiento=(?) WHERE idAlumno=(?);", actualizafechaNacimientoAlumno)   ######
    cursor.execute ("UPDATE alumnos SET ciudad=(?) WHERE idAlumno=(?);", actualizaciudadAlumno)
    cursor.execute ("UPDATE alumnos SET direccion=(?) WHERE idAlumno=(?);", actualizadireccionAlumno)
    cursor.execute ("UPDATE alumnos SET codigoPostal=(?) WHERE idAlumno=(?);", actualizacodPostalAlumno)
    cursor.execute ("UPDATE alumnos SET fechaIngreso=(?) WHERE idAlumno=(?);", actualizafechaIngresoAlumno)    #######
    conn.commit()

def BorrarAlumno(conn,idBorrar):
    if idBorrar!='':
        cursor=conn.cursor()
        cursor.execute("DELETE FROM alumnos WHERE idAlumno=(?);",(idBorrar,))
        cursor.execute("UPDATE alumnos SET idAlumno=idAlumno-1 WHERE idAlumno>(?);",(idBorrar,))
        conn.commit()
    else:
        print("No se borra alumno")
