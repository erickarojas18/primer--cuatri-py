#Leer numero

resp="Si"
while resp=="Si" or resp== "si":
    num1=int(input("Digite un numero: "))
    if num1==0 or num1<= 10 :
        print(num1)
    else:
        print("Error")
        print("Debe digitar un numero entre 0 y 10.")
        print("Escribir Si o No")
        resp=input()