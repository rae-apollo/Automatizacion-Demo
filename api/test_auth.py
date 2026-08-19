import pytest

@pytest.mark.parametrize("endpoint_path, username, password", [
    ("/clientes/auth/accesstoken", "ehs@sommytech.com.ar", "123456"),
    ("/suppliers/auth/accesstoken", "778", "driver01"),
    ("/operadores/auth/accesstoken", "admin", "EHS1974")
])
def test_login_api_exitoso(realizar_login, endpoint_path, username, password):
    response = realizar_login(endpoint_path, username, password)
    assert response.status_code == 200
    assert "token" in response.json()