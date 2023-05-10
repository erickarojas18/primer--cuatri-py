#Definir el monto total a pagar con descuento
monto = int((input("Digite el monto a cancelar: ")))
numero_azar = int(input("Digite un numero al azar: "))

if numero_azar < 50:
    descuento = monto*0.15
    total = monto - descuento
    print("FELICIDADES!")
    print(f'Usted con el numero {numero_azar} obtuvo un descuento del "15%", descontandole {descuento} del precio total, el cual ahora es de {total}')
elif numero_azar >= 50:
    descuento = monto*0.20
    total = monto - descuento
    print("FELICIDADES!")
    print(f'Usted con el numero {numero_azar} obtuvo un descuento del "20%", descontandole {descuento} del precio total, el cual ahora es de {total}')