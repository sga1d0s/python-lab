# Import para majeno de excel
import pandas as pd

# Import para generar gráficos
import matplotlib.pyplot as plt

# Import para manejo de directorios
from pathlib import Path

print("\n\n--------PROYECTO1_GALDOS-------")
print("-------------------------------\n")

df = pd.read_excel("incidencias_it.xlsx")
print(df.head())

# 1.- CARGA
print("\nNúmero total de filas")
print(len(df))

print("\nNúmero total de columnas")
print(len(df.columns))

# 2.- INDICADORES
##### Total de incidencias y % por estado.
total_incidencias = len(df)
por_estado = df["estado"].value_counts()
porcentaje_estado = por_estado / total_incidencias * 100

print(f"\nTotal de incidencias: {total_incidencias}")
print(f"\nIncidencias por {por_estado}")
print(f"\nPorcentaje por {porcentaje_estado}")

##### Incidencias por categoría.
por_categoria = df["categoria"].value_counts()

print(f"\nIncidencias por {por_categoria}")

##### Incidencias por departamento.
por_departamento = df["departamento"].value_counts()

print(f"\nIncidencias por {por_departamento}")

##### Media de horas_resolucion de las incidencias cerradas.
cerradas = df[df["estado"] == "Cerrada"]
media_horas = cerradas["horas_resolucion"].mean()  # hace la media de los valores

print(f"\nMedia de resolución de incidencias cerradas: {media_horas:.2f} horas")

##### Técnico con más incidencias cerradas.
cerradas_por_tecnico = cerradas["tecnico"].value_counts()

tecnico_mas_cierres = cerradas_por_tecnico.idxmax()
numero_de_cierres = cerradas_por_tecnico.max()

print(f"\nTécnico con más incidencias cerradas: {tecnico_mas_cierres}")
print(f"Incidencias cerradas: {numero_de_cierres}")

# 3.- GRÁFICOS
Path("salida").mkdir(exist_ok=True)

##### Gráfico de incidencias por categoría.
plt.figure(figsize=(8, 5))

por_categoria.plot(kind="bar")

plt.title("Incidencias por categoría")
plt.xlabel("Categoría")
plt.ylabel("Número de incidencias")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("salida/grafico_categorias.png")
plt.close()

print("\nGráfico de incidencias por categoría finalizado")

##### Gráfico de incidencias por departamento.
plt.figure(figsize=(8, 5))

por_departamento.plot(kind="pie")

plt.title("Incidencias por departamento")
plt.xlabel("Departamento")
plt.ylabel("Número de incidencias")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("salida/grafico_departamentos.png")
plt.close()
print("\nGráfico de incidencias por departamento finalizado")

##### Gráfico de evolución mensual.
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")

por_mes = df.groupby("mes").size().sort_index()

plt.figure(figsize=(8, 5))

por_mes.plot(kind="line", marker="o")

plt.title("Evolución mensual de incidencias")
plt.xlabel("Mes")
plt.ylabel("Número de incidencias")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("salida/grafico_evolucion.png")
plt.close()
print("\nGráfico de evolución mensual finalizado")

##### Media de horas de resolución por prioridad.
media_por_prioridad = cerradas.groupby("prioridad")["horas_resolucion"].mean()

print("\nMedia de resolución por prioridad (horas):")
print(media_por_prioridad.round(2))

##### Mes con más incidencias y su categoría principal.
mes_negro = por_mes.idxmax()
incidencias_mes_negro = por_mes.max()

datos_mes_negro = df[df["mes"] == mes_negro]
categorias_mes_negro = datos_mes_negro["categoria"].value_counts()

categoria_principal = categorias_mes_negro.idxmax()
incidencias_categoria_principal = categorias_mes_negro.max()

print(f"\nMes con más incidencias: {mes_negro}")
print(f"Total de incidencias: {incidencias_mes_negro}")
print(f"Categoría más frecuente: {categoria_principal}")
print(f"Incidencias de esa categoría: {incidencias_categoria_principal}")

print("\nRecuento por categoría en ese mes:")
print(categorias_mes_negro)

##### Cruce categoría * departamento.
cruce_categoria_departamento = (
    df.groupby(["categoria", "departamento"]).size().unstack(fill_value=0)
)

print("\nIncidencias por categoría y departamento:")
print(cruce_categoria_departamento)

# 4.- EXPORTAR INDICADORES
# Resumen general
resumen = pd.DataFrame(
    {
        "Indicador": [
            "Total de incidencias",
            "Media de resolución de cerradas (horas)",
            "Técnico con más incidencias cerradas",
            "Número de cierres del técnico",
        ],
        "Valor": [
            total_incidencias,
            media_horas,
            tecnico_mas_cierres,
            numero_de_cierres,
        ],
    }
)

# Resumen del mes negro
resumen_mes_negro = pd.DataFrame(
    {
        "Indicador": [
            "Mes con más incidencias",
            "Total de incidencias del mes",
            "Categoría más frecuente del mes",
            "Incidencias de esa categoría",
        ],
        "Valor": [
            str(mes_negro),
            incidencias_mes_negro,
            categoria_principal,
            incidencias_categoria_principal,
        ],
    }
)

tabla_estados = pd.DataFrame(
    {"Incidencias": por_estado, "Porcentaje": porcentaje_estado}
)

with pd.ExcelWriter("salida/indicadores.xlsx") as writer:
    resumen.to_excel(writer, sheet_name="Resumen", index=False)
    tabla_estados.to_excel(writer, sheet_name="Estados")
    por_categoria.to_excel(writer, sheet_name="Categorias")
    por_departamento.to_excel(writer, sheet_name="Departamentos")
    cerradas_por_tecnico.to_excel(writer, sheet_name="Tecnicos")
    por_mes.to_excel(writer, sheet_name="Evolucion mensual")
    media_por_prioridad.to_excel(writer, sheet_name="Horas por prioridad")
    resumen_mes_negro.to_excel(writer, sheet_name="Mes negro", index=False)
    categorias_mes_negro.to_excel(writer, sheet_name="Categorias mes negro")
    cruce_categoria_departamento.to_excel(writer, sheet_name="Categoria x departamento")

print("\nIndicadores exportados a salida/indicadores.xlsx")

# 5.- GENERAR INFORME AUTOMÁTICAMENTE
categoria_top = por_categoria.idxmax()
cantidad_categoria_top = por_categoria.max()
porcentaje_categoria_top = cantidad_categoria_top / total_incidencias * 100

departamento_top = por_departamento.idxmax()
cantidad_departamento_top = por_departamento.max()

porcentaje_cerradas = len(cerradas) / total_incidencias * 100
pendientes = total_incidencias - len(cerradas)

texto_informe = f"""# Informe de incidencias IT

Se han analizado {total_incidencias} incidencias para conocer las
necesidades de soporte y el estado de su resolución.

## Tres hallazgos principales

1. {categoria_top} es la categoría con más incidencias, con
   {cantidad_categoria_top} casos ({porcentaje_categoria_top:.2f} % del total).
   Conviene revisar sus problemas recurrentes para identificar
   posibles medidas de prevención.

2. {departamento_top} registra el mayor volumen de incidencias,
   con {cantidad_departamento_top} casos. Este dato ayuda a planificar
   el soporte, aunque no permite comparar tasas de incidencias
   sin conocer el tamaño de cada departamento.

3. El {porcentaje_cerradas:.2f} % de las incidencias están cerradas,
   con una media de resolución de {media_horas:.2f} horas.
   Quedan {pendientes} incidencias abiertas o en curso que requieren
   seguimiento según su urgencia.

## Análisis adicional

### Resolución por prioridad

Media de horas de resolución de las incidencias cerradas:
"""

for prioridad, horas in media_por_prioridad.items():
    texto_informe += f"- {prioridad}: {horas:.2f} horas.\n"

texto_informe += f"""
### Mes con más incidencias

El mes {mes_negro} registró el mayor volumen, con
{incidencias_mes_negro} incidencias. La categoría que más contribuyó
a ese volumen fue {categoria_principal}, con
{incidencias_categoria_principal} casos.

### Cruce de categorías y departamentos

La hoja «Categoria x departamento» de salida/indicadores.xlsx
permite consultar cuántas incidencias de cada categoría
se registraron en cada departamento.

## Criterio de cálculo

Las medias de resolución se calculan únicamente sobre incidencias
cerradas, ignorando las horas vacías y sin sustituirlas por cero.
Si hay empate en un máximo, se muestra el primero obtenido.

## Gráficos

![Incidencias por categoría](salida/grafico_categorias.png)

![Incidencias por departamento](salida/grafico_departamentos.png)

![Evolución mensual](salida/grafico_evolucion.png)
"""

Path("informe.md").write_text(texto_informe, encoding="utf-8")

print("\nInforme generado en informe.md")