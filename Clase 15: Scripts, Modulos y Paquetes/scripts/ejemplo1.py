import sys


print( sys.argv ) # argument value

if len(sys.argv) == 3:
    print(f"Estas ejecutando: {sys.argv[0]}")
    cadena = sys.argv[1]
    cantidad_repeticion = int(sys.argv[2])
    print( cadena * cantidad_repeticion)
else:
    print("Cantidad de argumentos invalidos")