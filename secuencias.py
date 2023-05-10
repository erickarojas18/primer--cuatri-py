
letras="Hoy es un dia Maravilloso"
print(letras)

#funcion len()
print(len(letras))

#Funcion str()
num=123
numeros=str(num)
x=1456
print(numeros+str(x))

#funcion upper()
print(letras.upper())

#funcion lower()
print(letras.lower())
#Funcion split()
lista=letras.split(" ")
print(lista)
print (lista[2])

#funcion join

print("-".join(lista))

#funcion strip()
oracion=" Carlos es muy feliz "
print(oracion.strip())

#funcion replace()

oracion2=oracion.replace("feliz", "INFELIZ")
print(oracion2)