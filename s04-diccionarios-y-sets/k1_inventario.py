##########################
#----------KATA1---------#
##########################
print("\n\n----------KATA1----------")
print("-------------------------\n")

# Datos de inventario
inventario = {
    "srv-web01": {"ip": "10.0.0.10", "so": "Ubuntu 22.04", "ram_gb": "16 GB"},
    "srv-db01": {"ip": "10.0.0.11", "so": "Debian 12", "ram_gb": "32 GB"},
    "srv-backup": {"ip": "10.0.0.12", "so": "Ubuntu 22.04", "ram_gb": "8 GB"},
}

# Mostrar el inventario completo

print("Inventario completo:")

for hostname, datos in inventario.items():
    print(f"{hostname}: IP {datos['ip']}, SO {datos['so']}, RAM {datos['ram_gb']} GB")

# Consultar un equipo que existe

datos = inventario.get("srv-db01", "equipo no encontrado en el inventario")

print(f"\nDatos de {'srv-db01'}: {datos}")

# Consultar un equipo que no existe

datos = inventario.get("srv-ftp01", "equipo no encontrado en el inventario")

print(f"Datos de {'srv-ftp01'}: {datos}")