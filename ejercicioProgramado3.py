
num = 0
num_mayor = 0
num_menor = 0
contador = 0
while num >= 0:
    num = int(input("Escriba un numero: "))
    if contador == 0:
        num_mayor = num
        num_menor = num
        contador = contador + 1
    elif num >= 0:
        if num > num_mayor:
            num_mayor = num
            contador = contador + 1
        elif num < num_menor:
            num_menor = num
            contador = contador + 1
        else:
            contador = contador + 1
    elif num < 0:
        print("El numero negativo finalizo el programa")
        print(f'Numero mayor = {num_mayor}')
        print(f'Numero menor = {num_menor}')
        print(f'Cantidad de numeros = {contador}')
    