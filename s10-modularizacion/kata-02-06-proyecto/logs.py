def cuenta_por_tipo(lineas):
    """Cuenta la cantidad de líneas de log por tipo."""
    conteos = {
        "Failed password": 0,
        "Accepted": 0,
        "Invalid user": 0,
        "Otras": 0,
    }

    for linea in lineas:
        tipo = clasifica_linea(linea)
        conteos[tipo] += 1

    print("\n--- auth.log ---")

    for tipo, cantidad in conteos.items():
        print(f"{tipo}: {cantidad}")
        
    print(f"Total: {len(lineas)}")


def clasifica_linea(linea):
    """Devuelve el tipo de una línea de log."""
    linea = linea.lower()
    if "failed password" in linea:
        return "Failed password"
    elif "accepted" in linea:
        return "Accepted"
    elif "invalid user" in linea:
        return "Invalid user"
    return "Otras"

if __name__ == "__main__":
    clasifica_linea("Jun 14 00:15:50 srv-web01 sshd[5585]: Accepted publickey for deploy from 192.168.1.20 port 47001 ssh2")