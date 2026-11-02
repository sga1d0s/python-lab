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

if __name__ == "__main__":
    print(f"La IP: 10.10.0.1 es: {valida_ip("10.10.0.1")}")