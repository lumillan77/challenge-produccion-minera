
# Challenge Producción Minera

## Descripción
Este proyecto presenta una solución integral para el análisis de datos de producción minera,
incluyendo análisis exploratorio de datos, modelado de base de datos, desarrollo de una API REST
y visualización de indicadores clave.
El objetivo es permitir el análisis eficiente de la producción, consumo de recursos e incidentes
operativos a partir de un dataset estructurado.

---

## Estructura del proyecto
- api/ → API REST desarrollada con FastAPI
- data/ → Dataset original en formato CSV
- sql/ → Scripts SQL (creación de tablas, modelo normalizado y consultas)
- scripts/ → Análisis exploratorio en Python
- visualizaciones/ → Dashboard de visualización
- README.md → Documentación del proyecto

---

## Tecnologías utilizadas
- **Análisis de datos:** Python (Pandas)
- **Base de datos:** Oracle SQL
- **Backend / API:** Python (FastAPI)
- **Visualización:** Power BI

---

## Justificación del stack
Se eligió **Python** por su amplio ecosistema para análisis de datos y desarrollo backend.
**FastAPI** fue seleccionado por su alto rendimiento, validación automática de datos y
documentación interactiva (Swagger).
**Oracle SQL** se utilizó para el modelado relacional y consultas analíticas.
**Power BI** permite una visualización clara y profesional de los indicadores de negocio.

Este stack permite una solución clara, escalable y alineada con buenas prácticas de la industria.

---

## Requisitos técnicos
- Python 3.11
- FastAPI
- Uvicorn
- Pandas

Instalación de dependencias:
```bash
pip install fastapi uvicorn pandas