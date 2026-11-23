import sys
from pathlib import Path

from alertas import clasifica_alerta
from formato import formatea_bytes
from informe import texto_informe
from logs import cuenta_fallos_por_ip, cuenta_por_tipo
from validaciones import valida_ip

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


def genera_informe(servidores):
    """Devuelve los contadores y una línea por servidor."""
    contadores = {"OK": 0, "WARNING": 0, "CRITICAL": 0}
    detalles = []

    for servidor in servidores:
        estado = clasifica_alerta(servidor["cpu"], servidor["ram"], servidor["disco"])
        contadores[estado] += 1

        try:
            valida_ip(servidor["ip"])
        except ValueError as error:
            estado_ip = f"INVÁLIDA: {error}"
        else:
            estado_ip = "válida"

        detalles.append(
            f"{servidor['nombre']} ({servidor['ip']}, {estado_ip}): "
            f"estado={estado}, "
            f"espacio_usado={formatea_bytes(servidor['espacio_usado'])}"
        )

    return contadores, detalles


if __name__ == "__main__":
    # Leer primero: si falta el log, aún no hemos impreso nada.
    ruta = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else (Path(__file__).resolve().parent / "datos/auth.log")
    )
    try:
        lineas = ruta.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"error: no existe el fichero {ruta}", file=sys.stderr)
        sys.exit(1)

    estados, detalles = genera_informe(servidores)
    por_tipo = cuenta_por_tipo(lineas)
    fallos = cuenta_fallos_por_ip(lineas)
    top_ips = sorted(fallos.items(), key=lambda par: par[1], reverse=True)[:5]

    texto = "\n".join(detalles) + "\n\n"
    texto += texto_informe(estados, por_tipo, top_ips)

    salida = Path(__file__).resolve().parent / "salida"
    salida.mkdir(exist_ok=True)
    (salida / "informe.txt").write_text(texto, encoding="utf-8")
    print(texto, end="")
