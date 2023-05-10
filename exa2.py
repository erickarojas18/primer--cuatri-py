
def crear_listas():
    nom_hom=[]
    nom_muj=[]
    return nom_hom,nom_muj

def llenar_lista(nom_hom,nom_muj,cantidad ):
    contador = 0
    while contador < cantidad:
        nombre = input("Escriba un nombre de hombre: ")
        nom_hom.append(nombre)

        nombremujer = input("Escriba un nombre de mujer: ")
        nom_muj.append(nombremujer)
        contador = contador + 1
    return nom_hom,nom_muj

def modificar_listas(nom_hom,nom_muj):
    valor = input("Digite la lista que desea  modificar: ")
    if valor in nom_hom:
        x = nom_hom.index(valor)
        nuevo_valor = input("Ingrese el nuevo nombre ")
        nom_hom[x] = nuevo_valor
        print("El nombre ha sido modificado con exito ")
        
    elif valor in nom_muj:
        n = nom_muj.index(valor)
        nuevo_valor = input("Ingrese un nuevo nombre ")
        nom.muj[n] = nuevo_valor
        print("El nombre ha sido modificado con exito")

def mostrar_listas(nom_hom,nom_muj):
    print(nom_hom)
    print(nom_muj)

def guardar_lista():
    print("Los datos han sido guardados con exito")


def menu():
    nom_hom, nom_muj = crear_listas()
    while True:
        print("------- MENU -------")
        print("1. Llenar listas")
        print("2. Modificar listas")
        print("3. Mostar lista ")
        print("4. Guardar lista ")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cantidad = int(input("Ingrese la cantidad de trabajadores a ingresar: "))
            nom_hom, nom_muj = llenar_lista(nom_hom, nom_muj,cantidad)
        elif opcion == "2":
            modificar_listas(nom_hom,nom_muj)
        elif opcion == "3":
            mostrar_listas(nom_hom,nom_muj)
        elif opcion == "4":
            guardar_lista()
        elif opcion=="5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()