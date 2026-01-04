
# Challenge Producción Minera

## Descripción
Este proyecto presenta una solución integral para el análisis de datos de producción minera,
incluyendo análisis exploratorio de datos, modelado de base de datos, desarrollo de una API REST
y visualización de indicadores clave.
El objetivo es permitir el análisis eficiente de la producción, consumo de recursos e incidentes
operativos a partir de un dataset estructurado.

---

## Estructura del proyecto
- backend/ → API REST desarrollada con FastAPI
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
Se eligió **Python** por su amplio ecosistema para el análisis de datos y desarrollo de APIs.
**FastAPI** fue seleccionado por su alto rendimiento, validación automática de datos mediante
Pydantic y documentación interactiva integrada (Swagger).
**Oracle SQL** se utilizó para el diseño del modelo relacional y consultas analíticas.
**Power BI** permite una visualización clara, interactiva y profesional de los indicadores clave
del negocio.

Este stack ofrece una solución escalable, clara y alineada con buenas prácticas de la industria.

---

## Requisitos técnicos
- Python 3.11
- FastAPI
- Uvicorn
- Pandas

Instalación de dependencias:
```bash
pip install fastapi uvicorn pandas

## Cómo acceder a la documentación de la API
Una vez levantada la API de manera local, se puede acceder a la documentación
interactiva (Swagger UI) desde el navegador en la siguiente dirección:

http://127.0.0.1:8000/docs


