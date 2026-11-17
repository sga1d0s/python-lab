def formatea_bytes(n):
  """Convierte un número de bytes en una cadena legible (KB, MB, GB,
  TB)."""
  unidades = ["B", "KB", "MB", "GB", "TB"]
  tamano = float(n)
  indice = 0
  while tamano >= 1024 and indice < len(unidades) - 1:
    tamano = tamano / 1024
    indice = indice + 1
  return f"{tamano:.2f} {unidades[indice]}"

if __name__ == "__main__":
  print(f"100 formateado a {formatea_bytes(100)}")