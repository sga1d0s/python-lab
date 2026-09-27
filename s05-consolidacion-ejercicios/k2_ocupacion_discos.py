print("\n\n-------------KATA1-------------")
print("-------------------------------\n")

lineas = [
    "/dev/sda1;45;100",
    "/dev/sdb1;180;500",
    "/dev/sdc1;95;100",
]

print(f"{"Disco":<12} {"Usado":>12} {"Total":>12} {"Ocupacion":>12}")

for linea in lineas:
  disco, usado, total = linea.split(';')
  usado = int(usado)
  total = int(total)
  ocupacion = usado / total * 100

  print(f"{disco:<12} {usado:>12} {total:>12} {ocupacion:>12}%")
  