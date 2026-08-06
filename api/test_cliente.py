import requests

def test_obtner_pasajeros(api_url, token_cliente):
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

