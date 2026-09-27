##########################
#----------KATA3---------#
##########################
print("\n\n----------KATA3----------")
print("-------------------------\n")

conexiones = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7",  "10.0.0.5"]

ips_unicas = set(conexiones)

print(f"Total de conexiones: {len(conexiones)}")
print(f"IPs únicas: {ips_unicas}")
print(f"Total de IPs distintas: {len(ips_unicas)}")