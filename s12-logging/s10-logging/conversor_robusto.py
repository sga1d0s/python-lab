UNIDADES = {"kb": 1, "mb": 1024, "gb": 1024**2, "tb": 1024**3}


def convertir(valor, origen, destino):
    """Convierte un valor entre unidades; lanza errores si los datos son malos."""
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")

    if origen not in UNIDADES or destino not in UNIDADES:
        raise KeyError(f"unidad desconocida: {origen} o {destino}")

    valor_en_kb = valor * UNIDADES[origen]
    return valor_en_kb / UNIDADES[destino]


while True:  # Reintenta después de cualquier entrada inválida.
    try:
        valor = float(input("Valor a convertir: "))
        origen = input("Unidad de origen (kb/mb/gb/tb): ").strip().lower()
        destino = input("Unidad de destino (kb/mb/gb/tb): ").strip().lower()
        resultado = convertir(valor, origen, destino)
    except ValueError as error:
        print(f"Entrada no válida: {error}")
    except KeyError as error:
        print(f"Unidad no reconocida: {error}")
    else:  # Solo se ejecuta cuando no hubo excepción.
        print(f"{valor} {origen.upper()} son {resultado:.4f} {destino.upper()}")
    finally:  # Se ejecuta tanto si funcionó como si falló.
        print("-- intento de conversión terminado --")
