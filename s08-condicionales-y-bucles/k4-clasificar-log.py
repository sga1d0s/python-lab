print("\n\n-------------KATA4-------------")
print("-------------------------------\n")

""" datos/auth.log es el log de SSH de un servidor: 600 líneas como estas.

Jun 14 00:04:20 srv-web01 sshd[8150]: Invalid user user from 165.71.109.230 port 63522
Jun 14 00:12:51 srv-web01 sshd[8874]: Accepted publickey for deploy from 192.168.1.44 port 50944 ssh2
Jun 14 00:30:46 srv-web01 sshd[3926]: Failed password for postgres from 69.167.105.132 port 51713 ssh2 

Recorred todas las líneas y clasificad cada una en una de cuatro clases: Failed
password , Accepted , Invalid user u otras. Al final, imprimid cuántas hay
de cada clase y el total.

Ejemplo de ejecución:

Failed password: ...
Accepted: ...
Invalid user: ...
Otras: ...
Total: 600


• lineas = Path("datos/auth.log").read_text().splitlines() os da
  la lista de líneas (con from pathlib import Path arriba).
• Las líneas empiezan por la fecha, así que startswith sobre la línea entera
  no sirve: usad in . Si preferís startswith , quedaos antes con el mensaje:
  linea.split(": ", 1)[1].
• Una línea va a una sola clase: cadena de elif con un else para las otras.
• in distingue mayúsculas. En el log hay líneas como
  Failed password for invalid user postgres : ¿en qué clase caen?
• Comprobad vuestros números con grep -c "Failed password" datos/
  auth.log y compañía: si Python y grep no coinciden, el que se equivoca es
  vuestro script. Y los cuatro juntos tienen que sumar 600.
"""

from pathlib import Path

lineas = Path("datos/auth.log").read_text().splitlines()

passwordFail = 0
accepted = 0
invalidUser = 0
other = 0

total = 0

for key, linea in enumerate(lineas, start=1):
    if "failed password" in linea.lower():
        passwordFail += 1
    elif "accepted" in linea.lower():
        accepted += 1
    elif "Invalid user" in linea:
        invalidUser += 1
    else:
        other += 1

    total += 1


print(f"Failed password: {passwordFail}")
print(f"Accepted: {accepted}")
print(f"Invalid user: {invalidUser}")
print(f"Otras: {other}")
print(f"Total: {total}")
