def valida_ip(ip):
    """Lanza ValueError si la IPv4 no es válida."""
    partes = ip.split(".")

    if len(partes) != 4:
        raise ValueError(f"tiene {len(partes)} partes en vez de 4")

    for parte in partes:
        if not parte.isdigit():
            raise ValueError(f"{parte!r} no es un número")

        numero = int(parte)
        if not 0 <= numero <= 255:
            raise ValueError(f"{numero} se sale de 0-255")
    # No hace falta return: una IP válida termina sin lanzar nada.