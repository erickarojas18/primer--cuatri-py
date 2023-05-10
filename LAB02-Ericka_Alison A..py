codigos = ["COD001", "COD002", "COD003", "COD004", "COD005", "COD007", "COD008", "COD009"]
articulo = ["Arroz", "Frijoles", "Azúcar", "Cafe", "Sal", "Masa", "Harina", "Aceite"]
precio = [5000, 1900, 1500, 3500, 500, 1500, 700, 3000]
cantidad = [200, 0, 300, 100, 60, 20, 0, 3]
facturas = []


def buscar_articulo(cod):
    if cod in codigos:
        enc = True
        idx = codigos.index(cod)
    else:
        enc = False
        idx = -1
    return idx


def agregar_articulo():
    codigo = input("Ingrese el código del artículo: ")
    if buscar_articulo(codigo) != -1:
        print("El artículo ya existe en el inventario")
    else:
        nombre = input("Ingrese el nombre del artículo: ")
        cant = int(input("Ingrese la cantidad del artículo: "))
        precio_art = float(input("Ingrese el precio del artículo: "))
        codigos.append(codigo)
        articulo.append(nombre)
        precio.append(precio_art)
        cantidad.append(cant)


def modificar_articulo():
    codigo = input("Ingrese el código del artículo: ")
    pos = buscar_articulo(codigo)
    if pos != -1:
        nombre = input("Ingrese el nuevo nombre del artículo: ")
        cant = int(input("Ingrese la nueva cantidad del artículo: "))
        precio_art = float(input("Ingrese el nuevo precio del artículo: "))
        articulo[pos] = nombre
        precio[pos] = precio_art
        cantidad[pos] = cant
        print("El artículo ha sido modificado exitosamente")
    else:
        print("El artículo no existe en el inventario")


def eliminar_articulo():
    codigo = input("Ingrese el código del artículo: ")
    pos = buscar_articulo(codigo)
    if pos != -1:
        resp = input("¿Está seguro de que desea borrar este artículo? (S/N)")
        if resp.upper() == "S":
            codigos.pop(pos)
            articulo.pop(pos)
            precio.pop(pos)
            cantidad.pop(pos)
            print("El artículo ha sido eliminado exitosamente")
        else:
            print("Se ha cancelado la transacción")
    else:
        print("El artículo no existe en el inventario")


def mostrar_inventario(codigos,articulo,cantidad,precio):
    print("Inventario:")
    print("Código \tNombre \tCantidad \tPrecio")
    for i in range(len(codigos)):
        print(codigos[i], "\t", articulo[i], "\t", cantidad[i], "\t", precio[i])


def venta():
    mostrar_inventario(codigos,articulo,precio,cantidad)
    total_pagar = 0
    articulos_comprar = []
    cantidades_comprar = []
    precios_comprar = []
    while True:
        codigo = input("Ingrese el código del artículo que desea comprar (0 para terminar): ")
        if codigo == "0":
            break
        pos = buscar_articulo(codigo)
        if pos != -1:
            cant = int(input("Ingrese la cantidad que desea comprar: "))
            if cant > cantidad[pos]:
                print("No hay suficiente cantidad de este artículo en inventario")
            else:
                total_pagar += cant * precio[pos] * 0.13
                articulos_comprar.append(articulo[pos])
                cantidades_comprar.append(cant)
                precios_comprar.append(precio[pos])
                cantidad[pos] -= cant
        else:
            print("El artículo no existe en el inventario")
    if len(articulos_comprar) > 0:
        for i in range(len(articulos_comprar)):
            print("Total a pagar: " ,total_pagar)
        facturas.append({"articulos": articulos_comprar, "cantidades": cantidades_comprar, "precios": precios_comprar, "total": total_pagar})
    else:
        print("No se han comprado artículos")


def pideDatos(mensaje):
    x = input(mensaje)
    return x


 # Programa principal
codigos = ["COD001", "COD002", "COD003", "COD004", "COD005", "COD007", "COD008", "COD009"]
articulo = ["Arroz", "Frijoles", "Azúcar", "Cafe", "Sal", "Masa", "Harina", "Aceite"]
precio = [5000,1900, 1500, 3500, 500, 1500, 700, 3000]
cantidad = [200, 0, 300, 100, 60, 20, 0, 3]
facturas = []
inventario = []
opc = 0
while opc < 7:
    print("******************************")
    print("1-Inventario ")
    print("2-Modificar")
    print("3-Eliminar")
    print("4-Ventas")
    print("5-Salir")
    print("******************************")
    opc = int(pideDatos("Ingrese una acción a realizar"))
    if opc == 1:
        mostrar_inventario(codigos,articulo,cantidad,precio)
    elif opc == 2:
        modificar_articulo()
    elif opc == 3:
        eliminar_articulo()
    elif opc == 4:
        venta()
    elif opc == 5:
        print("Hasta luego")
