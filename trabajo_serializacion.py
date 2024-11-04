import pickle

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()
#esto guarda el archivo 
del (fichero_binario)

#se creara un archivo inilegible en la carpeta donde esta este archivo.py