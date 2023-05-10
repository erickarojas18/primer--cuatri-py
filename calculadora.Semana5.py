
# Fun pidecantidad
def pidecantidad():
    cantidad_numeros=int(input("Digite la cantidad de numeros a calcular: "))
    return (cantidad_numeros)


# Fun pidevalor
def pidevalor():
    n1 =int(input("Digite el primer numero: "))
    n2 = int(input("Digite el segundo numero"))
    return (n1, n2);


# Fun Suma
def sum():
    contador = 0
    cantidad_numeros = int(input(" Cuantos numeros desea sumar: "))
    total = 0
    while (contador < cantidad_numeros):
        numero = int(input("Digite un numero: "))
        total = total + numero
        contador = contador + 1
    return (total)

# Fun Multiplicacion
def multp(cantidad_numeros):
    contador = 0
    #cantidad_numeros = int(input(" Cunatos numeros desea sumar: "))
    total = 1
    while (contador < cantidad_numeros):
        numero = int(input("Digite un numero: "))
        total = total * numero
        contador = contador + 1
    return (total)

# Fun Resta
def rest(n1, n2):
    if (n1 > n2):
        print("La resta dara un resultado negativo, desea continuar?: ")
        op = int(input("Si = 1, No = Cualquier numero: "))
        if (op == 1):
            r = n1 - n2
            return (r)
        else:
            print("Has salido de la resta")
    else:
        r = n1 - n2
        return (r)


# Fun Division
def div(n1, n2):
    if (n1 == 0 | n2 == 0):
        print("No se puede realizar la operacion")
    else:
        r = n1 / n2
    return (r)


# Funcion principal
print("CALCULADORA DE ERICKA")
print("1 - Sum")
print("2 - Rest")
print("3 - Multp")
print("4 - Div")
op = int(input("Seleccione una opcion: "))
if (op == 1):
    pidecantidad()
    valor= sum()
    print("El resultado es:",valor)
elif op==2:
    a,b =pidevalor()
    total_resta=rest(a,b)
    print("El resultado es",total_resta)
elif (op == 3):
    n=pidecantidad()
    resultado_multp= multp(n)
    print("El resultado es:",resultado_multp)

elif (op == 4):
    a,b=pidevalor()
    resultado_Div = div(a,b)
    print("El resultado es:",resultado_Div)