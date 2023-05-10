

def EsBisiesto(año):
    return (año % 4 == 0 and not (año % 100 == 0)) or año % 400 == 0


def DiasDelMes(mes, año):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if EsBisiesto(año):
            return 29
        else:
            return 28


def Calcular_Dia_Juliano(dia, mes , año):
    diaj = 0
    for mes in range(1, mes):
        dia = dia + DiasDelMes(mes, año)
    diaj = diaj + dia
    return diaj


def LeerFecha():
    dia = int(input("Día:"))
    mes = int(input("Mes:"))
    año = int(input("Año:"))
    return dia, mes, año
#funcion_principal

dia, mes, año = LeerFecha()
print("Día Juliano: ", Calcular_Dia_Juliano(dia, mes, año))