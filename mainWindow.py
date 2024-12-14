import customtkinter as ctk
import pyodbc
from tkinter import messagebox

connection = None
def conexion():
    global connection 
    try:
        connection = pyodbc.connect('Driver={SQL Server};' 'Server=.\SQLEXPRESS;' 'Database=Educando;' 'Trusted_connection=yes;')
        cursor = connection.cursor() 

        return cursor
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}") 
        return None
    
    
def bd(usuario, contrasena):
    try:
        cursor = conexion()
        cursor.execute("SELECT * FROM Usuarios WHERE Usuario = ? AND Contrasena = ?", (usuario, contrasena)) 
        result = cursor.fetchone() 
        return result is not None 
    except pyodbc.Error as e: 
        messagebox.showerror("Error", f"Error en la conexión: {e}") 
        return
    
def registrarUsuario(nombre, password, email):
    try:
        cursor = conexion()
        
        # Verificar si el usuario ya está registrado
        cursor.execute("SELECT * FROM Usuarios WHERE Email = ?", email)
        if cursor.fetchone():
            connection.close()
            messagebox.showerror("Error","El email ya ha sido registrado")
            return
          
        # Insertar el nuevo usuario en la base de datos
        cursor.execute("INSERT INTO Usuarios VALUES (?, ?, ?)", 
                       (nombre,password,email))
        connection.commit()
        connection.close()
        return True
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}") 
        return 
    
import pyodbc
from tkinter import messagebox

def getLectura(name):
    try:
        cursor = conexion()
        
        # Realizar la consulta para obtener la lectura
        cursor.execute("SELECT Contenido FROM Lecciones WHERE NombreLeccion = ?", name)
        result = cursor.fetchone()
        connection.close()
        return result[0]
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")


def getLectura(name):
    try:
        cursor = conexion()
        
        # Realizar la consulta para obtener la lectura
        cursor.execute("SELECT Contenido FROM Lecciones WHERE NombreLeccion = ?", name)
        result = cursor.fetchone()
        connection.close()
        return result[0]
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")

def verProgreso():
    try:
        cursor = conexion()
        
        query = """SELECT U.Usuario AS 'USUARIOS', 
        COUNT(L.IDLeccion) AS 'LECCIONES COMPLETADAS',
        SUM(L.TotalPreguntas) AS 'TOTAL PREGUNTAS',
        SUM(L.RespuestasCorrectas) AS 'RESPUESTAS CORRECTAS',
        CONCAT(SUM(DATEDIFF(MINUTE, L.Inicio, L.Fin)) / 60, ' horas, ', 
        SUM(DATEDIFF(MINUTE, L.Inicio, L.Fin)) % 60, ' minutos') AS 'DURACION'
        FROM Usuarios U INNER JOIN LeccionesCompletadas L ON U.IDUsuario = L.IDUsuario
        GROUP BY U.Usuario"""

        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")

def getUsuarios():
    try:
        cursor = conexion()
        
        cursor.execute("SELECT Usuario FROM Usuarios")
        result = cursor.fetchall()
        usuarios = []
        for row in result:
            usuarios.append(row[0])

        connection.close()
        return usuarios
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")

def getUsuariosInfo(nombre):
    try:
        cursor = conexion()
        
        query = """SELECT U.Usuario AS 'USUARIOS', 
        COUNT(L.IDLeccion) AS 'LECCIONES COMPLETADAS',
        SUM(L.TotalPreguntas) AS 'TOTAL PREGUNTAS',
        SUM(L.RespuestasCorrectas) AS 'RESPUESTAS CORRECTAS',
        CONCAT(SUM(DATEDIFF(MINUTE, L.Inicio, L.Fin)) / 60, ' horas, ', 
        SUM(DATEDIFF(MINUTE, L.Inicio, L.Fin)) % 60, ' minutos') AS 'DURACION'
        FROM Usuarios U INNER JOIN LeccionesCompletadas L ON U.IDUsuario = L.IDUsuario
        WHERE U.Usuario = ?
        GROUP BY U.Usuario"""

        cursor.execute(query,nombre)
        result = cursor.fetchall()
        connection.close()
        return result
    
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")
