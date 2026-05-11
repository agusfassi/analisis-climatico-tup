import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------
# Script de análisis climático - Escenario A
# Autor: Agustin Fassi
# Descripción: Procesa datos de temperatura global (GCAG)
# y genera indicadores estadísticos básicos y un gráfico
# de evolución temporal. Los resultados se exportan a
# la carpeta /resultados.
# -------------------------------------------------------

df = pd.read_csv("datos/dataset.csv")

# Filtramos la fuente GCAG para evitar duplicados con GISTEMP
df = df[df["Source"] == "gcag"].copy()
df = df.sort_values("Year").reset_index(drop=True)

# Indicadores estadísticos básicos
temp_promedio = df["Mean"].mean()
temp_maxima = df["Mean"].max()
temp_minima = df["Mean"].min()

print("=== INDICADORES CLIMÁTICOS ===")
print(f"Temperatura promedio (anomalía): {temp_promedio:.4f} °C")
print(f"Temperatura máxima registrada:   {temp_maxima:.4f} °C")
print(f"Temperatura mínima registrada:   {temp_minima:.4f} °C")

# Gráfico de evolución temporal
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Mean"], color="tomato", linewidth=1.5, label="Anomalía de temperatura")
plt.axhline(y=temp_promedio, color="steelblue", linestyle="--", label=f"Promedio: {temp_promedio:.2f} °C")
plt.title("Evolución de la Anomalía de Temperatura Global")
plt.xlabel("Año")
plt.ylabel("Anomalía (°C)")
plt.legend()
plt.tight_layout()

os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/grafico_temperatura.png")
plt.show()
print("Gráfico guardado en resultados/grafico_temperatura.png")

# Exportar resumen de indicadores
resumen = pd.DataFrame({
    "Indicador": ["Promedio", "Máxima", "Mínima"],
    "Valor (°C)": [temp_promedio, temp_maxima, temp_minima]
})
resumen.to_csv("resultados/resumen_indicadores.csv", index=False)
print("Resumen exportado en resultados/resumen_indicadores.csv")
