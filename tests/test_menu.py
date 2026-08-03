import time
import pytest
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso_y_navegacion_a_nueva_reserva_de_remis(driver: WebDriver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    login_page.iniciar_sesion("ehs@sommytech.com.ar", "123456")
    time.sleep(2) # Esperamos 2 segundos para que se procese el login (puedes ajustar este tiempo según sea necesario)
    menu.ir_a_nueva_reserva_de_remis() # Navegamos al menú de nueva reserva de remis
    WebDriverWait(driver, 10).until(EC.url_contains("booking")) # Esperamos a que la URL contenga "booking"
    except_url_part = "booking"
    assert except_url_part in driver.current_url, f"Se esperaba que la URL contenga '{except_url_part}' pero se obtuvo '{driver.current_url}'" # Verificamos que la URL contenga la parte esperada
    driver.save_screenshot("screenshot_login_exitoso_nueva_reserva.png") # Tomamos una captura de pantalla del resultado del login exitoso
    time.sleep(2) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)

def test_recorrido_completo_del_menu_despues_de_login_exitoso(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales("ehs@sommytech.com.ar", "123456") # Ingresamos las credenciales de prueba
    WebDriverWait(driver, 10).until(EC.url_contains("services")) # Esperamos a que la URL contenga "services".
    menu.ir_a_nueva_reserva_de_remis() # Navegamos al menú de nueva reserva
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación 
    menu.ir_a_nuevo_envio() # Navegamos al menú de nuevo envío
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación 
    menu.ir_a_nueva_mensajeria() # Navegamos al menú de nueva mensajería
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación 
    menu.ir_a_reserva_de_asiento_charter() # Navegamos al menú de reserva de asiento charter
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_logistica_corporativa() # Navegamos al menú de logística corporativa
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_seguimiento_de_viajes() # Navegamos al menú de seguimiento de viajes
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_mis_reservas_de_remis() # Navegamos al menú de mis reservas de remis
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_mis_envios_mensajerias() # Navegamos al menú de mis envíos y mensajería
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_estado_de_envios() # Navegamos al menú de estado de envíos
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_mis_reservas_de_charter() # Navegamos al menú de mis reservas de chárter
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_gestion_de_servicios_charter() # Navegamos al menú de gestión de servicios chárter
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_dashboard_remis() # Navegamos al menú de dashboard remis
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_dashboard_charter() # Navegamos al menú de dashboard chárter
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_mi_perfil() # Navegamos al menú de mi perfil
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_gestion_de_pasajeros() # Navegamos al menú de gestión de pasajeros
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_medios_de_pago() # Navegamos al menú de medios de pago
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_puntos_de_encuentro()
    time.sleep(2) 
    time.sleep(1.5) # Pausa para que el modal desaparezca y limpie la pantalla antes de seguir
    menu.ir_a_cambiar_contraseña() # Navegamos al menú de cambiar contraseña
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.ir_a_terminos_y_condiciones() # Navegamos al menú de términos y condiciones
    time.sleep(2) # Esperamos 2 segundos para que se procese la navegación
    menu.cerrar_sesion() # Cerramos sesión al finalizar el recorrido del menú   