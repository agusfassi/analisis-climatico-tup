import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------
# Script de análisis climático - Escenario A
# Autor: Agustin Fassi
# Materia: Organización Empresarial - UTN TUP
# -------------------------------------------------------
# Este script procesa el dataset de anomalías de temperatura
# global provisto por GCAG (Global Climate at a Glance).
# Se filtra una única fuente de datos para evitar duplicados,
# se calculan indicadores estadísticos básicos y se genera
# un gráfico de evolución temporal exportado a /resultados.
# -------------------------------------------------------

# Carga del dataset desde la carpeta /datos
# El archivo debe estar en formato CSV con columnas: Source, Year, Mean
df = pd.read_csv("datos/dataset.csv")

# Filtramos solo la fuente GCAG para evitar duplicados con GISTEMP
# Ambas fuentes registran anomalías pero con metodologías distintas
df = df[df["Source"] == "gcag"].copy()
df = df.sort_values("Year").reset_index(drop=True)

# Cálculo de indicadores estadísticos sobre la columna Mean
# Mean representa la anomalía respecto al promedio del período base 1951-1980
temp_promedio = df["Mean"].mean()
temp_maxima = df["Mean"].max()
temp_minima = df["Mean"].min()

print("=== INDICADORES CLIMÁTICOS ===")
print(f"Temperatura promedio (anomalía): {temp_promedio:.4f} °C")
print(f"Temperatura máxima registrada:   {temp_maxima:.4f} °C")
print(f"Temperatura mínima registrada:   {temp_minima:.4f} °C")

# Generación del gráfico de evolución temporal
# Se usa una línea punteada para indicar el promedio histórico
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Mean"], color="tomato", linewidth=1.5, label="Anomalía de temperatura")
plt.axhline(y=temp_promedio, color="steelblue", linestyle="--", label=f"Promedio: {temp_promedio:.2f} °C")
plt.title("Evolución de la Anomalía de Temperatura Global")
plt.xlabel("Año")
plt.ylabel("Anomalía (°C)")
plt.legend()
plt.tight_layout()

# Guardado del gráfico en /resultados usando ruta relativa
os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/grafico_temperatura.png")
plt.show()
print("Gráfico guardado en resultados/grafico_temperatura.png")

# Exportar resumen de indicadores a CSV
resumen = pd.DataFrame({
    "Indicador": ["Promedio", "Máxima", "Mínima"],
    "Valor (°C)": [temp_promedio, temp_maxima, temp_minima]
})
resumen.to_csv("resultados/resumen_indicadores.csv", index=False)
print("Resumen exportado en resultados/resumen_indicadores.csv")
