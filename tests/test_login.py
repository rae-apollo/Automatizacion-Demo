import time
import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
fake = Faker()

credenciales_invalidas_username = fake.email() # Generamos un nombre de usuario aleatorio con Faker
credenciales_invalidas_password = fake.password() # Generamos una contraseña aleatoria con Faker
@pytest.mark.parametrize("username, password, es_exitoso", [
    ("ehs@sommytech.com.ar", "123456", True),
    (credenciales_invalidas_username, credenciales_invalidas_password, False)
])

# CASO 1 : Login exitoso y navegación a nueva reserva de remis
def test_login(driver: WebDriver, username, password, es_exitoso):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    login_page.iniciar_sesion(username, password) # Iniciamos sesión con las credenciales de prueba
    if es_exitoso:
        WebDriverWait(driver, 10).until(EC.url_contains("services")) # Esperamos a que la URL contenga "services".
        assert "services" in driver.current_url
        time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
# CASO 2 : Login fallido con credenciales inválidas    
    else:
        mensaje_esperado = "Las credenciales ingresadas son incorrectas. Por favor, intente nuevamente." # Mensaje de error esperado
        mensaje_actual = login_page.obtener_mensaje_error() # Obtenemos el mensaje de error actual
        assert mensaje_esperado in mensaje_actual, f"Esperaba '{mensaje_esperado}' pero llegó '{mensaje_actual}'"
        driver.save_screenshot("screenshot_login_fallido.png") # Tomamos una captura de pantalla del resultado del login fallido
        time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
        login_page.cerrar_mensaje_error() # Cerramos el mensaje de error para limpiar la interfaz
        time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
