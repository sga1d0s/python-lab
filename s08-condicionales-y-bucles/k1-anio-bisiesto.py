print("\n\n-------------KATA1-------------")
print("-------------------------------\n")

""" Un año es bisiesto si es divisible entre 4, salvo que sea divisible entre 100 —en ese
caso solo es bisiesto si además es divisible entre 400—. Escribe un script que pida
un año por teclado y diga si es bisiesto o no. """

anio = int(input("Introduce un año: "))

if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
