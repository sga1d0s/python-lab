##########################
#----------KATA4---------#
##########################
print("\n\n----------KATA4----------")
print("-------------------------\n")

conexiones = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7",  "10.0.0.5"]
contador = {}

for intento in conexiones:
   contador[intento] = contador.get(intento, 0) +1
print(f"Intentos por IP: {contador}")

for ip, intentos in contador.items():
  if (intentos >= 3):
    print(f"IPs sospechosas (>=3 intentos): {ip}")