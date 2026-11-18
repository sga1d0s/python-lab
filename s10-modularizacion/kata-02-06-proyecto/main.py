print("\n\n---------KATA2 a KATA6---------")
print("-------------------------------\n")

from pathlib import Path

from alertas import clasifica_alerta
from informe import texto_informe
from logs import cuenta_fallos_por_ip, cuenta_por_tipo

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


def genera_informe(servidores):
    """Genera un informe de los servidores."""
    for servidor in servidores:
        estado = clasifica_alerta(servidor["cpu"], servidor["ram"], servidor["disco"])
        contador_estados[estado] = contador_estados[estado] + 1


    return contador_estados

if __name__ == "__main__":
    lineas = Path("datos/auth.log").read_text().splitlines()

    estados = genera_informe(servidores)
    por_tipo = cuenta_por_tipo(lineas)
    fallos = cuenta_fallos_por_ip(lineas)
    top_ips = sorted(fallos.items(), key=lambda par: par[1], reverse=True)[:5]

    texto = texto_informe(estados, por_tipo, top_ips)

    Path("salida").mkdir(exist_ok=True)
    Path("salida/informe.txt").write_text(texto, encoding="utf-8")
    print(texto, end="")