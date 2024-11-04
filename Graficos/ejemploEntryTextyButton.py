from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

nombreDireccion=Label(miFrame, text="Direccion de casa:")
nombreDireccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password:")
PassLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

ComentariosLabel=Label(miFrame, text="Comentarios:")
ComentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
	
	minombre.set("Juan")


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()

