print("\n\n-------------KATA3-------------")
print("-------------------------------\n")

""" La monitorización os pasa el uso de CPU, RAM y disco (en %) de toda la flota:
Cada servidor se clasifica así:

CRITICAL si cualquiera de los tres valores es ≥ 90.
WARNING si ninguno llega a 90 pero alguno es ≥ 75.
OK en cualquier otro caso.

Imprimid una línea por servidor con su estado y, al final, cuántos hay de cada estado.

Ejemplo de ejecución:

srv-web01: OK
srv-web02: CRITICAL
srv-db01: WARNING
...
OK: 3 · WARNING: 2 · CRITICAL: 2

* En cada vuelta, servidor["cpu"] os da la CPU de ese servidor (es un dict, como en la S04).
* Comprobad primero la condición más grave (CRITICAL); si no se cumple,pasad a la siguiente.
* or os permite comprobar “cualquiera de los tres” sin anidar tres if .
* Para el recuento final valen tres contadores sueltos o un dict {"OK": 0, "WARNING": 0, "CRITICAL": 0} al que sumáis 1 en la clave del estado.
* srv-bck01 y srv-mail01 están justo en los límites: si os salen mal, mirad > frente a >= . """

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

critical = 0
warning = 0
ok = 0

for servidor in flota:
    if (
        servidor["cpu"] >= CRITICAL
        or servidor["ram"] >= CRITICAL
        or servidor["disco"] >= CRITICAL
    ):
        critical += 1
        print(f"{servidor['host']}: CRITICAL")
    elif (
        servidor["cpu"] >= WARNING
        or servidor["ram"] >= WARNING
        or servidor["disco"] >= WARNING
    ):
        warning += 1
        print(f"{servidor['host']}: WARNING")
    else:
        ok += 1
        print(f"{servidor['host']}: OK")

print(f"OK: {ok}   *   WARNING: {warning}   *   CRITICAL: {critical}")
