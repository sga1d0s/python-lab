print("\n\n-------------KATA0-------------")
print("-------------------------------\n")

with open("servidores.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.read().splitlines()

servidores = {}

for linea in lineas:
    # Asigna cada salto del split a una variable
    servidor, cpu, ram = linea.split(";")

    # Inserta servidor como clave del diccionario anidado
    servidores[servidor] = {
        "cpu": float(cpu),
        "ram": float(ram),
    }

print("Informe de estado de servidores")
print("-" * 31)
print(f"{'Servidor':<12} {'CPU':>7} {'RAM':>7}")

for servidor, datos in servidores.items():
    cpu = f"{datos['cpu']:.1f}"
    ram = f"{datos['ram']:.1f}"
    print(f"{'Servidor':<12} {cpu:>7} {ram:>7}")
