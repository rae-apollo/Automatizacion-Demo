import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # Importamos las librerías necesarias para Selenium y WebDriver Manager
from pages.login_page import LoginPage # Importamos la clase LoginPage desde el archivo login_page.py
from pages.menu_component import MenuComponent # Importamos la clase MenuComponent desde el archivo menu_component.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reserva_page import ReservaPage # Importamos la clase ReservaPage desde el archivo reserva_page.py   

@pytest.fixture
def driver():
# Configuramos las opciones de Chrome para deshabilitar el guardado de contraseñas y otras características que puedan interferir con las pruebas
    chrome_options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
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

def test_login_clientes_traslada_web(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales("ehs@sommytech.com.ar", "123456") # Ingresamos las credenciales de prueba
    time.sleep(2) # Esperamos 2 segundos para que se procese el login (puedes ajustar este tiempo según sea necesario)
    menu.ir_a_nueva_reserva_de_remis() # Navegamos al menú de nueva reserva de remis
    reserva_page = ReservaPage(driver) # Creamos una instancia de ReservaPage
    reserva_page.seleccionar_origen("Defensa 814")
    time.sleep(3) # Seleccionamos la dirección de origen
    reserva_page.completar_piso_departamento("Piso 5 Depto Q")
    time.sleep(2) # Completamos el campo de piso y departamento (si es necesario)
    reserva_page.seleccionar_destino("Av. Belgrano 553")# Seleccionamos la dirección de destino
    time.sleep(3) # Esperamos 3 segundos para que se procesen las selecciones de origen y destino (puedes ajustar este tiempo según sea necesario)
    reserva_page.hacer_click_continuar()
    reserva_page.hacer_click_confirmar()
    WebDriverWait(driver, 10).until(EC.url_contains("booking")) # Esperamos a que la URL contenga "booking"
    except_url_part = "booking"
    assert except_url_part in driver.current_url, f"Se esperaba que la URL contenga '{except_url_part}' pero se obtuvo '{driver.current_url}'" # Verificamos que la URL contenga la parte esperada
    time.sleep(5) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)