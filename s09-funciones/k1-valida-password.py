print("\n\n-------------KATA1-------------")
print("-------------------------------\n")

intento = 0


def validaPassword(pwd) -> bool:
    if len(pwd) < 8:
        return False

    isUpper = False
    idDigit = False
    validate = False

    for caracter in pwd:
        if caracter.isupper():
            isUpper = True
        if caracter.isdigit():
            idDigit = True
        if isUpper and idDigit:
            validate = True

    return validate


while intento <= 4:
    pwd = input("Introduzca su contraseña: ")

    if validaPassword(pwd):
        print("Contraseña guardada correctamente")
        break
    else:
        print("Contraseña incorrecta vuelva a introducir la contraseña")
        intento += 1
