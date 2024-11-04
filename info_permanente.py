import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):
		
		listaDePersona=open("FicheroExterno", "ab+")
		listaDePersona.seek(0)

		try:
			self.personas=pickle.load(listaDePersona)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("El fichero esta vacio")

		finally:
			listaDePersona.close()
			del(listaDePersona)

	def agregarPersonas(self, p):
		self.personas.append(p)
		
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def GuardarPersonasEnFicheroExrerno(self):
		listaDePersona=open("FicheroExterno", "wb")
		pickle.dump(self.personas, listaDePersona)
		listaDePersona.close()
		del(listaDePersona)

	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print (p)
		

miLista=ListaPersonas()
persona=Persona("Juan", "Masculino", 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()	

#practicar desiframiento de este codigo





		