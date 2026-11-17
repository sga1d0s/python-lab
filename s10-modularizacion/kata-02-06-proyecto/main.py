print("\n\n---------KATA2 a KATA6---------")
print("-------------------------------\n")

from pathlib import Path

from alertas import clasifica_alerta
from formato import formatea_bytes
from logs import cuenta_fallos_por_ip, cuenta_por_tipo
from validaciones import valida_ip

lineas = Path("datos/auth.log").read_text().splitlines()

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

    print("\n--- Resumen ---")
    for estado, cantidad in contador_estados.items():
        print(f"{estado}: {cantidad}")

if __name__ == "__main__":
    genera_informe(servidores)
    cuenta_por_tipo(lineas)
    
    for ip, cantidad in list(cuenta_fallos_por_ip(lineas).items())[:5]:
        print(f"{ip}: {cantidad}")