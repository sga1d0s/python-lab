print("\n\n-------------KATA1-------------")
print("-------------------------------\n")

agenda = {
    "ana": {"tel": 600111222, "email": "ana@empresa.com"},
    "luis": {"tel": 600333444, "email": "luis@empresa.com"},
    "marta": {"tel": 600555666, "email": "marta@empresa.com"},
}

# Pregunta por el nombre y normaliza sin espacios y en minusculas
nombre = input("Nombre del contacto?: ").strip().lower()

print(f"Buscando {nombre}...\n")

contacto = agenda.get(nombre)

if contacto is None:
    print(f"El contacto {nombre} no se encuentra en la agenda.")
    respuesta = input("Si quieres añadirlo a la agenda pulsa 'Y' \n").strip().lower()
    if respuesta == "y":
        telefono = input("Indica el teléfono: \n")
        email = input("Indica el e-mail: \n")

        # Anadir datos a contacto
        contacto = {"tel": telefono, "email": email}
        # Añdir datos de contacto a nombre
        agenda[nombre] = contacto

    else:
        print("Saliendo de agenda")

if contacto is not None:
    print(
        f"\nNombre = {nombre}\n"
        f"Teléfono = {contacto['tel']}\n"
        f"E-mail = {contacto['email']}"
    )
