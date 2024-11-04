correo=input("Introduce tu email: ")

arroba=correo.count("@")

while (correo.startswith("@")==True or correo.endswith("@")==True or arroba!=1):
	print("El correo es incorrecto, comprueba tu @")
	correo=input("Introduce tu email: ")
	arroba=correo.count("@")

print("Tu correo", correo , "es correcto")