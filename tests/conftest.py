import pytest
from selenium import webdriver
# Configuramos el driver de Chrome utilizando webdriver_manager
from selenium.webdriver.chrome.service import Service
# Configuramos las opciones de Chrome para deshabilitar el guardado de contraseñas y otras características que puedan interferir con las pruebas
from selenium.webdriver.chrome.options import Options
# Importamos ChromeDriverManager para gestionar automáticamente la descarga y actualización del controlador de Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Fixture para inicializar y cerrar el driver de Selenium.
@pytest.fixture
def driver():
# Configuramos las opciones de Chrome para deshabilitar el guardado de contraseñas y otras características que puedan interferir con las pruebas
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.geolocation": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
# Configuramos el driver de Chrome utilizando webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit() # Cerramos el navegador al finalizar la prueba


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ejecutamos el hook original y obtenemos el resultado
    outcome = yield
    report = outcome.get_result()

    if item.obj.__doc__:

        node_doc = item.obj.__doc__.strip().split("\n")[0]  # Obtenemos la primera línea de la docstring

        if hasattr(item, 'callspec'):
            # Si la prueba es parametrizada, obtenemos los parámetros
            params = f"[{item.callspec.id}]"
            report.nodeid = f"{node_doc} {params}"
        else:
            report.nodeid = node_doc

