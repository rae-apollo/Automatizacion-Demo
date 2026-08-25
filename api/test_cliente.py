import requests
import pytest
from .conftest import logger
# Marcador para indicar que esta prueba es de tipo GET.
@pytest.mark.get 
# Función de prueba para obtener la lista de pasajeros.
def test_obtener_pasajeros(request, api_url, token_cliente):
    endpoint = f"{api_url}/passengers/previews"
    logger.info(f"Realizando solicitud GET a {endpoint} con token: {token_cliente}")
    params = {
        "pageIndex": 1,
        "pageSize": 50,
        "orderBy": "userName",
        "sortOrder": "Ascending"
    }
    headers = {
        "Access-Token": token_cliente
    }

    response = requests.get(endpoint, params=params, headers=headers)
    logger.info(f"Respuesta recibida con status code: {response.status_code} y contenido: {response.json()}")

# Imprimir información relevante para depuración y verificación de la prueba.
    print(f"\n[TOKEN UTILIZADO]: {token_cliente}")
    print(f"[STATUS CODE]: {response.status_code}")
    print(f"[RESPONSE JSON]: {response.json()}")

    request.node.status_code = response.status_code  # Guardar el status code en el nodo de la prueba para su uso en los hooks.
    assert response.status_code == 200

