#Calcular el numero de pulsaciones
print("Selecione un sexo")
print("1=femenino")
print("2 masculino")

sexo = int(input("Opcion: "))
if sexo <= 0 or sexo >=3:
   print("Seleccione una opcion correcta")
elif sexo == 1:
    edad = int(input("Digite su edad: "))
    pulsaciones = (220-edad)/10
    print(f'Las pulsaciones por 10 seg que usted debe poseer es de {pulsaciones}')
elif sexo == 2:
    edad = int(input("Digite su edad: "))
    pulsaciones = (210-edad)/10
    print(f'Las pulsaciones por 10 seg que usted debe poseer es de {pulsaciones}')