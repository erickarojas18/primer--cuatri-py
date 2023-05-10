def mensaje():
    print("Hoy es un buen dia")

def suma():
    n1=int(input("valor 1"))
    n2=int(input("valor 2"))
    s=n1+n2
    print("la suma es de:,",s)


#funciones con parametros y no retorno
def mensaje2(x):
     print(x)

def multi(n1,n2):
    s=n1*n2
    print("imprime en funcion el resultado:,",s)

#funciones con parametros y retornos
def multi2(n1,n2):
    s=n1*n2
    return (s)


#progrma principal
mensaje()
#suma()

men="ESTE ES EL SEGUNDO MENSAJE"
mensaje2(men)

a=9
b=10
multi(a,b)
resultado= multi2(a,b)
c=resultado+10
print("Este es el resultado",resultado,c)
