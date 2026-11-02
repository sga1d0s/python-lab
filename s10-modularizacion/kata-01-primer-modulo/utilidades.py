
def calcula_porcentaje(usado, total):
  """ Devuelve que porcentaje representa usado sobre total."""
  return usado / total * 100

if __name__== "__main__":
  print("Prueba módulo utilidades:")
  print(calcula_porcentaje(25, 100))