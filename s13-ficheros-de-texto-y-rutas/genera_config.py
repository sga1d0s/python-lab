from pathlib import Path

# Las claves entre llaves se sustituyen por los datos de cada host.
PLANTILLA = """# Configuración generada automáticamente
host: {nombre}
ip: {ip}
entorno: {entorno}
"""

HOSTS = [
    {"nombre": "srv-web01", "ip": "192.168.1.10", "entorno": "produccion"},
    {"nombre": "srv-web02", "ip": "192.168.1.11", "entorno": "produccion"},
    {"nombre": "srv-db01", "ip": "192.168.1.20", "entorno": "produccion"},
    {"nombre": "srv-test01", "ip": "192.168.1.90", "entorno": "pruebas"},
]


def genera_config(carpeta: Path) -> None:
    """Genera un fichero de configuración por cada host de HOSTS."""
    # Si la carpeta ya existe, exist_ok=True permite volver a ejecutar el script.
    carpeta.mkdir(exist_ok=True)

    for host in HOSTS:
        # ** descompone el diccionario en argumentos con nombre para format().
        contenido = PLANTILLA.format(**host)
        ruta = carpeta / f"{host['nombre']}.conf"
        # write_text crea el fichero o sobrescribe su contenido si ya existía.
        ruta.write_text(contenido, encoding="utf-8")
        print(f"Generado {carpeta.name}/{ruta.name}")


if __name__ == "__main__":
    # La salida se guarda junto al script, independientemente del directorio actual.
    carpeta_script = Path(__file__).resolve().parent
    genera_config(carpeta_script / "configs_generadas")
