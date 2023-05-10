#Calcular el promedio de edad N de estudiantes
#Utilizando ciclo For
n=int(input("Digite la cantidad de estudiantes"))
c=1;
suma=0;
print("Digite la edad de alumnos")
for i in range(1n+1):
    print("Alumno", i)
    edad=int(input())
    suma=suma+edad
prom=suma/n
print("Se sumaron",n,"edades y el promedio es",prom)