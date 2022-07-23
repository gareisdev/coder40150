# Crear lista vacia
lista_vacia = []

# Crear lista con elementos
lista_elementos = [1, 2, 3, 4, "Hola", "Mundo"]

# Operaciones con listas
lista1 = [1, 2, 3]
lista2 = [3, 4, 5, 6]
lista3 = lista1 + lista2

# Acceder a elementos dentro de una lista
heroes_marvel = ["Iron Man", "Spiderman", "She-Hulk"]
print(heroes_marvel[0])

# Slicing de una lista
print( heroes_marvel[0:2] )

# Eliminar elementos de una lista
print("Se ha eliminado el/la heroe/heroina: ", heroes_marvel.pop(1) )
print( heroes_marvel )

# Obtener el indice de un elemento
calificacion = [10, 10, 9, 8, 7, 8, 10, 5]

indice = calificacion.index(11)
print("Donde aparece el 11:", indice)

# Agregar elementos a una lista
