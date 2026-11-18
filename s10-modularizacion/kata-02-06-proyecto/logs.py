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

    return conteos


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

def ip_de(linea):
    """Devuelve la IP de la línea de log con contraseña fallida."""
    return linea.split("from ")[1].split(" ")[0]

def cuenta_fallos_por_ip(lineas):
    """Cuenta los fallos de contraseña por IP."""
    conteos = {}

    for linea in lineas:
        if "failed password" in linea.lower():
            ip = ip_de(linea)
            conteos[ip] = conteos.get(ip, 0) + 1

    return conteos

if __name__ == "__main__":
    print(f"Tipo: {clasifica_linea('Jun 14 00:15:50 srv-web01 sshd[5585]: Accepted publickey for deploy from 192.168.1.20 port 47001 ssh2')}")
    print(f"IP: {ip_de('Jun 14 00:15:50 srv-web01 sshd[5585]: Failed password for invalid user admin from 192.168.1.20 port 47001 ssh2')}")
    cuenta_fallos_por_ip(['Jun 14 00:15:50 srv-web01 sshd[5585]: Failed password for invalid user admin from 192.168.1.20 port 47001 ssh2'])