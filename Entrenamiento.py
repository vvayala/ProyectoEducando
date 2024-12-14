import tkinter as tk
from tkinter import messagebox, ttk
from quiz_datos import quiz_datos

pregunta_actual = 0

def comprobar_resp(choice):
    pregunta = quiz_datos[pregunta_actual]
    seleccion = opciones_botones[choice].cget("text")

    if seleccion == pregunta["respuesta"]:
        global score
        score += 1
        nota.config(text="Score: {}/{}".format(score, len(quiz_datos)))
        resultado_titulo.config(text="Correcto!", foreground="green")
    else:
        resultado_titulo.config(text="Incorrecto!", foreground="red")

    for boton in opciones_botones:
        boton.config(state="disabled")
    siguiente_boton.config(state="normal")

def sig_pregunta():
    global pregunta_actual
    pregunta_actual += 1
    
    if pregunta_actual < len(quiz_datos):
        mostrar_pregunta()
    else:
        messagebox.showinfo("Sesión completada",
                            "Preguntas acertadas: {}/{}".format(score, len(quiz_datos)))
        root.quit()

def mostrar_pregunta():
    pregunta = quiz_datos[pregunta_actual]
    pregunta_titulo.config(text=pregunta["pregunta"])

    opciones = pregunta["opciones"]
    for i in range(4):
        opciones_botones[i].config(text = opciones[i], state = "normal")

    resultado_titulo.config(text="")
    siguiente_boton.config(state="disabled")

root = tk.Tk()
root.title("Sesion de entrenamiento")
root.geometry("500x400")

pregunta_titulo = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
pregunta_titulo.pack(pady=10)

opciones_botones = []
for i in range(4):
    boton = ttk.Button(
        root,
        command=lambda i=i: comprobar_resp(i)
    )
    boton.pack(pady=5)
    opciones_botones.append(boton)

resultado_titulo = ttk.Label(
    root,
    anchor = "center",
    padding = 10
)
resultado_titulo.pack(pady=10)

#resultado
score = 0

nota= ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_datos)),
    anchor="center",
    padding=10
)
nota.pack(pady=10)

siguiente_boton = ttk.Button(
    root,
    text="Siguiente",
    command= sig_pregunta,
    state="disabled"
)
siguiente_boton.pack(pady=10)

mostrar_pregunta()


root.mainloop()