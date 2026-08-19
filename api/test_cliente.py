import requests
import pytest

# Marcador para indicar que esta prueba es de tipo GET.
@pytest.mark.get 
# Función de prueba para obtener la lista de pasajeros.
def test_obtener_pasajeros(api_url, token_cliente):
    endpoint = f"{api_url}/passengers/previews"
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
    assert response.status_code == 200

