import time
from faker import Faker 
from pages.login_page import LoginPage 
from pages.menu_component import MenuComponent 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.reserva_page import ReservaPage    
from data.data_login import LOGIN_WEB_CLIENTES

USUARIO_VALIDO, PASSWORD_VALIDO, _= LOGIN_WEB_CLIENTES[0]

# Función de prueba para verificar la reserva de remis de punto a punto.
def test_reserva_remis_punto_a_punto(driver, record_property):
    """ CASO 1 : Reserva de remis de punto a punto"""
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    reserva_page = ReservaPage(driver) # Creamos una instancia de ReservaPage    reserva_page = ReservaPage(driver) # Creamos una instancia de ReservaPage
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO) # Iniciamos sesión con las credenciales de prueba
    menu.ir_a_nueva_reserva_de_remis() # Navegamos a la sección de nueva reserva de remis
    time.sleep(2) # Esperamos 3 segundos para que se cargue la página de reserva de remis (puedes ajustar este tiempo según sea necesario)
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

    # --- EXTRAER CÓDIGO DE RESERVA PARA EL REPORTE ---
    try:
        codigo_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'bg-green-500')]"))
        )
        codigo_reserva = codigo_element.text.strip()
        record_property("status_code", codigo_reserva)
    except Exception as e:
        record_property("status_code", "ERROR")

    time.sleep(5)
