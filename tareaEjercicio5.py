#calcular el salario de 15 trabajadores
#variable
contador=0
totalpagos=0

while contador <15:
   nombre= input("Digite su nombre: ")
   horas=int(input("Digite las horas trabajadas: "))
   valor_hora=int(input("Digite el valor de cada hora trabajada "))

   calculo=horas*valor_hora
   totalpagos=totalpagos + calculo
   contador=contador + 1
   print(f'Persona {nombre} su salario es de {calculo}')

promedio=totalpagos/15
print(f'El promedio de todos los salarios es de {promedio}')
