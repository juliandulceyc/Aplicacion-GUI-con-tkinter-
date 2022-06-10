import tkinter as tk 
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        #Ventana principal 
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)
        #Configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        #Usuario 
        etiqueta1 = tk.Label(self, text='Usuario:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E, pady=5, padx=5)
        self.entrada1 = ttk.Entry(self)
        self.entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        #Password
        etiqueta2 = tk.Label(self, text='Password:')
        etiqueta2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.entrada2 = ttk.Entry(self, show='*')
        self.entrada2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        #Botón
        boton1 = ttk.Button(self, text='Login', command=self._login)
        boton1.grid(row=3, column=0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login',
                            f'Usuario: {self.entrada1.get()}, Password: {self.entrada2.get()}')

# Ejecutar la ventana
if __name__=='__main__':
    login_ventana= Login()
    login_ventana.mainloop()
