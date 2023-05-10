# Datos de los choferes (Cédula, Nombre, Salario por hora)
choferes = {
    "11111111": ["Juan Perez", 10],
    "22222222": ["Pedro Gomez", 12],
    "33333333": ["Maria Rodriguez", 11],
    "44444444": ["Luisa Garcia", 9],
    "55555555": ["Carlos Sanchez", 10.5]
}

# Horas trabajadas por cada chofer en la semana (lunes a viernes)
horas_trabajadas = {
    "11111111": [8, 8, 8, 8, 8],
    "22222222": [7, 8, 6, 7, 8],
    "33333333": [8, 8, 8, 8, 7],
    "44444444": [8, 8, 7, 6, 8],
    "55555555": [7, 7, 7, 7, 8]
}

# Calculo de horas trabajadas y salario semanal para cada chofer
salario_semanal = {}
total_horas = 0
nombre_max_horas = ""
horas_max = 0
for cedula, datos in choferes.items():
    nombre = datos[0]
    salario_hora = datos[1]
    horas = sum(horas_trabajadas[cedula])
    salario = salario_hora * horas
    salario_semanal[cedula] = salario
    total_horas += horas
    if horas > horas_max:
        horas_max = horas
        nombre_max_horas = nombre

# Calculo del total por planilla
total_planilla = sum(salario_semanal.values())

# Impresion de los resultados
print("Horas trabajadas y salario semanal por chofer:")
for cedula, salario in salario_semanal.items():
    nombre = choferes[cedula][0]
    horas = sum(horas_trabajadas[cedula])
    print(f"{nombre}: {horas} horas trabajadas, salario semanal de {salario} dólares.")
print(f"Total por planilla: {total_planilla} dólares.")
print(f"El chofer que labora más horas es: {nombre_max_horas}, con {horas_max} horas trabajadas.")
