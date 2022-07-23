import sys


def validar_numero(numero):
    if 0 <= numero <= 10:
        return True
    else:
        return False

if len(sys.argv) == 3:

    numero1 = int(sys.argv[1])
    numero2 = int(sys.argv[2])

    if validar_numero(numero1) and validar_numero(numero2):

        if numero1 >= 7 and numero2 >= 7:
            print("Promocionado")
        elif numero1 >= 4 and numero2 >= 4:
            print("Aprobado , debe rendir un final")
        elif numero1 < 4 or numero2 < 4:
            if numero1 < 4:
                print("Desaprobado, debe recuperar el primer parcial")
            else:
                print("Desaprobado, debe recuperar el segundo parcial")
        elif numero1 < 4 and numero2 < 4:
            print("Desaprobo los dos parciales, debe recursar")
else:
    print("Uso del script: desafio.py <valor1> <valor2>")
