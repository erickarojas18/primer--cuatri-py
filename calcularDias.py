#Hacer un programa que calcule los meses que tienen 30 dias
#Cuales solo 31 dias y si es Febrero determinar si es 29 o 28
mes=input("Indique el mes:")
a=int(input("Indique el año:"))
if(mes=="Enero" or mes=="Marzo" or mes=="Mayo"or mes=="Julio" or mes=="Agosto" or mes=="Octubre" or mes=="Diciembre"):
  dias=31
else:
   if(mes=="Abril"or mes=="Junio" or mes=="Setiembre"or mes=="Noviembre" ):
      dias=30
   else:
       if( a%4==0 ):
        dias=29
        mensaje=" es biciesto. ."
       else:
           dias=28
           mensajes= "no es biciesto"
print("La cantidad de dias que tiene el mes es de ",mes, " es " ,dias ,"dias")
if(mes=="Febrero"):
    print("El año" ,a , mensaje)