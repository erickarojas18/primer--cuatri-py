#SECUENCIA---ESTRUCTURA DE LISTAS

lista=[1,2,30,3,5,"Ana"]
print(lista)
print(lista[4])
print(lista[2:4])
print(lista[-1])

for i in range(0,4):
    print("VALOR :",lista[i],end='')

#crear listas

listaNombre=[]
#funcion append()
print(" ")
print(listaNombre)
listaNombre.append("Maria")
print(listaNombre)
listaNombre.append("pedro")
print(listaNombre)

#funcion insert()---inserta valores por posicion
listaNombre.insert(1,"vera")
print(listaNombre)
listaNombre.insert(2,"juan")
print(listaNombre)

#funcion extend()

listaNombre.extend(["Sofia","Marcos","Miguel"])
print(listaNombre)

#fincion index()

x=listaNombre.index("Sofia")
print("Sofia se encuentra en la posicion",x,"de la lista")

#funcion in()

print("Esta el nombre Ana en la lista?","Ana" in listaNombre)

#funcion remuve()
listaNombre.remove("juan")
print(listaNombre)


#funcion pop()
listaNombre.pop()
print(listaNombre)