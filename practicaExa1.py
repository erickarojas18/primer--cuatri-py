
codigos = ("C01", "C02", "C03", "C04", "C05")
agenda = {}

for codigo in codigos:
    nombre = input(f"Ingrese el nombre del cliente con código {codigo}: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    agenda[codigo] = {"Nombre": nombre, "Email": email, "Teléfono": telefono}

print("Agenda de clientes:")
for codigo, datos in agenda.items():
    print(f"{codigo}: {datos['Nombre']}, {datos['Email']}, {datos['Teléfono']}")
