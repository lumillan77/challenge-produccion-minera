
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os


# APP

app = FastAPI(title="API Producción Minera")


# CARGA DE DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "produccion_minera.csv")

df = pd.read_csv(DATA_PATH)

# Limpiar columnas
df.columns = df.columns.str.strip()

for col in ["equipo_id", "turno", "operador", "zona"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Evitar NaN → JSON error
df = df.replace({np.nan: None})

print(df.columns)


# MODELO Pydantic

class ProductionRecord(BaseModel):
    fecha: str
    turno: str
    equipo_id: str
    operador: str
    zona: str
    toneladas_extraidas: float
    horas_operativas: float
    consumo_combustible: float | None = None
    incidentes: int
    ley_mineral: float



# ENDPOINTS

#produccion

@app.get("/produccion")
def get_produccion(limit: int = 10, offset: int = 0):
    return df.iloc[offset: offset + limit].to_dict(orient="records")


#produccion(equipo_id)

@app.get("/produccion/{equipo_id}")
def produccion_por_equipo(equipo_id: str):
    data = df[df["equipo_id"] == equipo_id]

    if data.empty:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    return data.to_dict(orient="records")


#estadisticas por zona

@app.get("/estadisticas/zona/{nombre}")
def estadisticas_por_zona(nombre: str):
    data = df[df["zona"].str.lower() == nombre.lower()]

    if data.empty:
        raise HTTPException(status_code=404, detail="Zona no encontrada")

    return {
        "zona": nombre,
        "produccion_total": float(data["toneladas_extraidas"].sum()),
        "produccion_promedio": float(data["toneladas_extraidas"].mean()),
        "incidentes_promedio": float(data["incidentes"].mean())
    }


#ranking de operadores

@app.get("/ranking/operadores")
def ranking_operadores():
    ranking = (
        df.groupby("operador")["toneladas_extraidas"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    return ranking.to_dict(orient="records")

#produccion

@app.post("/produccion")
def agregar_produccion(registro: ProductionRecord):
    global df

    nuevo = pd.DataFrame([registro.model_dump()])
    df = pd.concat([df, nuevo], ignore_index=True)

    df.to_csv(DATA_PATH, index=False)

    return {"mensaje": "Registro agregado correctamente"}