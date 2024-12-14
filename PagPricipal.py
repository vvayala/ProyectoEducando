import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import time
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
import mainWindow
import json


# Diccionarios para almacenar datos
usuarios = {}
grupos = {"Tradicional": [], "Interactivo": []}

# Ventana principal
def iniciar_aplicacion(usuario):
    ventana = tk.Tk()
    ventana.title("Aplicación Educativa Interactiva")
    ventana.geometry("800x600")
    ventana.configure(bg="#f0f8ff")  # Fondo azul claro

    tk.Label(
        ventana,
        text=f"Bienvenido a la Aplicación Educativa {usuario}",
        font=("Arial", 20, "bold"),
        fg="#333",
        bg="#f0f8ff",
    ).pack(pady=20)

    # Estilo para botones
    estilo_botones = {
        "font": ("Arial", 12),
        "bg": "#4caf50",
        "fg": "white",
        "activebackground": "#45a049",
        "relief": tk.RAISED,
        "width": 30,
        "height": 2,
    }

    # Contenedor de botones para mejorar la organización
    contenedor_botones = tk.Frame(ventana, bg="#f0f8ff")
    contenedor_botones.pack(pady=10)

    botones = [
        ("Registro de Usuarios", ventana_registro),
        ("Revisiones de Lectura", lecturas),
        ("Sesión de Entrenamiento", ventana_entrenamiento),
        ("Ver Progreso de Usuarios", mostrar_progreso),
        ("Comparar Grupos de Control",lambda : comparar_resultados(usuario)),
    ]

    for texto, comando in botones:
        tk.Button(
            contenedor_botones, text=texto, command=comando, **estilo_botones
        ).pack(pady=5)

    tk.Button(
        ventana,
        text="Salir",
        command=ventana.quit,
        font=("Arial", 12),
        bg="#f44336",
        fg="white",
        activebackground="#e53935",
        relief=tk.RAISED,
        width=20,
        height=2,
    ).pack(pady=20)

    ventana.mainloop()


# Funciones principales (registro, revisiones, entrenamiento, progreso y comparaciones)
def ventana_registro():
    def registrar():
        nombre = entrada_nombre.get()
        contrasena = entrada_contrasena.get()
        email = entrada_email.get()
        
        if not nombre or not contrasena or not email:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
            return
        
        if mainWindow.registrarUsuario(nombre, contrasena, email):
            messagebox.showinfo("Completado","Usuario agregado con exito!")
            ventana_registro.destroy()

    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de Usuarios")
    ventana_registro.geometry("400x300")
    ventana_registro.configure(bg="#f0f8ff")

    tk.Label(ventana_registro, text="Nombre:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
    entrada_nombre = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_nombre.pack()

    tk.Label(ventana_registro, text="Contraseña:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
    entrada_contrasena = tk.Entry(ventana_registro, show='*', font=("Arial", 12))
    entrada_contrasena.pack()

    tk.Label(ventana_registro, text="Email:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
    entrada_email = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_email.pack()

    tk.Button(ventana_registro, text="Registrar", command=registrar, bg="#4caf50", fg="white").pack(pady=20)

# funciones implementadas para las lecturas
archivo_json = "cuentos/cuentos_lecturas.json"

def cargar_cuentos(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def leer_contenido_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def mostrar_cuento(cuento, usuario):
    ventana_cuento = tk.Toplevel()
    ventana_cuento.title(cuento['titulo'])
    ventana_cuento.resizable(False,False)
    ventana_cuento.geometry("600x660")

    titulo_label = tk.Label(ventana_cuento, text=f"Título: {cuento['titulo']}", font=("Arial", 16, "bold"), wraplength=500)
    titulo_label.pack(pady=10)

    autor_label = tk.Label(ventana_cuento, text=f"Autor: {cuento.get('autor', 'Desconocido')}", font=("Arial", 12, "italic"))
    autor_label.pack(pady=5)

    contenido_text = scrolledtext.ScrolledText(ventana_cuento, wrap=tk.WORD, width=70, height=25, font=("Arial", 12))
    contenido_text.pack(pady=10)

    contenido = leer_contenido_archivo(cuento["contenido"])
    contenido_text.insert(tk.END, contenido)
    
     # Función que se ejecutará al cerrar la ventana o al presionar el botón "Finalizar"
    def on_closing():
        end_time = datetime.now()
        tiempo = (end_time - start_time).seconds
        # usuarios[usuario]["lecturas"] += 1
        # usuarios[usuario]["tiempo_uso"] += tiempo
        messagebox.showinfo("Actividad Completa", f"Lectura completada por {usuario} en {tiempo} segundos.")
        ventana_cuento.destroy()

    finalizar_button = tk.Button(ventana_cuento, 
                                text="Finalizar",  
                                bg="#4CAF50",  
                                borderwidth=2, 
                                fg="white",
                                relief="raised",  
                                font=("Arial", 12, "bold"), command=on_closing)
    finalizar_button.pack(pady=20)
    start_time = datetime.now()
    ventana_cuento.protocol("WM_DELETE_WINDOW", on_closing)

def crear_botones(ventana, cuentos, usuario):
    for cuento in cuentos:
        boton = tk.Button(ventana, 
                          text=cuento['titulo'], 
                          command=lambda c=cuento: mostrar_cuento(c, usuario),
                          font=("Arial", 12), 
                          fg="white",  # Color 
                          bg="#4CAF50",  #  fondo
                          relief="raised",  # borde
                          borderwidth=2,
                          width=34, #ancho en x
                          height=2,  # Alto en y
                          padx=10,  
                          pady=5) 
        boton.pack(pady=5)

        
def lecturas():
    
    cuentos = cargar_cuentos(archivo_json)

    ventana = tk.Toplevel()
    ventana.title("Sección de lectura")
    ventana.geometry("600x600")

    titulo_label = tk.Label(ventana, text="Cuentos Disponibles", font=("Arial", 16, "bold"), wraplength=500)
    titulo_label.pack(pady=10)

    crear_botones(ventana, cuentos, 0)
    
    
    # def verLectura(nombre):
    #     contenido = mainWindow.getLectura(nombre)  
    #     verLectura = tk.Toplevel()
    #     verLectura.title(nombre)
    #     verLectura.geometry("400x800")
    #     verLectura.configure(bg="#f0f8ff")

    #     txtFrame = tk.Frame(verLectura, bg="#f0f8ff")
    #     txtFrame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10) 
    #     text_widget = tk.Text(txtFrame, wrap=tk.WORD, font=("Arial", 12), bg="#f0f8ff", state=tk.NORMAL) 
    #     text_widget.insert(tk.END, contenido) 
    #     text_widget.config(state=tk.DISABLED) 
    #     # Hacer que el widget de texto sea de solo lectura 
    #     scrollbar = tk.Scrollbar(txtFrame, command=text_widget.yview) 
    #     text_widget.configure(yscrollcommand=scrollbar.set) 
    #     scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
    #     text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #     tk.Button(verLectura, text="Finalizar", command=verLectura.destroy, bg="#4caf50", fg="white").pack(pady=20)


    # lecturas = tk.Toplevel()
    # lecturas.title("Lecturas disponibles")
    # lecturas.geometry("400x200")
    # lecturas.configure(bg="#f0f8ff")
    # lecturas.grid_columnconfigure(0,weight=1)
    # lecturas.grid_columnconfigure(1,weight=1)

    # tk.Button(lecturas, text="La caperucita roja", command=lambda : verLectura("La caperucita roja"), bg="#4caf50", fg="white").grid(row=0, column=0, padx=20, pady=20)
    # tk.Button(lecturas, text="Blancanieves", command= lambda : verLectura("Blancanieves"), bg="#4caf50", fg="white").grid(row=0, column=1, padx=20, pady=20)
    # tk.Button(lecturas, text="La cenicienta", command= lambda : verLectura("La cenicienta"), bg="#4caf50", fg="white").grid(row=1, column=0, padx=20, pady=20)
    # tk.Button(lecturas, text="La bella y la bestia",command= lambda : verLectura("La bella y la bestia"), bg="#4caf50", fg="white").grid(row=1, column=1, padx=20, pady=20)
    # tk.Button(lecturas, text="La bella durmiente", command= lambda : verLectura("La bella durmiente"), bg="#4caf50", fg="white").grid(row=2, column=0, padx=20, pady=20) 

def ventana_entrenamiento():
    usuario = 0
    if not usuario:
        return
    start_time = datetime.now()
    time.sleep(3)
    end_time = datetime.now()
    tiempo = (end_time - start_time).seconds
    usuarios[usuario]["entrenamientos"] += 1
    usuarios[usuario]["tiempo_uso"] += tiempo
    messagebox.showinfo("Actividad Completa", f"Entrenamiento completado por {usuario} en {tiempo} segundos.")


def mostrar_progreso():
    mostrar_progreso = tk.Toplevel()
    mostrar_progreso.title("Progreso de usuarios")
    mostrar_progreso.geometry("800x600")

    datos = mainWindow.verProgreso()
    
    # Crear el Treeview
    tree = ttk.Treeview(mostrar_progreso)
    tree.pack(expand=True, fill='both')
    
    # Definir las columnas
    tree["columns"] = ("USUARIOS", "LECCIONES COMPLETADAS", "TOTAL PREGUNTAS", "RESPUESTAS CORRECTAS", "Duracion",)
    
    # Configurar encabezados de columna
    tree.column("#0", width=0, stretch=tk.NO)
    tree.heading("#0", text="", anchor=tk.W)
    
    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=150)
        tree.heading(col, text=col, anchor=tk.W)
    # Insertar datos en el Treeview
    for row in datos:
      tree.insert("", tk.END, values=[row[0],row[1],row[2],row[3], row[4:]])

def comparar_resultados(usuario):
    comparar_resultados = tk.Toplevel()
    comparar_resultados.title("Resultados")
    comparar_resultados.geometry("800x400")

    usuarios = mainWindow.getUsuarios()

    comparar_resultados.grid_columnconfigure(0,weight=1)
    comparar_resultados.grid_columnconfigure(1,weight=1)
    comparar_resultados.grid_columnconfigure(2,weight=1)    
    
    tk.Label(comparar_resultados, text="Selecciona un Usuario:").grid(row=1, column=0, padx=20, pady=20)  
    combo = ttk.Combobox(comparar_resultados, values=usuarios)
    combo.grid(row=2, column=0, padx=20, pady=20) 
    tk.Label(comparar_resultados, text="Resultados").grid(row=3, column=0, padx=20, pady=20) 
    tk.Label(comparar_resultados, text="Lecciones completadas").grid(row=4, column=0, padx=20, pady=20) 
    tk.Label(comparar_resultados, text="Total preguntas").grid(row=5, column=0, padx=20, pady=20) 
    tk.Label(comparar_resultados, text="Respuestas correctas").grid(row=6, column=0, padx=20, pady=20) 
    tk.Label(comparar_resultados, text="Duracion").grid(row=7, column=0, padx=20, pady=20) 

    actualUser = mainWindow.getUsuariosInfo(usuario)

    if len(actualUser) > 0:
        tk.Label(comparar_resultados, text=actualUser[0][0]).grid(row=3, column=1, padx=20, pady=20) 
        tk.Label(comparar_resultados, text=actualUser[0][1]).grid(row=4, column=1, padx=20, pady=20) 
        tk.Label(comparar_resultados, text=actualUser[0][2]).grid(row=5, column=1, padx=20, pady=20) 
        tk.Label(comparar_resultados, text=actualUser[0][3]).grid(row=6, column=1, padx=20, pady=20) 
        tk.Label(comparar_resultados, text=actualUser[0][4:]).grid(row=7, column=1, padx=20, pady=20) 
    else:
        messagebox.showerror("Error","El usuario no tiene lecciones")
        comparar_resultados.destroy()
    
    def seleccionar_usuario(event): 
        newUser = mainWindow.getUsuariosInfo(combo.get())
        if len(newUser) > 0:
            tk.Label(comparar_resultados, text=newUser[0][0]).grid(row=3, column=2, padx=20, pady=20) 
            tk.Label(comparar_resultados, text=newUser[0][1]).grid(row=4, column=2, padx=20, pady=20) 
            tk.Label(comparar_resultados, text=newUser[0][2]).grid(row=5, column=2, padx=20, pady=20) 
            tk.Label(comparar_resultados, text=newUser[0][3]).grid(row=6, column=2, padx=20, pady=20) 
            tk.Label(comparar_resultados, text=newUser[0][4:]).grid(row=7, column=2, padx=20, pady=20) 
        else:
            messagebox.showerror("Error","El usuario no tiene lecciones")
            comparar_resultados.destroy()

    combo.bind("<<ComboboxSelected>>",seleccionar_usuario)

# Iniciar la aplicación
if __name__ == "__main__":
    iniciar_aplicacion()
