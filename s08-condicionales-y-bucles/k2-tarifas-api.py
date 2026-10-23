print("\n\n-------------KATA2-------------")
print("-------------------------------\n")

""" Un proveedor cobra el uso de su API según el volumen de peticiones del mes, con
un precio por petición que depende del tramo en el que caiga el total:

Peticiones/mes          Precio por petición
Hasta 1.000             Gratis (0 €)
De 1.001 a 10.000       0.01 €
De 10.001 a 100.000     0.007 €
Más de 100.000          0.004 €

Cada mes se factura por separado, y todas sus peticiones se cobran al precio del
tramo en que cae su total. Tenéis las peticiones de los doce meses del año en una
lista:

Imprimid una línea por mes con su coste y, al final, el total del año. """

peticiones = [
    800,
    1000,
    2500,
    9800,
    10000,
    18000,
    42000,
    36000,
    100000,
    120000,
    150000,
    95000,
]

total = 0

for mes, peticion in enumerate(peticiones, start=1):
    if peticion > 100000:
        precio = 0.004
    elif peticion > 10000:
        precio = 0.007
    elif peticion > 1000:
        precio = 0.01
    else:
        precio = 0

    coste = peticion * precio
    total += coste
    print(f"Mes {mes}: Peticiones {peticion}, {coste:.2f} €")

print(f"Total del año: {total:.2f} €")