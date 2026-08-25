import time
import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.data_login import LOGIN_WEB_CLIENTES

USUARIO_VALIDO, PASSWORD_VALIDO, _= LOGIN_WEB_CLIENTES[0]
USUARIO_INVALIDO, PASSWORD_INVALIDO, _= LOGIN_WEB_CLIENTES[1]

# Función de prueba para verificar el login exitoso y la navegación a la nueva reserva de remis.
def test_login(driver: WebDriver):
    """ CASO 1 : Login exitoso y navegación a nueva reserva de remis"""
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO) # Iniciamos sesión con las credenciales de prueba
    WebDriverWait(driver, 10).until(EC.url_contains("services")) # Esperamos a que la URL contenga "services".
    assert "services" in driver.current_url
    time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
# Función de prueba para verificar el login fallido con credenciales inválidas.
def test_login_fallido(driver: WebDriver):
    """ CASO 2 : Login fallido con credenciales inválidas """
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    login_page.iniciar_sesion(USUARIO_INVALIDO, PASSWORD_INVALIDO) # Iniciamos sesión con las credenciales inválidas
    mensaje_esperado = "Las credenciales ingresadas son incorrectas. Por favor, intente nuevamente." # Mensaje de error esperado
    mensaje_actual = login_page.obtener_mensaje_error() # Obtenemos el mensaje de error actual
    assert mensaje_esperado in mensaje_actual, f"Esperaba '{mensaje_esperado}' pero llegó '{mensaje_actual}'"
    driver.save_screenshot("screenshot_login_fallido.png") # Tomamos una captura de pantalla del resultado del login fallido
    time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
    login_page.cerrar_mensaje_error() # Cerramos el mensaje de error para limpiar la interfaz
    time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
