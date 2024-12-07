import customtkinter as ctk
import pyodbc


def bd():
    connection = pyodbc.connect('Driver={SQL Server};' 'Server=.\SQLEXPRESS;' 'Database=ITCAPlus;' 'Trusted_connection=yes;')
    if connection:
        print(True)
bd()

