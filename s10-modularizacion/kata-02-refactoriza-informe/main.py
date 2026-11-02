print("\n\n-------------KATA2-------------")
print("-------------------------------\n")

from validaciones import valida_ip
from alertas import clasifica_alerta
from formato import formatea_bytes

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

def genera_informe():
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

  print()
  print("--- Resumen ---")

genera_informe()

for estado in contador_estados:
    print(f"{estado}: {contador_estados[estado]}")
