from io import open

archivo_texto=open("archivo.txt", "r+") #"r+ para escribir informacion; lectura y escritura" 
#archivo_texto=open("archivo.txt", "w") para escribir "write()" para leer "read()" y para añadir "append()"

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()

lista_texto[1]=" Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close
#archivo_texto.seek(len(archivo_texto.readline()))
#readline(para leer desde las lineas del texto determinado)
#archivo_texto.seek(len(archivo_texto.read())/2)
#para leer la mitad del string







