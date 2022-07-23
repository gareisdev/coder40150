# Dadas dos listas lista1 y lista2, realizar las siguientes tareas

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]


# Agregar a lista1 los elementos 1234 y "Hola"
lista1.append(1234)
lista1.append("Hola")
print("Lista 1:", lista1)

# Agregar a lista1 los elementos "Adios" y 1234
lista2.append("Adios")
lista2.append(1234)
print("Lista 2:", lista2)

# Crear una lista3 con todos los elementos de lista1 menos el ultimo
lista3 = lista1[:-1]
print("Lista 3:", lista3)

# Crear una lista4 con todos los elementos de lista2 menos el primero y el ultimo
lista4 = lista2[1:-1]
print("Lista 4:", lista4)

# Generar una lista5 con todos los elementos de lista3 y lista4
lista5 = lista4 + lista3
print("Lista 5:", lista5)