print("Asignaturas optativas año 2023")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

	print("Asignatura elegida " + asignatura)

else:

	print("La asignatura escogida no esta contemplada")