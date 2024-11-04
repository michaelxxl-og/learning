import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE Productos (Nombre_Articulo VARCHAR(50), Precio INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO Productos VALUES('Balon', 15, 'Deportes')")

miCursor.execute("SELECT * FROM Productos")

variosProductos=miCursor.fetchall()


for producto in variosProductos:
	
	print("Nombre Articulo: ", producto[0], "Seccion: ", producto [2]) 

miConexion.commit()

miConexion.close()