import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore

# Diccionarios para almacenar datos
usuarios = {}
grupos = {"Tradicional": [], "Interactivo": []}

# Ventana principal
def iniciar_aplicacion():
    ventana = tk.Tk()
    ventana.title("Aplicación Educativa Interactiva")
    ventana.geometry("800x600")
    ventana.configure(bg="#f0f8ff")  # Fondo azul claro

    tk.Label(
        ventana,
        text="Bienvenido a la Aplicación Educativa",
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
        ("Revisiones de Lectura", ventana_lecturas),
        ("Sesión de Entrenamiento", ventana_entrenamiento),
        ("Ver Progreso de Usuarios", mostrar_progreso),
        ("Comparar Grupos de Control", comparar_grupos),
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
        grupo = var_grupo.get()
        if not nombre or grupo not in grupos:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
            return
        if nombre in usuarios:
            messagebox.showerror("Error", "El usuario ya está registrado.")
            return
        usuarios[nombre] = {"grupo": grupo, "lecturas": 0, "entrenamientos": 0, "tiempo_uso": 0}
        grupos[grupo].append(nombre)
        messagebox.showinfo("Éxito", f"Usuario {nombre} registrado en el grupo {grupo}.")
        ventana_registro.destroy()

    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de Usuarios")
    ventana_registro.geometry("400x300")
    ventana_registro.configure(bg="#f0f8ff")

    tk.Label(ventana_registro, text="Nombre:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
    entrada_nombre = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_nombre.pack()

    var_grupo = tk.StringVar(value="Tradicional")
    tk.Label(ventana_registro, text="Selecciona un grupo:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
    tk.Radiobutton(ventana_registro, text="Tradicional", variable=var_grupo, value="Tradicional", bg="#f0f8ff").pack()
    tk.Radiobutton(ventana_registro, text="Interactivo", variable=var_grupo, value="Interactivo", bg="#f0f8ff").pack()

    tk.Button(ventana_registro, text="Registrar", command=registrar, bg="#4caf50", fg="white").pack(pady=20)


def ventana_lecturas():
    usuario = seleccionar_usuario()
    if not usuario:
        return
    start_time = datetime.now()
    time.sleep(2)
    end_time = datetime.now()
    tiempo = (end_time - start_time).seconds
    usuarios[usuario]["lecturas"] += 1
    usuarios[usuario]["tiempo_uso"] += tiempo
    messagebox.showinfo("Actividad Completa", f"Lectura completada por {usuario} en {tiempo} segundos.")


def ventana_entrenamiento():
    usuario = seleccionar_usuario()
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
    if not usuarios:
        messagebox.showerror("Error", "No hay usuarios registrados.")
        return

    ventana_progreso = tk.Toplevel()
    ventana_progreso.title("Progreso de Usuarios")
    ventana_progreso.geometry("800x600")

    nombres = list(usuarios.keys())
    tiempos = [usuarios[nombre]["tiempo_uso"] for nombre in nombres]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(nombres, tiempos, color="#4caf50")
    ax.set_title("Progreso por Usuario", fontsize=16)
    ax.set_ylabel("Tiempo de Uso (s)", fontsize=12)
    ax.set_xlabel("Usuarios", fontsize=12)

    canvas = FigureCanvasTkAgg(fig, master=ventana_progreso)
    canvas.draw()
    canvas.get_tk_widget().pack()


def comparar_grupos():
    if not grupos["Tradicional"] and not grupos["Interactivo"]:
        messagebox.showerror("Error", "No hay datos para comparar.")
        return

    ventana_comparacion = tk.Toplevel()
    ventana_comparacion.title("Comparación de Grupos")
    ventana_comparacion.geometry("800x600")

    grupos_nombres = ["Tradicional", "Interactivo"]
    tiempos = [
        sum(usuarios[usuario]["tiempo_uso"] for usuario in grupos[grupo])
        for grupo in grupos_nombres
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(grupos_nombres, tiempos, color=["#2196f3", "#ff9800"])
    ax.set_title("Comparación de Grupos de Control", fontsize=16)
    ax.set_ylabel("Tiempo Total (s)", fontsize=12)
    ax.set_xlabel("Grupos", fontsize=12)

    canvas = FigureCanvasTkAgg(fig, master=ventana_comparacion)
    canvas.draw()
    canvas.get_tk_widget().pack()


def seleccionar_usuario():
    if not usuarios:
        messagebox.showerror("Error", "No hay usuarios registrados.")
        return None

    def seleccionar():
        seleccion = lista_usuarios.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un usuario.")
            return
        usuario_seleccionado.set(lista_usuarios.get(seleccion))
        ventana_seleccion.destroy()

    ventana_seleccion = tk.Toplevel()
    ventana_seleccion.title("Seleccionar Usuario")
    ventana_seleccion.geometry("300x300")
    usuario_seleccionado = tk.StringVar()

    tk.Label(ventana_seleccion, text="Selecciona un usuario:").pack(pady=10)
    lista_usuarios = tk.Listbox(ventana_seleccion)
    lista_usuarios.pack()
    for usuario in usuarios:
        lista_usuarios.insert(tk.END, usuario)

    tk.Button(ventana_seleccion, text="Seleccionar", command=seleccionar).pack(pady=20)
    ventana_seleccion.wait_window()
    return usuario_seleccionado.get()


# Iniciar la aplicación
if __name__ == "__main__":
    iniciar_aplicacion()
