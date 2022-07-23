# Dada la tupla tupla1, realizar las siguientes tareas

tupla1 = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

# Obtener el ultimo elemento
print(tupla1[-1])

# Obtener la longitud de la tupla
print(len(tupla1))

# Obtener la posicion del numero 87
print(tupla1.index(87))

# Crear una lista con los ultimos 3 elementos de la tupla
lista = list(tupla1[-3:])
print( lista )

# Obtener el elemento que se encuentra en la posicion 8
print( tupla1[8] )

# Obtener el numero de veces que se repite el numero 7
print( tupla1.count(7) )