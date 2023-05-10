def llenar_lista(c):
    lista1=[]
    lista2=[]
    for i in range(c):
        num1 = int(input("Digite un numero para la lista 1: "))
        lista1.append(num1)
        num2= int(input("Digite un numero para la lista 2: "))
        lista2.append(num2)
    return lista1,lista2

def suma_listas(l1,l2,c):
    posicion =0
    sumalistas=[]
    for i in range(c):
     suma = l1[posicion] + l2[posicion]
     sumalistas.append(suma)
     posicion=posicion+1
    return sumalistas



print("Se creara sus listas")
c=int(input("Digite la cantidad de elementos de su lista "))
lista1, lista2 = llenar_lista(c)
print(lista1)
print(lista2)

print("Se va mostras la suma de las listas segun sea su posicion")
nuevalista= suma_listas(lista1,lista2,c)
print(nuevalista)