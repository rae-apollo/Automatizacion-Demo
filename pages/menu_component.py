from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

import pyautogui
import time
# Esta clase representa el componente del menú lateral de la aplicación, proporcionando métodos para interactuar con cada opción del menú. Cada método espera a que el botón correspondiente sea clickeable antes de hacer clic en él, lo que ayuda a garantizar que la interacción sea exitosa incluso si los elementos tardan en cargarse o si hay elementos superpuestos.
class MenuComponent:
    # Inicializamos la clase con el driver de Selenium y definimos los localizadores para cada botón del menú utilizando XPath. 
    # También configuramos una espera explícita para manejar elementos dinámicos en la página.    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Espera explícita para manejar elementos dinámicos
        self.btn_nueva_reserva = (By.XPATH, "//span[contains(text(), 'Nueva reserva de remis')]") # Botón para abrir el menú de nueva reserva
        self.btn_nuevo_envio = (By.XPATH, "//span[contains(text(), 'Nuevo envío')]") # Botón para abrir el menú de nuevo envío
        self.btn_nueva_mensajeria = (By.XPATH, "//span[contains(text(), 'Nueva mensajería')]") # Botón para abrir el menú de nueva mensajería (si existe)
        self.btn_reserva_de_asiento_charter = (By.XPATH, "//span[contains(text(), 'Reserva de asiento (Chárter)')]") # Botón para abrir el menú de reserva de asiento charter (si existe)    
        self.btn_logistica_corporativa = (By.XPATH, "//span[contains(text(), 'Logística corporativa')]") # Botón para abrir el menú de logística corporativa (si existe)
        self.btn_seguimiento_de_viajes = (By.XPATH, "//span[contains(text(), 'Seguimiento de viajes')]") # Botón para abrir el menú de seguimiento de viajes (si existe)
        self.btn_mis_reservas_de_remis = (By.XPATH, "//span[contains(text(), 'Mis reservas de remis')]") # Botón para abrir el menú de mis reservas de remis (si existe)
        self.btn_mis_envios_mensajerias = (By.XPATH, "//span[contains(text(), ' Mis envíos / Mensajería')]") # Botón para abrir el menú de mis envíos y mensajería (si existe)
        self.btn_estado_de_envios = (By.XPATH, "//span[contains(text(), 'Estado de envíos')]") # Botón para abrir el menú de estado de envíos (si existe)
        self.btn_mis_reservas_de_charter = (By.XPATH, "//span[contains(text(), ' Mis reservas de Chárter ')]") # Botón para abrir el menú de mis reservas de chárter (si existe)
        self.btn_gestion_de_servicios_charter = (By.XPATH, "//span[contains(text(), ' Gestión de servicio Chárter ')]") # Botón para abrir el menú de gestión de servicios chárter (si existe)
        self.btn_dashboard_remis = (By.XPATH, "//span[contains(text(), ' Dashboard Remis ')]") # Botón para abrir el menú de dashboard remis (si existe)
        self.btn_dashboard_charter = (By.XPATH, "//span[contains(text(), ' Dashboard Chárter ')]") # Botón para abrir el menú de dashboard envíos (si existe)
        self.btn_mi_perfil = (By.XPATH, "//span[contains(text(), 'Mi perfil')]") # Botón para abrir el menú de mi perfil (si existe)
        self.btn_gestion_de_pasajeros = (By.XPATH, "//span[contains(text(), 'Gestión de pasajeros')]") # Botón para abrir el menú de gestión de pasajeros (si existe)
        self.btn_medios_de_pago = (By.XPATH, "//span[contains(text(), 'Medios de pago')]") # Botón para abrir el menú de medios de pago (si existe)
        self.btn_soporte_telefonico = (By.XPATH, "//span[contains(text(), 'Soporte (telefónico)')]") # Botón para abrir el menú de soporte telefónico (si existe)
        self.btn_puntos_de_encuentro = (By.XPATH, "//span[contains(text(), 'Puntos de encuentro')]") # Botón para abrir el menú de puntos de encuentro (si existe)  
        self.btn_cambiar_contraseña = (By.XPATH, "//span[contains(text(), 'Cambiar contraseña')]") # Botón para abrir el menú de cambiar contraseña (si existe)
        self.btn_terminos_y_condiciones = (By.XPATH, "//span[contains(text(), 'Términos y condiciones')]") # Botón para abrir el menú de términos y condiciones (si existe) 
        self.btn_cerrar_sesion = (By.XPATH, "//span[contains(text(), 'Cerrar sesión')]") # Botón para cerrar sesión (si existe)
        # Apuntamos directo al BOTÓN padre que está dentro del contenedor del diálogo de puntos de encuentro
        self.btn_cerrar_modal_puntos = (By.XPATH, "//cli-meeting-points//button[contains(@class, 'mat-mdc-icon-button')]")
        self.btn_aceptar_condiciones = (By.XPATH, "//button[.//span[text()='ACEPTAR' or normalize-space(text())='ACEPTAR']]")
    def ir_a_nueva_reserva_de_remis(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nueva_reserva)) # Esperamos a que el botón de nueva reserva sea clickeable
        elemento.click() # Hacemos click en el botón de nueva reserva
    def ir_a_nuevo_envio(self):
        btn_envio = self.wait.until(EC.element_to_be_clickable(self.btn_nuevo_envio))
        btn_envio.click()
        btn_aceptar = self.wait.until(EC.visibility_of_element_located(self.btn_aceptar_condiciones))
        time.sleep(1)
        ActionChains(self.driver).move_to_element(btn_aceptar).click().perform()
        self.wait.until(EC.invisibility_of_element_located(self.btn_aceptar_condiciones))
        time.sleep(2)
    def ir_a_nueva_mensajeria(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nueva_mensajeria)) # Esperamos a que el botón de nueva mensajería sea clickeable
        elemento.click() # Hacemos click en el botón de nueva mensajería
    def ir_a_reserva_de_asiento_charter(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_reserva_de_asiento_charter)) # Esperamos a que el botón de reserva de asiento charter sea clickeable
        elemento.click() # Hacemos click en el botón de reserva de asiento charter
    def ir_a_logistica_corporativa(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_logistica_corporativa)) # Esperamos a que el botón de logística corporativa sea clickeable
        elemento.click() # Hacemos click en el botón de logística corporativa
    def ir_a_seguimiento_de_viajes(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_seguimiento_de_viajes)) # Esperamos a que el botón de seguimiento de viajes sea clickeable
        elemento.click() # Hacemos click en el botón de seguimiento de viajes
    def ir_a_mis_reservas_de_remis(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_mis_reservas_de_remis)) # Esperamos a que el botón de mis reservas de remis sea clickeable
        elemento.click() # Hacemos click en el botón de mis reservas de remis
    def ir_a_mis_envios_mensajerias(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_mis_envios_mensajerias)) # Esperamos a que el botón de mis envíos y mensajería sea clickeable
        elemento.click() # Hacemos click en el botón de mis envíos y mensajería
    def ir_a_estado_de_envios(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_estado_de_envios)) # Esperamos a que el botón de estado de envíos sea clickeable
        elemento.click() # Hacemos click en el botón de estado de envíos
    def ir_a_mis_reservas_de_charter(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_mis_reservas_de_charter)) # Esperamos a que el botón de mis reservas de chárter sea clickeable
        elemento.click() # Hacemos click en el botón de mis reservas de chárter
    def ir_a_gestion_de_servicios_charter(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_gestion_de_servicios_charter)) # Esperamos a que el botón de gestión de servicios chárter sea clickeable
        elemento.click() # Hacemos click en el botón de gestión de servicios chárter
    def ir_a_dashboard_remis(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_dashboard_remis)) # Esperamos a que el botón de dashboard remis sea clickeable
        elemento.click() # Hacemos click en el botón de dashboard remis
    def ir_a_dashboard_charter(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_dashboard_charter)) # Esperamos a que el botón de dashboard chárter sea clickeable
        elemento.click() # Hacemos click en el botón de dashboard chárter
    def ir_a_mi_perfil(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_mi_perfil)) # Esperamos a que el botón de mi perfil sea clickeable
        elemento.click() # Hacemos click en el botón de mi perfil
    def ir_a_gestion_de_pasajeros(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_gestion_de_pasajeros)) # Esperamos a que el botón de gestión de pasajeros sea clickeable
        elemento.click() # Hacemos click en el botón de gestión de pasajeros
    def ir_a_medios_de_pago(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_medios_de_pago)) # Esperamos a que el botón de medios de pago sea clickeable
        elemento.click() # Hacemos click en el botón de medios de pago
    def ir_a_soporte_telefonico(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_soporte_telefonico)) # Esperamos a que el botón de soporte telefónico sea clickeable
        elemento.click() # Hacemos click en el botón de soporte telefónico
        time.sleep(2) # Esperamos 2 segundos para que se abra el modal de soporte telefónico
        pyautogui.press('esc') # Presionamos la tecla 'Esc' para la ventana emergente de soporte telefónico
        time.sleep(1) # Esperamos 1 segundo para asegurarnos de que el modal se haya cerrado
    def ir_a_puntos_de_encuentro(self):
        btn_abrir = self.wait.until(EC.visibility_of_element_located(self.btn_puntos_de_encuentro))
        self.driver.execute_script("arguments[0].click();", btn_abrir)
        time.sleep(2.5) # Damos tiempo suficiente para que el modal termine de animarse y abrirse por completo
        
        # Esperamos a que el BOTÓN sea clickeable
        btn_cerrar = self.wait.until(EC.element_to_be_clickable(self.btn_cerrar_modal_puntos))
        # Hacemos el clic forzado mediante JavaScript en el botón contenedor
        self.driver.execute_script("arguments[0].click();", btn_cerrar)
        time.sleep(3) # Pausa extendida para garantizar que Angular destruya el backdrop (fondo oscuro)
    def ir_a_cambiar_contraseña(self):
        time.sleep(1) 
        # Esperamos a que el elemento esté presente en el DOM
        elemento = self.wait.until(EC.presence_of_element_located(self.btn_cambiar_contraseña))
        # Forzamos el clic con JS para evadir cualquier remanente transparente del modal de puntos de encuentro
        self.driver.execute_script("arguments[0].click();", elemento)

    def ir_a_terminos_y_condiciones(self):
        pestana_menu_principal = self.driver.current_window_handle
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_terminos_y_condiciones))
        self.driver.execute_script("arguments[0].click();", elemento)
        self.wait.until(EC.number_of_windows_to_be(2))
        todas_las_pestanas = self.driver.window_handles
        nueva_pestana = [p for p in todas_las_pestanas if p != pestana_menu_principal][0]        
        self.driver.switch_to.window(nueva_pestana)
        time.sleep(1.5)
        self.driver.close()
        self.driver.switch_to.window(pestana_menu_principal)
        elemento_menu = self.wait.until(EC.visibility_of_element_located(self.btn_terminos_y_condiciones))
        ActionChains(self.driver).move_to_element(elemento_menu).perform()
        time.sleep(1)
    def cerrar_sesion(self):
        time.sleep(1)
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_cerrar_sesion))
        self.driver.execute_script("arguments[0].click();", elemento)
        time.sleep(2) # Esperamos 2 segundos para que se procese el cierre de sesión