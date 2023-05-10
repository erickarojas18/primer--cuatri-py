#  secuencia fibonacci

nterms = int(input("cuantos terminos hay? "))

# first two terms
n1, n2 = 0, 1
count = 0

# comprobar si el número de términos es válido
if nterms <= 0:
   print("ingrese un numero")
# si sólo hay un término, devuelve n1
elif nterms == 1:
   print("secuencia fibonacci hasta",nterms,":")
   print(n1)
# generar fibonacci secuencia
else:
   print("secuencia fibonacci:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1