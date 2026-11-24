from pathlib import Path


def resumen_log(ruta_log: Path, ruta_resumen: Path) -> None:
    """Cuenta las líneas y los accesos del log y guarda un resumen de texto."""
    lineas_totales = 0
    accesos_aceptados = 0
    intentos_fallidos = 0

    # with cierra el fichero automáticamente al salir del bloque.
    with open(ruta_log, encoding="utf-8") as fichero:
        # Iteramos línea a línea sin cargar el log completo en memoria.
        for linea in fichero:
            lineas_totales += 1
            # Cada contador aumenta si la línea contiene el texto buscado.
            if "Accepted publickey" in linea:
                accesos_aceptados += 1
            if "Failed password" in linea:
                intentos_fallidos += 1

    # Construimos el resumen una vez terminada la lectura del log.
    resumen = (
        f"Resumen de {ruta_log.name}\n"
        f"Líneas totales: {lineas_totales}\n"
        f"Accesos aceptados: {accesos_aceptados}\n"
        f"Intentos fallidos: {intentos_fallidos}\n"
    )
    # write_text crea el resumen o lo sobrescribe en posteriores ejecuciones.
    ruta_resumen.write_text(resumen, encoding="utf-8")
    print(resumen, end="")
    print(f"Resumen guardado en {ruta_resumen.name}")


if __name__ == "__main__":
    # Las rutas parten del script para poder ejecutarlo desde cualquier carpeta.
    carpeta_script = Path(__file__).resolve().parent
    resumen_log(
        carpeta_script / "datos" / "auth.log",
        carpeta_script / "resumen_auth.txt",
    )
