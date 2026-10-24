print("\n\n-------------KATA3-------------")
print("-------------------------------\n")


def formateaBytes(n, decimales=2):
    unidades = ["B", "KB", "MB", "GB", "TB"]
    indice = 0

    while n >= 1024 and indice < len(unidades):
        n = n / 1024
        indice += 1

    return print(f"{n:.{decimales}f} {unidades[indice]}")


formateaBytes(500)
formateaBytes(2048)
formateaBytes(1536000)
formateaBytes(5_000_000_000)
formateaBytes(2048, decimales=0)
