import time
import pytest
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.data_login import LOGIN_WEB_CLIENTES

# Extraemos las credenciales válidas del primer conjunto de datos de LOGIN_WEB_CLIENTES. 
USUARIO_VALIDO, PASSWORD_VALIDO, _= LOGIN_WEB_CLIENTES[0]

# Función de prueba para verificar el login exitoso y la navegación a la nueva reserva de remis.
def test_login_exitoso_y_navegacion_a_nueva_reserva_de_remis(driver: WebDriver):
    """CASO 1 : Login exitoso y navegación a nueva reserva de remis."""
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO) # Iniciamos sesión con las credenciales válidas
    time.sleep(2) # Esperamos 2 segundos para que se procese el login (puedes ajustar este tiempo según sea necesario)
    menu.ir_a_nueva_reserva_de_remis() # Navegamos al menú de nueva reserva de remis
    WebDriverWait(driver, 10).until(EC.url_contains("booking")) # Esperamos a que la URL contenga "booking"
    except_url_part = "booking"
    assert except_url_part in driver.current_url, f"Se esperaba que la URL contenga '{except_url_part}' pero se obtuvo '{driver.current_url}'" # Verificamos que la URL contenga la parte esperada
    driver.save_screenshot("screenshot_login_exitoso_nueva_reserva.png") # Tomamos una captura de pantalla del resultado del login exitoso
    time.sleep(2) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)

# Función de prueba para verificar el recorrido completo del menú después de un login exitoso.
def test_recorrido_completo_del_menu_despues_de_login_exitoso(driver):
    """CASO 2 : Recorrido completo del menú después de un login exitoso."""
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO) # Iniciamos sesión con las credenciales válidas
    WebDriverWait(driver, 10).until(EC.url_contains("services")) # Esperamos a que la URL contenga "services".
    acciones_menu = [
        menu.ir_a_nueva_reserva_de_remis,
        menu.ir_a_nuevo_envio,
        menu.ir_a_nueva_mensajeria,
        menu.ir_a_reserva_de_asiento_charter,
        menu.ir_a_logistica_corporativa,
        menu.ir_a_seguimiento_de_viajes,
        menu.ir_a_mis_reservas_de_remis,
        menu.ir_a_mis_envios_mensajerias,
        menu.ir_a_estado_de_envios,
        menu.ir_a_mis_reservas_de_charter,
        menu.ir_a_gestion_de_servicios_charter,
        menu.ir_a_dashboard_remis,
        menu.ir_a_dashboard_charter,
        menu.ir_a_mi_perfil,
        menu.ir_a_gestion_de_pasajeros,
        menu.ir_a_medios_de_pago,
        menu.ir_a_puntos_de_encuentro,
        menu.ir_a_cambiar_contraseña,
        menu.ir_a_terminos_y_condiciones,
        menu.cerrar_sesion
    ]
    for accion in acciones_menu:
        accion() # Ejecutamos la acción del menú
        time.sleep(2) # Esperamos 2 segundos para que se procese la navegación