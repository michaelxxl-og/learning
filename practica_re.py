import re

nombre1="Carmen Angulo"

nombre2="Michael Quero"

nombre3="carmen angulo"

if re.search("Angulo", nombre2, re.IGNORECASE):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado")

'''PATRON "re.IGNORECASE", ignora si esta en mayusculas o minisculas'''

#re.match acepta tres argumentos, el ultimo puede ser el caso de arriba, si no comparamos dos y ya
