
import math

def pide_catetos():
    a = int(input("Digite el primer cateto: "))
    b = int(input("Digite el segundo cateto: "))
    return(a,b)


def funcion_calcula(a,b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return (hipotenusa)



#funcionprincipal

cateto1, cateto2=pide_catetos()
h=funcion_calcula(cateto1,cateto2)
h=round(h)
print("La Hipotenusa es :",h)

print("¿Desea ver la representacion grafuca del triangulo?")
resp=input("Responda con *S* para continuar o digite *N* para salir ")
if resp=="S" or resp=="s":
    for i in range(h+1):
        print("*" * i)
elif resp=="N" or resp=="n":
    print("Su programa finalizo")











