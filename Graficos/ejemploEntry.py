from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()


cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

nombreDireccion=Label(miFrame, text="Direccion de casa:")
nombreDireccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password:")
PassLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()

