print("Programa de becas año 2023")
distancia_escuela=int(input("Introduce la distancia en km "))
print(distancia_escuela)

numero_de_hermanos=int(input("Introduce el nº de hermanos en el centro "))
print(numero_de_hermanos)

salario_familar=int(input("Introduce el salario anual bruto "))
print(salario_familar)

if distancia_escuela>40 and numero_de_hermanos>2 or salario_familar<20000:

	print("Tienes derecho a beca")

else:

	print("No tienes derecho a beca")

