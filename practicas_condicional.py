salario_presidente=int(input("Introduce salario presidente "))
print("Salarios presidentes: " + str(salario_presidente))

salario_director=int(input("Introduce salario director "))
print("Salarios director: " + str(salario_director))

salario_jefe_de_area=int(input("Introduce salario jefe de area "))
print("Salario Jefe de area: " + str(salario_jefe_de_area))

salario_administrador=int(input("Introduce salario administrador" ))
print("Salarios administrador: " + str(salario_administrador))

if salario_administrador<salario_jefe_de_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en la empresa")