import customtkinter as ctk
import mainWindow

#Definir apariencia
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry("400x400")
app.title("Inicio de sesion")


def login():
    app.destroy()
    mainWindow.bd('test','1245')     


# Definir el label
label = ctk.CTkLabel(app,text="Inicio de sesion") 
label.pack(pady=20) 

# Crear el frame
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40, 
		fill='both',expand=True) 

# Agregar label a frame
label = ctk.CTkLabel(master=frame, 
					text='Ingrese su usuario y contrasena:') 
label.pack(pady=12,padx=10) 

# Agregar textbox para usuaroi
user_entry= ctk.CTkEntry(master=frame, 
						placeholder_text="Usuario") 
user_entry.pack(pady=12,padx=10) 

# Agregar textbox para pass
user_pass= ctk.CTkEntry(master=frame, 
						placeholder_text="Contrasena", 
						show="*") 
user_pass.pack(pady=12,padx=10) 

# CCreacion del boton login
button = ctk.CTkButton(master=frame, 
					text='Login',command=login) 
button.pack(pady=12,padx=10) 

app.mainloop()
