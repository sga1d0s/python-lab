print("\n\n-------------KATA2-------------")
print("-------------------------------\n")


flota = [
    {"host": "srv-web01", "cpu": 45, "ram": 60, "disco": 70},
    {"host": "srv-web02", "cpu": 92, "ram": 55, "disco": 40},
    {"host": "srv-db01", "cpu": 70, "ram": 88, "disco": 81},
    {"host": "srv-db02", "cpu": 30, "ram": 40, "disco": 95},
    {"host": "srv-bck01", "cpu": 10, "ram": 20, "disco": 74},
    {"host": "srv-mail01", "cpu": 75, "ram": 50, "disco": 60},
    {"host": "srv-dns01", "cpu": 5, "ram": 15, "disco": 20},
]

CRITICAL = 90
WARNING = 75


def clasifica_alerta(cpu, ram, disco):

    if cpu >= CRITICAL or ram >= CRITICAL or disco >= CRITICAL:
        return "CRITICAL"

    if cpu >= WARNING or ram >= WARNING or disco >= WARNING:
        return "WARNING"

    if cpu < WARNING or ram < WARNING or disco < WARNING:
        return "OK"


critical = 0
warning = 0
ok = 0

for servidor in flota:
    alerta = clasifica_alerta(servidor["cpu"], servidor["ram"], servidor["disco"])

    print(f"Servidor: {servidor['host']}", alerta)

    if alerta == "OK":
        ok += 1
    elif alerta == "WARNING":
        warning += 1
    else:
        critical += 1

print(f"\nOK: {ok}   *   WARNING: {warning}   *   CRITICAL: {critical}")
