edad=input("Introduce tu edad: ")

while(edad.isdigit()==False):

	print("Por favor introduce un valor numerico")

	edad=input("Introduce la edad: ")


if (int(edad)<18):

	print("No puede pasar")

else:

	print("Puedes pasar")