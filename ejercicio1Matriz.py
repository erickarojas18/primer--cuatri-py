
from random import randint

def llenaMat(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(randint(0,50))
        matriz.append(fila)
    return matriz

def sumar(matriz):
    suma = 0
    for fila in matriz:
        for num in fila:
            suma += num
    return suma


def Mostrar(matriz):
    print("La matriz es la siguiente")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end="  ")
        print()

def diagonales(matriz):
    diagonal_izquierda = []
    diagonal_derecha = []
    suma_izquierda = 0
    suma_derecha = 0
    for i in range(len(matriz)):
        diagonal_izquierda.append(matriz[i][i])
        diagonal_derecha.append(matriz[i][len(matriz)-1-i])
    for elemento in diagonal_izquierda:
        suma_izquierda += elemento
    for elemento in diagonal_derecha:
        suma_derecha += elemento
    print("Diagonal izquierda:", diagonal_izquierda)
    print("Diagonal derecha:", diagonal_derecha)
    return suma_izquierda, suma_derecha

def valor_maximo(matriz):
    valor_maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > valor_maximo:
                valor_maximo = elemento
    return valor_maximo


filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
matriz = llenaMat(filas, columnas)

suma_total = sumar(matriz)
print("La sumatoria de todos los valores de la matriz es:", suma_total)


print(matriz)

Mostrar(matriz)

suma_izquierda, suma_derecha = diagonales(matriz)
print("La sumatoria de la diagonal izquierda es:", suma_izquierda)
print("La sumatoria de la diagonal derecha es:", suma_derecha)


valor_maximo = valor_maximo(matriz)
print("El valor máximo de la matriz es:", valor_maximo)
