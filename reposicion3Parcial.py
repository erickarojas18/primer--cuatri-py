

def tiempo_segundos():
    h=int(input("Digite las horas: "))
    m = int(input("Digite los minutos: "))
    s=int(input("Digite los segundos: "))
    horas= h *3600
    minutos= m * 60
    segundos = s * 1
    return horas + minutos + segundos

def horas_segundos():
    seg=int(input("Digite la cantidad de segundos"))
    horas=seg// 3600
    sobrante1= seg % 3600
    minutos= sobrante1 // 60
    sobrante2= sobrante1 % 60
    segundos= sobrante2
    return horas,minutos,segundos


#programaPrincipal
print("***MENU***")
print("1 Convertir a segundos")
print("2 convertir a horas,minutos,segundos")
resp=int(input("Eliga una opción: "))

if  resp== 1 :
    n= tiempo_segundos()
    print(n)
else:
    h, m , s = horas_segundos()
    print("Las hoars son: ",h)
    print("Los minutos son: ",m)
    print("Los segundos son",s)