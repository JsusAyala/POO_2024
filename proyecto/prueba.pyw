import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Configurar la ventana
root.title("Mi Aplicación")
root.geometry("400x300")

# Crear una etiqueta
label = tk.Label(root, text="¡Hola, Mundo!")
label.pack()

# Crear una función para el botón
def on_click():
    label.config(text="¡Botón presionado!")

# Crear un botón
button = tk.Button(root, text="Presiona aquí", command=on_click)
button.pack()

# Ejecutar el loop principal
root.mainloop()
