from datetime import datetime
from pathlib import Path


def parsea_fila(linea):
    """Devuelve los campos limpios o lanza ValueError con el motivo."""
    campos = [campo.strip() for campo in linea.split(";")]

    # También considera vacía una línea como ;;;;
    if all(not campo for campo in campos):
        raise ValueError("fila vacía")
    if len(campos) != 5:
        raise ValueError(f"número de columnas incorrecto: {len(campos)}")

    fecha, producto, unidades_texto, precio_texto, comercial = campos

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"fecha no válida: {fecha!r}")

    try:
        unidades = int(unidades_texto)
    except ValueError:
        raise ValueError(f"unidades no numéricas: {unidades_texto!r}")
    if unidades <= 0:
        raise ValueError(f"unidades no positivas: {unidades}")

    if not precio_texto:
        raise ValueError("precio ausente")
    try:
        precio = float(precio_texto.replace(",", "."))
    except ValueError:
        raise ValueError(f"precio no numérico: {precio_texto!r}")

    return {
        "fecha": fecha,
        "producto": producto,
        "unidades": unidades,
        "precio": precio,
        "comercial": comercial,
    }


def main():
    ruta = Path(__file__).resolve().parent / (
        "datos/sucios/ventas_2026_07_sucio.csv"
    )
    lineas = ruta.read_text(encoding="utf-8").splitlines()

    vistas = {}  # Línea original -> número donde apareció por primera vez.
    correctas = 0
    descartadas = 0
    total = 0.0

    for numero, linea in enumerate(lineas[1:], start=2):
        try:
            venta = parsea_fila(linea)
            if linea in vistas:
                raise ValueError(f"repite la fila {vistas[linea]}")
        except ValueError as error:
            descartadas += 1
            print(f"fila {numero} descartada: {error}")
            continue

        vistas[linea] = numero
        correctas += 1
        total += venta["unidades"] * venta["precio"]

    print()
    print(f"Filas correctas: {correctas}")
    print(f"Filas descartadas: {descartadas}")
    print(f"TOTAL VENTAS JULIO: {total:.2f} EUR")


if __name__ == "__main__":
    main()