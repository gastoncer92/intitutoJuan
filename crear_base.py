import sqlite3

def conexion():
    conn = sqlite3.connect('Base_de_Datos.db')
    return conn

def data_base_Asistencias(conn):
    cursor = conn.cursor()
    cursor.executescript("""
CREATE TABLE "Asistencias" (
	"ID_Alumno"	INTEGER NOT NULL,
	"Nombre"	TEXT,
	"Apellido"	TEXT,
	"Fechas"	TEXT,
	"Materias"	TEXT,
	"Clases"	INTEGER,
	PRIMARY KEY("ID_Alumno" AUTOINCREMENT)
)
""")


def data_base_Matriculas(conn):
    cursor = conn.cursor()
    cursor.executescript("""
CREATE TABLE "Matriculas" (
	"PagoAnual"	INTEGER,
	"PagoSemanal"	INTEGER,
	"MontodelPago"	REAL,
	"RegistrodelaPaga"	TEXT
)
""")

def db_alumno2(conn):
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS [registro] (
[id] INTEGER  NOT NULL PRIMARY KEY,
[nombre] VARCHAR(15)  NULL,
[apellido] VARCHAR(15)  NULL,
[dni] VARCHAR(15) NULL,
[fechadenacimiento] VARCHAR(15) NULL,
[ciudad] VARCHAR(15) NULL,
[fechadesalida] VARCHAR(15) NULL,
[direccion] VARCHAR(15)  NULL,
[correo] VARCHAR(15)  NULL,
[telefono] VARCHAR(15)  NULL
)""")

def db_alumno(conn):
    cursor=conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS [alumnos] (
[idAlumno] INTEGER  NOT NULL PRIMARY KEY,
[nombre] VARCHAR(15)  NULL,
[apellido] VARCHAR(15)  NULL,
[dni] VARCHAR(15)  NULL,
[correo] VARCHAR(15)  NULL,
[numTel] VARCHAR(15)  NULL,
[fechaNacimiento] VARCHAR(15)  NULL,
[ciudad] VARCHAR(15)  NULL,
[direccion] VARCHAR(15)  NULL,
[codigoPostal] VARCHAR(15)  NULL,
[fechaIngreso] VARCHAR(15)  NULL,
[estado] VARCHAR(10)  NULL
)""")