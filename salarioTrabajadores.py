
def leer():
    dato = int(input("Digite el dato: "))
    return dato


def definir_salario_base(categoria):
    if categoria == 1:
        salario_base = 2300000
        return salario_base
    elif categoria == 2:
        salario_base = 1700000
        return salario_base
    elif categoria == 3:
        salario_base = 650000
        return salario_base
    elif categoria == 4:
        salario_base = 850000
        return salario_base
    elif categoria == 5:
        salario_base = 350000
        return salario_base


def calc_dedicacion_exclusiva(salario_base, categoria):
    if categoria == 1 or categoria == 2 or categoria == 3:
        extra = salario_base * 0.15
        return extra
    else:
        print("No hay extra de dedicacion exclusiva para este puesto")
        extra = 0
        return extra


def calc_anualidades(allos):
    if allos <= 5:
        anualidad = allos * 1200
        return anualidad
    elif allos >= 6:
        calc = allos - 5
        calc2 = calc * 500
        anualidad = calc2 + 6000
        return anualidad


def calc_deducciones(salario_base, dedicacion_exclusiva, anualidad):
    calc_salario = salario_base + dedicacion_exclusiva + anualidad
    calc_ccss = calc_salario * 0.09
    calc_seguro_vida = calc_salario * 0.03
    calc_ahorro = calc_salario * 0.05
    deducciones = calc_ahorro + calc_ccss + calc_seguro_vida
    salario_bruto = calc_salario - deducciones
    calc_hacienda = 0
    if salario_bruto > 1500000:
        calc_hacienda = salario_bruto * 0.03
        salario_bruto = salario_bruto - calc_hacienda
    return calc_ccss, calc_seguro_vida, calc_ahorro, calc_hacienda, salario_bruto



# def principal
def menu():
    print("\nSistema Calculadora Salarial\n")
    print("Primero seleccione su puesto en la empresa")
    print("1	Gerente	                2.300.000")
    print("2	Director Área	        1.700.000")
    print("3	Contadores	        650.000")
    print("4	Auditoria	        850.000")
    print("5	Asistente Admin 	350.000\n")
menu()
categoria = leer()
salario_base = definir_salario_base(categoria)
dedicacion_exclusiva = calc_dedicacion_exclusiva(salario_base, categoria)
print("\nDigite la cantidad de años trabajados")
allos = leer()
anualidad = calc_anualidades(allos)
calc_deducciones(salario_base, dedicacion_exclusiva, anualidad)
ccss, seguro_vida, ahorro, hacienda, salario_bruto = calc_deducciones(
    salario_base, dedicacion_exclusiva, anualidad)
print("\nBoucher de salario\n")
print(f'Categoria = {categoria}')
print(f'Salario base = {salario_base}')
print(f'Dedicacion exclusiva = {dedicacion_exclusiva}')
print(f'Anualidad = {anualidad}\n')
print(f'Rebajo CCSS = {ccss}')
print(f'Seguro de vida = {seguro_vida}')
print(f'Ahorro = {ahorro}')
print(f'Hacienda = {hacienda}')
print(f'Salario_bruto = {salario_bruto}\n')
