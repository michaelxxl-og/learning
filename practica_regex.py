import re

lista_nombres=['Carmen Angulo',
				'Gilbert Martinez',
				'Tiago Anuel',
				'Mike Angulo',
				'Tiago Manuel',
				'Tiago Quero']

for elemento in lista_nombres:

	if re.findall('Angulo$', elemento):

		print(elemento)

#Caracter "^": para ver los elementos de arriba, que comienzan por el elemento a buscar
#Caracter "$": para buscar el ultimo elemento en la lista
#Caracter "[]": para buscar caracteres ejemeplo "ñ" dentro de la lista
'''para buscar palabras iguales pero con diferentes ascentos o generos tipo
niñas o niños; buscar asi "niñ[ao]s", o bien sea camion y camión: "cami[oó]n"'''

'''podemos buscar letras entre los nombres como los que se encuentran arriba si 
quisieramos buscar las letras "ñ" o "z", no se encontraran, pero si buscamos de 
esta manera '^[a-i-m]' si encontrarian (hay que señalar si en tal caso son mayusculas
y minisculas)'''

