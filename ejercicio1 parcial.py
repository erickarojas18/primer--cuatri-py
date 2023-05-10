

def menu():
    print(' ***MENÚ*** ')
    print(' Opcion 1-cuadrado ')
    print(' Opcion 2-rectangulo ')
    print(' Opcion 3- rectangulo  abierto')
    print(' Opcion 4-SALIR ')
    opcion = input(" Digite una opcion entre 1 y 3: ")

    if opcion == '1':
        print(" 1-cuadrado ")
        cuadrado()
    elif opcion == '2':
        print(" 2-rectangulo ")
        rectangulo()
    elif opcion == '3':
        print(' 3-Rectangulo abierto')
        rectangulo_hueco()
    elif opcion == '4':
        print(' **** Saliendo del menu  ****')

def cuadrado():
    lado1 = int(input("Digite el primer número: "))
    lado2 = int(input("Digite el segundo número: "))
    for i in range(0,lado1):
        for j in range(0,lado2):
            print("* ", end="")
        print()
    return menu()
def rectangulo():
    lado1 = int(input("Digite el primer número (a): "))
    lado2 = int(input("Digite el segundo número (b): "))
    for q in range(0, lado2+1):
        for f in range(0, lado1+1):
            print("* ", end="")
        print()
    return menu()
def rectangulo_hueco():
    lado1 = int(input("Digite el primer número (b): "))
    lado2 = int(input("Digite el segundo número (a): "))
    for fila in range(lado1):
        for columna in range(lado2):
            if fila == 0 or fila == lado1 - 1 or columna == 0 or columna == lado2 - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    return menu()
menu()