from tkinter import *

root=Tk()

def imprimir():

	#print(varOpcion.get())

	if varOpcion.get()==1:

		etiqueta.config(text="Has elegido masculino")

	elif varOpcion.get()==2:

		etiqueta.config(text="Has elegido No-Binario")

	elif varOpcion.get()==3:

		etiqueta.config(text="Has elegido Helicoptero Apache")

	else:

		etiqueta.config(text="Has elegido femenino")

varOpcion=IntVar()

Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="femenino", variable=varOpcion, value=4, command=imprimir).pack()

Radiobutton(root, text="No-Binario", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Helicoptero Apache", variable=varOpcion, value=3, command=imprimir).pack()



etiqueta=Label(root)
etiqueta.pack()


root.mainloop()