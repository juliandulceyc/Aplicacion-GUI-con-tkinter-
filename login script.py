import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0)

#Configuración del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

#Usuario 
etiqueta1 = tk.Label(ventana, text='Usuario:')
etiqueta1.grid(row=0, column=0, sticky=tk.E, pady=5, padx=5)

entrada1 = ttk.Entry(ventana)
entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

#Password
etiqueta2 = tk.Label(ventana, text='Password:')
etiqueta2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

entrada2 = ttk.Entry(ventana, show='*')
entrada2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

#Botón
def login():
    messagebox.showinfo('Datos Login',
                        f'Usuario: {entrada1.get()}, Password: {entrada2.get()}')

boton1 = ttk.Button(ventana, text='Login', command=login)
boton1.grid(row=3, column=0, columnspan=2)

ventana.mainloop()