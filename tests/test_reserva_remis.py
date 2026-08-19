import time
from faker import Faker 
from pages.login_page import LoginPage 
from pages.menu_component import MenuComponent 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reserva_page import ReservaPage    
fake = Faker()


def test_reserva_remis_punto_a_punto(driver):
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
    driver.save_screenshot("screenshot_reserva_exitosa.png") # Tomamos una captura de pantalla del resultado de la reserva exitosa
    assert except_url_part in driver.current_url, f"Se esperaba que la URL contenga '{except_url_part}' pero se obtuvo '{driver.current_url}'" # Verificamos que la URL contenga la parte esperada
    time.sleep(5) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
