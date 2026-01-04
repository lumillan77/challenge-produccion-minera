# ==============================
# Parte A: Análisis de Datos
# Challenge Producción Minera
# ==============================

import pandas as pd

df = pd.read_csv("data/produccion_minera.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

df = df.dropna()

print("\nInformación del dataset después de limpiar nulos:")
print(df.info())

# ==============================
# MÉTRICAS CLAVE
# ==============================

# Productividad por equipo (promedio de toneladas extraídas)
productividad_equipo = df.groupby("equipo_id")["toneladas_extraidas"].mean()

print("\nProductividad promedio por equipo:")
print(productividad_equipo)


# Eficiencia de combustible (toneladas por unidad de combustible)
df["eficiencia_combustible"] = df["toneladas_extraidas"] / df["consumo_combustible"]

# Promedio de eficiencia por equipo
eficiencia_equipo = df.groupby("equipo_id")["eficiencia_combustible"].mean()

print("\nEficiencia promedio de combustible por equipo:")
print(eficiencia_equipo)


# Promedio de incidentes por equipo
incidentes_equipo = df.groupby("equipo_id")["incidentes"].mean()

print("\nPromedio de incidentes por equipo:")
print(incidentes_equipo)

# Promedio general de incidentes
promedio_incidentes = df["incidentes"].mean()
print("\nPromedio general de incidentes:", promedio_incidentes)


# Productividad promedio por operador A3
productividad_operador = df.groupby("operador")["toneladas_extraidas"].mean()

print("\nProductividad promedio por operador:")
print(productividad_operador)

# Operador con mejor rendimiento
mejor_operador = productividad_operador.idxmax()
mejor_valor = productividad_operador.max()

print("\nOperador con mejor rendimiento:")
print(mejor_operador, "-", mejor_valor)


# ==============================
# ESTADÍSTICAS DESCRIPTIVAS
# ==============================

# Estadísticas por zona
estadisticas_zona = df.groupby("zona")["toneladas_extraidas"].describe()

print("\nEstadísticas descriptivas por zona:")
print(estadisticas_zona)

# Estadísticas por turno
estadisticas_turno = df.groupby("turno")["toneladas_extraidas"].describe()

print("\nEstadísticas descriptivas por turno:")
print(estadisticas_turno)


# ==============================
# DETECCIÓN DE ANOMALÍAS
# ==============================

media = df["toneladas_extraidas"].mean()
desviacion = df["toneladas_extraidas"].std()

limite_superior = media + 2 * desviacion
limite_inferior = media - 2 * desviacion

anomalias = df[
    (df["toneladas_extraidas"] > limite_superior) |
    (df["toneladas_extraidas"] < limite_inferior)
]

print("\nProducciones anómalas detectadas:")
print(anomalias[["fecha", "equipo_id", "operador", "toneladas_extraidas"]])

print("\nTotal de anomalías detectadas:", len(anomalias))