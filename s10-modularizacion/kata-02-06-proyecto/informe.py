def texto_informe(contador_estados, por_tipo, top_ips):
    """Devuelve el informe completo como un único texto."""
    texto = "=== Informe del parque ===\n"

    texto += "\nServidores por estado:\n"
    for estado, cuantos in contador_estados.items():
        texto += f"  {estado}: {cuantos}\n"

    texto += "\nLíneas del log por tipo:\n"
    for tipo, cuantos in por_tipo.items():
        texto += f"  {tipo}: {cuantos}\n"

    texto += "\nTop 5 de IPs con más Failed password:\n"
    for ip, cuantos in top_ips:
        texto += f"  {ip}: {cuantos}\n"

    return texto