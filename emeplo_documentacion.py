from modulos import funciones_matematicas

class Areas:
	
	'''Esta clase calcula las areas de diferentes figuras geometricas'''

	def areaCuadrado(lado):

		'''Calcula el area de un cuadrado
		elevando al cuadrado el lado pasado 
		por parametro'''

		return "El area del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):

		'''Calcula el area de un triangulo'''

		return "El area del triangulo es: " + str((base*altura)/2)

help(funciones_matematicas)