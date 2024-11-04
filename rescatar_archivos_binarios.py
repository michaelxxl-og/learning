import pickle

fichero=open("practicaCalculadora", "r")

practicaCalculadora=pickle.load(fichero)

print(practicaCalculadora)