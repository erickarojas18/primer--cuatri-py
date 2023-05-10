
primer_tupla=("MARIA",11,6,1973)


print(primer_tupla)

#imprimir tupla por posicion

primer_tupla=("MARIA",11,6,1973)

print(primer_tupla[2])

#valor in

print("MARIA"in primer_tupla)

print("pedro" in primer_tupla)

#cuantas veces se repite dentro de uan tupla

print(primer_tupla.count(6))

#convertir lista a tupla
listanueva=["MARIA",11,6,1973]
tuplanueva=tuple(listanueva)
print(tuplanueva.count(11))

#valor len devuelve la cantidad de elementos en una tupla
len(primer_tupla)
print((len(primer_tupla)))

#desempaquetar la tupla
listanueva=["MARIA",11,6,1973]
tuplanueva=tuple(listanueva)
nombre,dia,mes,año=tuplanueva
print(nombre)
print(dia)
print(mes)
print(año)

#convertir tupla en lista (list)
listanueva=["MARIA",11,6,1973]
nuevalista=list(primer_tupla)
print(nuevalista)
print(tuplanueva)


#convetir lista a tupla(tuple)
listanueva=["MARIA",11,6,1973]
nuevalista=tuple(primer_tupla)
print(tuplanueva)
print(listanueva)

