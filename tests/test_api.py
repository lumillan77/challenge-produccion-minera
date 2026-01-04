
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_get_produccion():
    """
    Test del endpoint GET /produccion
    Verifica que devuelva una lista con datos
    """
    response = client.get("/produccion")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_produccion_por_equipo():
    """
    Test del endpoint GET /produccion/{equipo_id}
    Verifica que filtre correctamente por equipo
    """
    response = client.get("/produccion/EQ-004")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(row["equipo_id"] == "EQ-004" for row in data)


def test_get_produccion_equipo_inexistente():
    """
    Test de manejo de error cuando el equipo no existe
    """
    response = client.get("/produccion/EQ-999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Equipo no encontrado"


def test_ranking_operadores():
    """
    Test del endpoint GET /ranking/operadores
    Verifica que devuelva un ranking válido
    """
    response = client.get("/ranking/operadores")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0