""" KATA1 """
# tiempos = [120, 95, 300, 80, 150]

# total = 0
# for tiempo in tiempos:
#   total = total + tiempo

# media = total / len(tiempos)
# maximo = max(tiempos)

# print(f"Tiempos registrados: {tiempos}")
# print(f"Total: {total} ms")
# print(f"Media: {media} ms")
# print(f"Maximo: {maximo} ms")

""" KATA2 """
# hostnames = ['srv-web01', 'pc-oficina03', 'srv-db01', 'laptop-ana', 'srv-backup']

# servidores = []

# for host in hostnames:
#   if host.startswith("srv-"):
#     servidores.append(host)

# print(f"Equipos totales: {hostnames}")
# print(f"Servidores encontrados: {servidores}")
# print(f"Numero de servidores: {len(servidores)}")

""" KATA3 """
totalProductos = int(input("¿Cuantos productos quieres añadir? "))
listaCompra = []

for i in range(totalProductos):
  producto = input(f"Producto {i + 1}: ")
  listaCompra.append(producto)

print("Tu lista de la compra:")
for producto in listaCompra:
  print(f"- {producto}")

print(f"Total productos {len(listaCompra)}")