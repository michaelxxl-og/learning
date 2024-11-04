class Persona():

	def __init__(self, nombre, edad, ubicacion):

		self.nombre=nombre

		self.edad=edad

		self.ubicacion=ubicacion

	def descripcion(self):
		
		print("Nombre:", self.nombre, " Edad", self.edad, " Ubicacion", self.ubicacion)

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, ubicacion_empleado):

		super().__init__(nombre_empleado, edad_empleado, ubicacion_empleado)

		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		
		super().descripcion()

		print(" Salario: " , self.salario, "Antiguedad: ", self.antiguedad)
		

Manuel=Persona("Manuel", 55, "Colombia")

Manuel.descripcion()

print(isinstance(Manuel, Empleado))