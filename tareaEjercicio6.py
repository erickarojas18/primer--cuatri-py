
c=int(input("Digite una cifra"))
ci=0

while c!=0:
    x=c % 10
    ci=(ci*10)+x
    c= c//10
print("El numero invertido es",ci)