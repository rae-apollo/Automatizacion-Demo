import pytest
from faker import Faker
from pages.login_page import LoginPage
from selenium import webdriver

fake = Faker()

@pytest.fixture
def driver():
    driver = webdriver.Chrome() # Asegúrate de tener el controlador de Chrome en tu PATH o especifica la ruta completa
    yield driver
    driver.quit() # Cerramos el navegador al finalizar la prueba

#Caso 1 : Login exitoso con credenciales válidas
def test_login_exitoso(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales("ehs@sommytech.com.ar", "123456") # Ingresamos las credenciales de prueba
    # Aquí podrías agregar una verificación para asegurarte de que el login fue exitoso, como verificar la URL o la presencia de un elemento específico en la página después del login
    assert "services" in driver.current_url

    