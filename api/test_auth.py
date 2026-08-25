import pytest
from data.data_login import API_LOGIN_EXITOSO

@pytest.mark.post
@pytest.mark.parametrize("endpoint_path, username, password", API_LOGIN_EXITOSO)
def test_login_api_exitoso(realizar_login, endpoint_path, username, password):
    response = realizar_login(endpoint_path, username, password)
    assert response.status_code == 200
    assert "token" in response.json()