print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		calificaciion=7
	return valoracion

print(evaluacion(int(nota_alumno)))