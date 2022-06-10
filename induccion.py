import tkinter as tk 
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configurar el grid 
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Método de los eventos 
def evento1():
    boton1.config(text='Boton 1 presionado')

def evento2():
    boton2.config(text='Boton 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, background='yellow')

# Definimos dos botones 
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSEW', 
            padx=40, pady=30, ipadx=20, ipady=50,) #columnspan=2, rowspan=2)

# N(arriba), E(derecha), S(abajo), W(izquierda) ## Combinacion de dos 'letras' => para centrar
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1, column=0, sticky='NSWE')

# Boton3
boton3 = ttk.Button(ventana, text='Botón 3')
boton3.grid(row=0, column=1, sticky='NSWE')

# Botón 4
boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSEW')

ventana.mainloop()
