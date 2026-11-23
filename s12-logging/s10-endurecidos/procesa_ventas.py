from datetime import datetime
from pathlib import Path


def parsea_fila(linea):
    """Devuelve los campos limpios o lanza ValueError con el motivo."""
    # Separar por punto y coma y quitar espacios de los extremos de cada campo.
    campos = [campo.strip() for campo in linea.split(";")]

    # También considera vacía una línea como ;;;;
    if all(not campo for campo in campos):
        raise ValueError("fila vacía")
    # Comprobar las columnas antes de desempaquetarlas en cinco variables.
    if len(campos) != 5:
        raise ValueError(f"número de columnas incorrecto: {len(campos)}")

    fecha, producto, unidades_texto, precio_texto, comercial = campos

    # Kata 4: comprobar que la fecha existe; conservar su texto en el resultado.
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"fecha no válida: {fecha!r}")

    # Convertir las unidades y dar un motivo claro si no son un entero positivo.
    try:
        unidades = int(unidades_texto)
    except ValueError:
        raise ValueError(f"unidades no numéricas: {unidades_texto!r}")
    if unidades <= 0:
        raise ValueError(f"unidades no positivas: {unidades}")

    # Distinguir un precio ausente de uno que no se puede convertir a número.
    if not precio_texto:
        raise ValueError("precio ausente")
    try:
        # float espera un punto decimal; el CSV utiliza una coma.
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
    # Buscar el CSV junto al script, independientemente de dónde se ejecute.
    ruta = Path(__file__).resolve().parent / (
        "datos/sucios/ventas_2026_07_sucio.csv"
    )
    lineas = ruta.read_text(encoding="utf-8").splitlines()

    vistas = {}  # Línea original -> número donde apareció por primera vez.
    correctas = 0
    descartadas = 0
    total = 0.0

    # Saltar la cabecera y numerar desde 2 para coincidir con las filas del CSV.
    for numero, linea in enumerate(lineas[1:], start=2):
        try:
            venta = parsea_fila(linea)
            # Comparar la línea original: solo se descartan duplicados idénticos.
            if linea in vistas:
                raise ValueError(f"repite la fila {vistas[linea]}")
        except ValueError as error:
            # Descartar esta fila sin detener el procesamiento de las siguientes.
            descartadas += 1
            print(f"fila {numero} descartada: {error}")
            continue

        # Solo las ventas válidas y no repetidas se guardan y suman al total.
        vistas[linea] = numero
        correctas += 1
        total += venta["unidades"] * venta["precio"]

    print()
    print(f"Filas correctas: {correctas}")
    print(f"Filas descartadas: {descartadas}")
    print(f"TOTAL VENTAS JULIO: {total:.2f} EUR")


if __name__ == "__main__":
    main()
