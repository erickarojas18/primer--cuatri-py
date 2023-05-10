
def crear_lista():
    nombre_Trabajadores = []
    cedula_Trabajadores = []
    return nombre_Trabajadores, cedula_Trabajadores

def llenar_listas(nombre_Trabajadores, cedula_Trabajadores, cantidad):
    contador = 0
    while contador < cantidad:
        nombre = input("Escriba su nombre: ")
        nombre_Trabajadores.append(nombre)

        cedula = int(input("Digite su numero de cedula: "))
        cedula_Trabajadores.append(cedula)
        contador = contador + 1
    return nombre_Trabajadores, cedula_Trabajadores

def leer_listas(nombre_Trabajadores, cedula_Trabajadores, cantidad):
    contador = 0
    while contador < cantidad:
        print(nombre_Trabajadores[contador])
        print(cedula_Trabajadores[contador])
        contador = contador + 1
    return nombre_Trabajadores, cedula_Trabajadores

def mostrar_listas(nombre_Trabajadores, cedula_Trabajadores):
    print(nombre_Trabajadores)
    print(cedula_Trabajadores)

def insertar_datos(nombre_Trabajadores, cedula_Trabajadores):
    posición = int(input("Indique la posición donde va realizar el cambio "))
    nombre = input("Digite el nombre del nuevo empleado ")
    cedula = int(input("Digite la cedula del nuevo empleado "))
    nombre_Trabajadores.insert(posición, nombre)
    cedula_Trabajadores.insert(posición, cedula)
    return nombre_Trabajadores, cedula_Trabajadores

def modificar_listas(nombre_Trabajadores, cedula_Trabajadores):
    valor = input("Digite el nombre o la cedula a modificar: ")
    if valor in nombre_Trabajadores:
        x = nombre_Trabajadores.index(valor)
        nuevo_valor = input("Ingrese el nuevo nombre ")
        nombre_Trabajadores[x] = nuevo_valor
        cedula_Trabajadores[x] = input("Digite la nueva cedula: ")
        print("El valor ha sido modificado con exito ")
    elif valor in cedula_Trabajadores:
        n = cedula_Trabajadores.index(valor)
        nuevo_valor = input("Ingrese la nueva cedula  ")
        cedula_Trabajadores[n] = nuevo_valor
        nombre_Trabajadores[n] = input("Digite le nuevo nombre : ")
        print("El valor ha sido modificado con exito")

def borrar_listas(nombre_Trabajadores, cedula_Trabajadores):
    valor = input("Ingrese el nombre o la cédula a borrar: ")
    if valor in nombre_Trabajadores:
        nam = nombre_Trabajadores.index(valor)
        nombre_Trabajadores.pop(nam)
        cedula_Trabajadores.pop(nam)
        print("El valor ha sido eliminado con exito ")
    elif valor in cedula_Trabajadores:
        c = cedula_Trabajadores.index(valor)
        cedula_Trabajadores.pop(c)
        nombre_Trabajadores.pop(c)
        print("El valor ha sido eliminado con exito ")

def menu():
    nombre_Trabajadores, cedula_Trabajadores = crear_lista()
    while True:
        print("------- MENU -------")
        print("1. Llenar listas")
        print("2. Leer listas")
        print("3. Mostrar listas")
        print("4. Insertar datos")
        print("5. Modificar listas")
        print("6. Borrar listas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cantidad = int(input("Ingrese la cantidad de trabajadores a ingresar: "))
            nombre_Trabajadores, cedula_Trabajadores = llenar_listas(nombre_Trabajadores, cedula_Trabajadores, cantidad)
        elif opcion == "2":
            cantidad = len(nombre_Trabajadores)
            leer_listas(nombre_Trabajadores, cedula_Trabajadores, cantidad)
        elif opcion == "3":
            mostrar_listas(nombre_Trabajadores, cedula_Trabajadores)
        elif opcion == "4":
            nombre_Trabajadores, cedula_Trabajadores = insertar_datos(nombre_Trabajadores, cedula_Trabajadores)
        elif opcion == "5":
            modificar_listas(nombre_Trabajadores, cedula_Trabajadores)
        elif opcion == "6":
            borrar_listas(nombre_Trabajadores, cedula_Trabajadores)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
