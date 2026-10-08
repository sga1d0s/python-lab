import pandas as pd

df = pd.read_excel("datos/servidores.xlsx")

print(df.head())    # primeras 5 filas
df.info()           # columnas, tipos y huecos vacíos
print(len(df))      # nº de filas
print(df.columns)   # nombres de las columnas

print(df["so"].head())   # una columna (aqui, sus 5 primeros valores)

activos = df[df["estado"] == "activo"]
print(len(activos)) # 28