import pytest
import logging
import pathlib
import requests

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
# Fixture para obtener el token de cliente.
def token_cliente(realizar_login):
    response = realizar_login("/clientes/auth/accesstoken", "ehs@sommytech.com.ar", "123456")
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

@pytest.hookimpl(hookwrapper=True)
# Hook para capturar el resultado de cada prueba y registrar información relevante.
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        report.status_code = getattr(item, "status_code", "N/A")
# Hook para agregar una columna de "Status Code" en el reporte HTML.
def pytest_html_results_table_header(cells):
    cells.insert(1, '<th>Status Code</th>')
# Hook para agregar el valor del "Status Code" en la fila correspondiente del reporte HTML.
def pytest_html_results_table_row(report, cells):
    status = getattr(report, "status_code", "N/A")
    cells.insert(1, f'<td>{status}</td>')
