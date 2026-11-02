def valida_ip(ip):
    """Comprueba que una IP tiene 4 partes numéricas entre 0 y 255."""
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False
    return True


def clasifica_alerta(cpu, ram, disco):
    """Clasifica el estado de un servidor según su CPU, RAM y disco (%)."""
    if cpu >= 90 or ram >= 90 or disco >= 90:
        return "CRITICAL"
    elif cpu >= 75 or ram >= 75 or disco >= 75:
        return "WARNING"
    else:
        return "OK"


def formatea_bytes(n):
    """Convierte un número de bytes en una cadena legible (KB, MB, GB,
    TB)."""
    unidades = ["B", "KB", "MB", "GB", "TB"]
    tamano = float(n)
    indice = 0
    while tamano >= 1024 and indice < len(unidades) - 1:
        tamano = tamano / 1024
        indice = indice + 1
    return f"{tamano:.2f} {unidades[indice]}"


servidores = [
    {
        "nombre": "srv-web01",
        "ip": "10.0.0.5",
        "cpu": 40,
        "ram": 55,
        "disco": 35,
        "espacio_usado": 3_500_000_000,
    },
    {
        "nombre": "srv-db01",
        "ip": "10.0.0.300",
        "cpu": 92,
        "ram": 60,
        "disco": 70,
        "espacio_usado": 900_000_000_000,
    },
    {
        "nombre": "srv-bck01",
        "ip": "10.0.0.8",
        "cpu": 78,
        "ram": 40,
        "disco": 50,
        "espacio_usado": 15_000_000,
    },
]
contador_estados = {"OK": 0, "WARNING": 0, "CRITICAL": 0}

for servidor in servidores:
    ip_valida = valida_ip(servidor["ip"])
    estado = clasifica_alerta(servidor["cpu"], servidor["ram"], servidor["disco"])
    espacio = formatea_bytes(servidor["espacio_usado"])
    contador_estados[estado] = contador_estados[estado] + 1

    if ip_valida:
        etiqueta_ip = "válida"
    else:
        etiqueta_ip = "INVÁLIDA"

    print(
        f"{servidor['nombre']} ({servidor['ip']}, {etiqueta_ip}): estado={estado}, espacio_usado={espacio}"
    )

print()
print("--- Resumen ---")

for estado in contador_estados:
    print(f"{estado}: {contador_estados[estado]}")
