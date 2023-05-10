
import datetime
import random

# Estructuras de datos
abonados = {}
telefonos = {}
llamadas = []
facturas = []

# Abonado 1
abonado1 = {'cedula': '12345678', 'nombre': 'Juan Perez', 'direccion': 'San Jose, Costa Rica',
            'email': 'juanperez@gmail.com', 'telefono': '11111111', 'estado': 'disponible'}
abonados[abonado1['telefono']] = abonado1
telefonos[abonado1['telefono']] = {"abonado": abonado1['cedula'], "estado": abonado1['estado']}

# Abonado 2
abonado2 = {'cedula': '23456789', 'nombre': 'Maria Garcia', 'direccion': 'Alajuela, Costa Rica',
            'email': 'mariagarcia@gmail.com', 'telefono': '22222222', 'estado': 'ocupado'}
abonados[abonado2['telefono']] = abonado2
telefonos[abonado2['telefono']] = {"abonado": abonado2['cedula'], "estado": abonado2['estado']}

# Abonado 3
abonado3 = {'cedula': '34567890', 'nombre': 'Pedro Ramirez', 'direccion': 'Cartago, Costa Rica',
            'email': 'pedroramirez@gmail.com', 'telefono': '33333333', 'estado': 'disponible'}
abonados[abonado3['telefono']] = abonado3
telefonos[abonado3['telefono']] = {"abonado": abonado3['cedula'], "estado": abonado3['estado']}

# Abonado 4
abonado4 = {'cedula': '45678901', 'nombre': 'Ana Rojas', 'direccion': 'Heredia, Costa Rica',
            'email': 'anarojas@gmail.com', 'telefono': '44444444', 'estado': 'disponible'}
abonados[abonado4['telefono']] = abonado4
telefonos[abonado4['telefono']] = {"abonado": abonado4['cedula'], "estado": abonado4['estado']}

# Abonado 5
abonado5 = {'cedula': '56789012', 'nombre': 'Luis Fernandez', 'direccion': 'San Jose, Costa Rica',
            'email': 'luisfernandez@gmail.com', 'telefono': '55555555', 'estado': 'suspendido'}
abonados[abonado5['telefono']] = abonado5
telefonos[abonado5['telefono']] = {"abonado": abonado5['cedula'], "estado": abonado5['estado']}

# Abonado 6
abonado6 = {'cedula': '67890123', 'nombre': 'Gabriela Hernandez', 'direccion': 'Alajuela, Costa Rica',
            'email': 'gabrielahernandez@gmail.com', 'telefono': '66666666', 'estado': 'suspendido'}
abonados[abonado6['telefono']] = abonado6
telefonos[abonado6['telefono']] = {"abonado": abonado6['cedula'], "estado": abonado6['estado']}

# Abonado 7
abonado7 = {'cedula': '78901234', 'nombre': 'Mario Gomez', 'direccion': 'Cartago, Costa Rica',
            'email': 'mariogomez@gmail.com', 'telefono': '77777777', 'estado': 'disponible'}
abonados[abonado7['telefono']] = abonado7
telefonos[abonado7['telefono']] = {"abonado": abonado7['cedula'], "estado": abonado7['estado']}

# Abonado 8
abonado8 = {'cedula': '89012345', 'nombre': 'Sofia Rodriguez', 'direccion': 'Heredia, Costa Rica',
            'email': 'sofiarodriguez@gmail.com', 'telefono': '88888888', 'estado': 'disponible'}
abonados[abonado8['telefono']] = abonado8
telefonos[abonado8['telefono']] = {"abonado": abonado8['cedula'], "estado": abonado8['estado']}

# Abonado 9
abonado9 = {'cedula': '90123456', 'nombre': 'Jorge Ramirez', 'direccion': 'San Jose', 'email': 'jorgeramirez@gmail.com',
            'telefono': '99999999', 'estado': 'ocupado'}
abonados[abonado9['telefono']] = abonado9
telefonos[abonado9['telefono']] = {"abonado": abonado9['cedula'], "estado": abonado9['estado']}

# Abonado 10
abonado10 = {'cedula': '01234567', 'nombre': 'Alejandro Pacheco', 'direccion': 'Puntarenas',
             'email': 'alejandropacheco@gmail.com', 'telefono': '00000000', 'estado': 'disponible'}
abonados[abonado10['telefono']] = abonado10
telefonos[abonado10['telefono']] = {"abonado": abonado10['cedula'], "estado": abonado10['estado']}


# Registro de abonado
def registrar_abonado():
    cedula = input("Ingrese la cédula del abonado: ")
    cedula = str(cedula)
    nombre = input("Ingrese el nombre completo del abonado: ")
    direccion = input("Ingrese la dirección del abonado: ")
    email = input("Ingrese el correo electrónico del abonado: ")
    telefono = obtener_telefono_libre()
    fecha_pago = datetime.date.today() + datetime.timedelta(days=46)
    estado = 'disponible'
    abonados[cedula] = {"nombre": nombre, "direccion": direccion, "email": email, "telefono": telefono,"fecha_pago": fecha_pago, "estado": estado}
    telefonos[telefono] = {"abonado": cedula, "estado": estado}
    print("\nRegistro exitoso.")
    print("Datos del nuevo abonado:")
    print("Cédula:", cedula)
    print("Nombre:", nombre)
    print("Dirección:", direccion)
    print("Correo electrónico:", email)
    print("Teléfono:", telefono)
    print("Fecha de primer pago:", fecha_pago)


# Obtener número de teléfono libre
def obtener_telefono_libre():
    t = random.randint(10000000, 99999999)
    telefono = str(t)
    return telefono


# Registro de llamadas
def registrar_llamada():
    telefono_origen = input("Ingrese el número de teléfono del abonado que llama: ")
    if telefonos[telefono_origen]["estado"] == "ocupado":
        print("El número de teléfono está ocupado.")
        return
    telefono_destino = input("Ingrese el número de teléfono al que desea llamar: ")
    if telefono_destino not in telefonos:
        print("El número de teléfono no existe.")
        return
    if telefonos[telefono_destino]["estado"] == "suspendido":
        print("El número de teléfono está suspendido por falta de pago.")
        return
    if telefonos[telefono_destino]["estado"] == "disponible":
        telefonos[telefono_origen]["estado"] = "ocupado"
        telefonos[telefono_destino]["estado"] = "ocupado"
        tiempo_inicio = datetime.datetime.now()
        print(f"Llamada en curso entre {telefono_origen} y {telefono_destino}.")
        input("Presione Enter para finalizar la llamada.")
        tiempo_fin = datetime.datetime.now()
        duracion = (tiempo_fin - tiempo_inicio).total_seconds() / 60
        costo = duracion * 20 * 1.13
        llamadas.append({"telefono_origen": telefono_origen, "telefono_destino": telefono_destino, "duracion": duracion,"costo": costo})
        telefonos[telefono_origen]["estado"] = "disponible"
        telefonos[telefono_destino]["estado"] = "disponible"
        print(f"Llamada finalizada. Duración: {duracion:.2f} minutos. Costo: {costo:.2f} colones.")


# Generar facturas
def generar_factura():
    cedula = input("Digite el numero de cedula del abonado: ")
    if cedula not in abonados:
        print("La cédula del abonado no existe.")
        return

    # Obtener información del abonado
    nombre = abonados[cedula]["nombre"]
    direccion = abonados[cedula]["direccion"]
    email = abonados[cedula]["email"]
    telefono = abonados[cedula]["telefono"]
    fecha_pago = abonados[cedula]["fecha_pago"]
    estado = abonados[cedula]["estado"]

    # Calcular fecha límite de pago
    fecha_limite_pago = fecha_pago + datetime.timedelta(days=15)

    # Calcular monto a pagar
    monto_a_pagar = sumar_costos_abonado(cedula)

    # Crear factura
    factura = {
        "cedula": cedula,
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "telefono": telefono,
        "fecha_pago": fecha_pago,
        "fecha_limite_pago": fecha_limite_pago,
        "monto_a_pagar": monto_a_pagar,
        "estado": estado
    }

    # Agregar factura a la lista de facturas
    facturas.append(factura)

    # Imprimir factura
    print("FACTURA")
    print("-----------------------------------------------------")
    print("Cédula:", cedula)
    print("Nombre:", nombre)
    print("Dirección:", direccion)
    print("Correo electrónico:", email)
    print("Teléfono:", telefono)
    print("Fecha de pago:", fecha_pago)
    print("Fecha límite de pago:", fecha_limite_pago)
    print("Monto a pagar:", monto_a_pagar)
    print("Estado:", estado)
    print("-----------------------------------------------------")


def sumar_costos_abonado(cedula):
    costos_totales = 0
    for llamada in llamadas:
        telefono_origen = llamada["telefono_origen"]
        telefono_destino = llamada["telefono_destino"]
        costo = llamada["costo"]
        if abonados[cedula]["telefono"] == telefono_origen:
            costos_totales += costo
        elif abonados[cedula]["telefono"] == telefono_destino:
            costos_totales += costo
    return costos_totales


# Consulta de registro de llamadas
def consultar_registro_llamadas():
    telefono = input("Ingrese el número de teléfono del abonado: ")
    print(f"Registro de llamadas para el número de teléfono {telefono}:")
    for llamada in llamadas:
        if llamada["telefono_origen"] == telefono or llamada["telefono_destino"] == telefono:
            duracion = llamada["duracion"]
            costo = llamada["costo"]
            telefono_destino = llamada["telefono_destino"]
            print(f"Número destino: {telefono_destino}, Duración: {duracion:.2f} minutos, Costo: {costo:.2f} colones")
            consultar_facturas_pagadas(telefono)


def consultar_facturas_pagadas(telefono):
    print(f"Facturas pagadas por el abonado con cédula {telefono}:")
    for factura in facturas:
        if factura["telefono"] == telefono:
            if factura['estado'] != "suspendido":
                fecha = factura["fecha_pago"]
                monto = factura["monto_a_pagar"]
                print(f"Fecha de la factura: {fecha}, Monto pagado: {monto:.2f} colones")


def dar_de_alta_abonado():
    cedula = input("Digite el numero de cedula del abonado: ")
    if cedula in abonados:
        if abonados[cedula]["estado"] == "disponible" or abonados[cedula]["estado"] == "ocupado":
            del abonados[cedula]
            print("El abonado ha sido dado de alta exitosamente.")
        elif abonados[cedula]["estado"] == "suspendido":
            print("El abonado debe una o más facturas. Por favor, cancele todas las facturas pendientes antes de darlo de alta.")
    else:
        print("La cédula del abonado no existe.")


def menu():
    while True:
        print("------- MENU -------")
        print("1. Registrar abonado")
        print("2. Registrar registroadas")
        print("3. Generar facturas")
        print("4. Control de cuentas")
        print("5. Dar de alta a un abonado")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_abonado()

        elif opcion == "2":
            registrar_llamada()

        elif opcion == "3":
            generar_factura()

        elif opcion == "4":
            consultar_registro_llamadas()

        elif opcion == "5":
            dar_de_alta_abonado()

        elif opcion == "6":
            print("¡Hasta luego!")
            with open('datos_abonados.txt', 'w') as f:
                for abonado in abonados.values():
                    f.write(str(abonado) + '\n')
                for telefono in telefonos.values():
                    f.write(str(telefono) + '\n')
                for llamada in llamadas:
                    f.write(str(llamada) + '\n')
                for factura in facturas:
                    f.write(str(factura) + '\n')
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
menu()


