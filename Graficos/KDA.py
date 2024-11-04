
KDA = str()

Kills = "K"
Deaths = "D"
Assist = "A"

K = input(
	"El numero de Muertes:")
D = input("El numero de Eliminaciones:")
A = input("El numero de Asistencias:")


KDA = int(K) - int(D) + int(A)


print("Tu KDA es:", KDA // 3)