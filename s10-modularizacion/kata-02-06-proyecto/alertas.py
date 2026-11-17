def clasifica_alerta(cpu, ram, disco):
  """Clasifica el estado de un servidor según su CPU, RAM y disco (%)."""
  if cpu >= 90 or ram >= 90 or disco >= 90:
    return "CRITICAL"
  elif cpu >= 75 or ram >= 75 or disco >= 75:
    return "WARNING"
  else:
    return "OK"

if __name__ =="__main__":
  data = {
    "cpu": 80, "ram": 75, "disco": 25
  }
  print(f"Clasificación CPU: 80, RAM: 75, Disco: 25 -> {clasifica_alerta(data["cpu"], data["ram"], data["disco"])}")