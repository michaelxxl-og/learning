import math

print ("Programa de caluculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumido demasiados intentos. el programa finalizara")
		break;

	numero=int(input("Introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print ("La Raiz cuadrada de " + str(numero) + " es " + str(solucion))