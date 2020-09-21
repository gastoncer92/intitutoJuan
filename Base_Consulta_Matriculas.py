def insertar_base_matriculas(conn, matricula):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Matriculas(ID_Alumnos, Pago_Anual, Pago_Semanal, Monto_del_Pago, Registro_de_la_Paga) VALUES(?,?,?,?)", matricula)
    conn.commit()

def extraer_base_matriculas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT ID_Alumnos, Pago_Anual, Pago_Semanal, Monto_del_Pago, Registro_de_la_Paga FROM Matriculas")
    return cursor

def borrar_base_matriculas(conn, cursor=None, idborrar=None):
    cursor.conn.cursor()
    cursor.execute("DELETE FROM Matriculas WHERE ID_Alumnos", idborrar)
    cursor.execute("UPDATE Matriculas SET ID_Alumnos=ID_Alumnos-1 WHERE ID_Alumnos > ?", idborrar)
    conn.commit()