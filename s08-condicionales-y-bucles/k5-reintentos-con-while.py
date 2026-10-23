print("\n\n-------------KATA5-------------")
print("-------------------------------\n")

""" Un script de despliegue comprueba que un servicio responde antes de seguir, y lo
reintenta como mucho 5 veces. Como todavía no hablamos con la red, el resulta‐
do de cada intento lo simula una lista: el intento 1 da el primer elemento, el 2 el
segundo, y así.

resultados = ["timeout", "timeout", "error", "ok"]

Con un while , imprimid cada intento con su resultado; en cuanto salga "ok" ,
cortad con break y decid en qué intento respondió. Si se agotan los 5 intentos
sin "ok", terminad con un mensaje de error.

Ejemplo de ejecución:

Intento 1: timeout
Intento 2: timeout
Intento 3: error
Intento 4: ok
Servicio disponible en el intento 4.

Después, la variante: cambiad la lista por una en la que el servicio no responde
nunca y comprobad que sale el error.

resultados = ["timeout", "error", "timeout", "timeout", "error"]

Intento 1: timeout
Intento 2: error
Intento 3: timeout
Intento 4: timeout
Intento 5: error
ERROR: el servicio no responde tras 5 intentos.

* Guardad el máximo en una variable ( MAX_INTENTOS = 5 ) y usad un conta‐
  dor de intentos: while intento < MAX_INTENTOS: .
* resultados[intento] os da el resultado del intento actual si el contador
  empieza en 0.
* Al salir del while no sabéis si fue por el break o por agotar los intentos:
  una booleana ( disponible = False antes del bucle, True justo antes del
  break ) os lo dice. """

resultados = ["timeout", "timeout", "error", "ok"]

intento = 0
MAX_INTENTOS = 5

while intento < MAX_INTENTOS:
    resultado = resultados[intento]
    intento += 1
    print(f"Intento {intento}: {resultado}")

    if resultado == "ok":
        break

print(f"Servicio disponible en el intento {intento}")

intento = 0
MAX_INTENTOS = 5

resultados = ["timeout", "error", "timeout", "timeout", "error"]

while intento < MAX_INTENTOS:
    resultado = resultados[intento]
    intento += 1
    print(f"Intento {intento}: {resultado}")

    if resultado == "ok":
        print(f"Servicio disponible en el intento {intento}")
        break

print(f"ERROR: el servicio no responde tras {intento} intentos.")
