
def menu():
    print(' Opcion 1-sacar multiplo ')
    print(' Opcion 2-suma de numeros ')
    print(' Opcion 3- salir')

    opcion = input(" Digite una opcion entre 1 y 3: ")

    if opcion == '1':
        print(" 1-sacar multiplo ")
        multiplo()
    elif opcion == '2':
        print(" 2-sumatoria de cifras: ")
        suma()
    elif opcion == '3':
        print(' **** Saliendo del menu  ****')

def pide_numeros ():
    n=int(input("Digite una cifra"))
    return (n)

def suma_cifras(n):
      suma = 0
      while  n > 0:
        suma = suma + (n % 10)
        n = n // 10
      return suma


resp="1"
while resp!="0":
   n1=pide_numeros()
   total=suma_cifras(n1)
   multiplo= total%9
   print("El resultado de la suma es:",total)
   if multiplo==0:
       print("El numero ingresado *Si* es multiplo de 9")
   else:
       print("El numero que ingresado *No* es multiplo de 9")
       resp=input("Digite 0 para terminar o otro numero para crear otro calculo")

