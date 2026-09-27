##########################
#----------KATA2---------#
##########################
print("\n\n----------KATA2----------")
print("-------------------------\n")

# Lista de niveles de log

registros = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO", "DEBUG"]

contador= {}
for nivel in registros:
  contador[nivel] = contador.get(nivel,0) +1

print(f"{contador}\n")
for nivel, veces in contador.items():
  print(f"{nivel}:{veces}")