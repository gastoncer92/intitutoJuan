def insertar_base_asistencias(conn, asistencias):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Asistencias(ID_Alumnos, Nombre, Apellido, Materias, Fechas, Clases) VALUES(?,?,?,?,?,?)", asistencias)
    conn.commit()

def extraer_base_asistencias(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT ID_Alumnos, Nombre, Apellido, Materias, Fechas, Clases FROM Asistencias")
    return cursor

def borrar_base_asistencias(conn, cursor=None, idborrar=None):
    cursor.conn.cursor()
    cursor.execute("DELETE FROM Asistencias WHERE ID_Alumnos", idborrar)
    cursor.execute("UPDATE Asistencias SET ID_Alumnos=ID_Alumnos-1 WHERE ID_Alumnos > ?", idborrar)

    conn.commit()