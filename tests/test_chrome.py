import pytest
import time
import pyautogui
from faker import Faker 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from pages.login_page import LoginPage 
from pages.menu_component import MenuComponent 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reserva_page import ReservaPage    

fake = Faker()

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
# CASO 1 : Login fallido con credenciales aleatorias generadas por Faker
def test_login_fallido_con_faker(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    user_random = fake.email() # Generamos un nombre de usuario aleatorio con Faker
    password_random = fake.password() # Generamos una contraseña aleatoria con Faker
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales(user_random, password_random) # Ingresamos las credenciales aleatorias
    mensaje_esperado = "Las credenciales ingresadas son incorrectas. Por favor, intente nuevamente." # Mensaje de error esperado
    mensaje_actual = login_page.obtener_mensaje_error() # Obtenemos el mensaje de error actual
    assert mensaje_esperado in mensaje_actual, f"Esperaba '{mensaje_esperado}' pero llegó '{mensaje_actual}'"
    time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)
    login_page.cerrar_mensaje_error() # Cerramos el mensaje de error para limpiar la interfaz
    time.sleep(2) # Esperamos 2 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)

# CASO 2 : Login exitoso con credenciales válidas y navegación a la sección de nueva reserva de remis
def test_login_exitoso_y_navegacion_a_nueva_reserva_de_remis(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales("ehs@sommytech.com.ar", "123456") # Ingresamos las credenciales de prueba
    time.sleep(2) # Esperamos 2 segundos para que se procese el login (puedes ajustar este tiempo según sea necesario)
    menu.ir_a_nueva_reserva_de_remis() # Navegamos al menú de nueva reserva de remis
    WebDriverWait(driver, 10).until(EC.url_contains("booking")) # Esperamos a que la URL contenga "booking"
    except_url_part = "booking"
    assert except_url_part in driver.current_url, f"Se esperaba que la URL contenga '{except_url_part}' pero se obtuvo '{driver.current_url}'" # Verificamos que la URL contenga la parte esperada
    time.sleep(5) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesario)    
 
 # CASO 3 : Recorrido completo del menu de cliente después de un login exitoso
def test_recorrido_completo_del_menu_despues_de_login_exitoso(driver):
    login_page = LoginPage(driver) # Creamos una instancia de LoginPage
    menu = MenuComponent(driver) # Creamos una instancia de MenuComponent
    driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
    login_page.ingresar_credenciales("ehs@sommytech.com.ar", "123456") # Ingresamos las credenciales de prueba
    WebDriverWait(driver, 10).until(lambda d: "services" in d.current_url or "booking" in d.current_url) # Esperamos a que la URL contenga "services" o "booking"
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
    time.sleep(5) # Esperamos 5 segundos para observar el resultado (puedes ajustar este tiempo según sea necesar