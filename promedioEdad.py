#Calcular el promedio de edad N estudiantes
#Utilizando el ciclo Mientras

n=int(input("Digite la cantidad de estudiantes"))
c=1;
suma=0;
print("Digite la edad de sus alumnos")
while (c<=n):
    print("Alumno ",c)
    edad=int(input())
    suma=suma+edad
    c=c+1
prom=suma/n
print("Se sumaron ",n,"edades y el promedio es",prom)