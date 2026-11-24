from pathlib import Path


def explora(carpeta: Path) -> None:
    """Muestra el nombre, stem, extensión y tamaño de los ficheros de una carpeta."""
    # Crear un Path no comprueba si existe: lo comprobamos antes de recorrerlo.
    if not carpeta.exists():
        print(f"La carpeta no existe: {carpeta}")
        return

    # Una ruta existente también podría apuntar a un fichero.
    if not carpeta.is_dir():
        print(f"La ruta no es una carpeta: {carpeta}")
        return

    # iterdir() recorre los elementos directamente dentro de la carpeta.
    for ruta in carpeta.iterdir():
        # Ignoramos las subcarpetas y mostramos solo los ficheros.
        if ruta.is_file():
            # stat() devuelve metadatos; st_size indica el tamaño en bytes.
            tamano = ruta.stat().st_size
            print(
                f"{ruta.name:<28} stem={ruta.stem:<16} "
                f"suffix={ruta.suffix:<6} {tamano} bytes"
            )


if __name__ == "__main__":
    # Partimos de la ubicación del script para no depender de dónde se ejecuta.
    carpeta_script = Path(__file__).resolve().parent
    # El operador / une las partes de la ruta de forma portable.
    explora(carpeta_script / "datos")
