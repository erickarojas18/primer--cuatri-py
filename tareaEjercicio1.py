#Definir el total de lo que debe pagar una persona por una llanta
cantidad_llantas=int(input("Dijite el numero de llantas que desea comprar "))

if  cantidad_llantas<=0:
    print("Error, selecione una cantidad correcta")

elif cantidad_llantas>=1 and cantidad_llantas<4:
    total=cantidad_llantas*80000
    print(f'El total a pagar por {cantidad_llantas} es de {total} (cada llanata tiene un precio de 80000')

elif cantidad_llantas>=5:
    total= cantidad_llantas*70000
    print(f'El total a pagar por {cantidad_llantas} es de {total} (cada llanta tiene un precio de 70000')

