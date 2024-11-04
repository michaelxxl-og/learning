from tkinter import *
from tkinter import messagebox

root=Tk()

#-----------Funciones-----------------

def infoAdicinal():
	messagebox.showinfo("Procesador de Mike", "Procesador de texto V.2023")

def avisoLicencia():
	messagebox.showwarning("Licencia", "producto bajo licencia GNU")
	
def SalirAplicacion():
	#valor=messagebox.askquestion("Salir", "Quieres salir de la app?")

	#"askquestion dispone del si y no, quiere decir que el valor es `yes`o`no`, y
	#con askokcancel es `true`o`False

	valor=messagebox.askokcancel("Salir", "Quieres salir de la app?")

	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
	if valor==False:
		root.destroy()


#---------------------------------------- 

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")

#-----------------------------

archivoMenu.add_separator()

#-----------------------------

archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=SalirAplicacion)

#-----------------------------

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#-----------------------------

archivoTools=Menu(barraMenu, tearoff=0)

#-----------------------------

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicinal)

#-----------------------------
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

#-----------------------------
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

#-----------------------------
barraMenu.add_cascade(label="Herramientas", menu=archivoTools)

#-----------------------------
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#-----------------------------
root.mainloop()