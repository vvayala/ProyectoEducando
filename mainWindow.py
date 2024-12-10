import customtkinter as ctk
import pyodbc
from tkinter import messagebox

def bd(usuario, contrasena):
    try:
        connection = pyodbc.connect('Driver={SQL Server};' 'Server=.\SQLEXPRESS;' 'Database=Educando;' 'Trusted_connection=yes;')
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM Usuarios WHERE Usuario = ? AND Contrasena = ?", (usuario, contrasena)) 
        result = cursor.fetchone() 
        return result is not None 
    except pyodbc.Error as e: 
        messagebox.showerror("Error", f"Error en la conexión: {e}") 
        return

