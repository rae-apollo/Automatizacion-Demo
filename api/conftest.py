pytest_plugins = ["conftest"]
import pytest
import logging
import pathlib
import requests
from data.data_login import API_LOGIN_EXITOSO

@pytest.fixture(scope="session")
# Fixture para obtener la URL base de la API.
def api_url():
    return "https://api.traslada.com.ar"

@pytest.fixture(scope="session")
# Fixture para realizar el login y obtener el token.
def realizar_login(api_url):
    def _login(ruta_endpoint, username, password, api_key="apikey_valida"):
        endpoint = f"{api_url}/{ruta_endpoint.lstrip('/')}"
        payload = {
            "ApiKey": api_key,
            "UserName": username,
            "Password": password
        }
        return requests.post(endpoint, json=payload)
    return _login

@pytest.fixture(scope="session")
# Fixture para obtener el token de cliente que realiza login.
def token_cliente(realizar_login):
    ruta_endpoint, username, password = API_LOGIN_EXITOSO[0]  # Tomamos el primer conjunto de credenciales válidas
    response = realizar_login(ruta_endpoint, username, password)
    return response.json().get("token")
# Fixture para configurar el logger.
path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=path_dir / 'historial.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()

