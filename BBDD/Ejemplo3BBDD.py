import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")



miConexion.commit()

miConexion.close()