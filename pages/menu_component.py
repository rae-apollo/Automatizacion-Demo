from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

class MenuComponent:
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
        self.btn_mis_reservas_de_charter = (By.XPATH, "//span[contains(text(), 'Mis reservas de chárter')]") # Botón para abrir el menú de mis reservas de chárter (si existe)
        self.btn_gestion_de_servicios_charter = (By.XPATH, "//span[contains(text(), 'Gestión de servicios chárter')]") # Botón para abrir el menú de gestión de servicios chárter (si existe)
        self.btn_mi_perfil = (By.XPATH, "//span[contains(text(), 'Mi perfil')]") # Botón para abrir el menú de mi perfil (si existe)
        self.btn_gestion_de_pasajeros = (By.XPATH, "//span[contains(text(), 'Gestión de pasajeros')]") # Botón para abrir el menú de gestión de pasajeros (si existe)
        self.btn_medios_de_pago = (By.XPATH, "//span[contains(text(), 'Medios de pago')]") # Botón para abrir el menú de medios de pago (si existe)
        self.btn_soporte_telefonico = (By.XPATH, "//span[contains(text(), 'Soporte (telefónico)')]") # Botón para abrir el menú de soporte telefónico (si existe)
        self.btn_puntos_de_encuentro = (By.XPATH, "//span[contains(text(), 'Puntos de encuentro')]") # Botón para abrir el menú de puntos de encuentro (si existe)  
        self.btn_cambiar_contraseña = (By.XPATH, "//span[contains(text(), 'Cambiar contraseña')]") # Botón para abrir el menú de cambiar contraseña (si existe)
        self.btn_terminos_y_condiciones = (By.XPATH, "//span[contains(text(), 'Términos y condiciones')]") # Botón para abrir el menú de términos y condiciones (si existe) 
        self.btn_cerrar_sesion = (By.XPATH, "//span[contains(text(), 'Cerrar sesión')]") # Botón para cerrar sesión (si existe)
        self.btn_cerrar_modal_puntos = (By.XPATH, "//button[contains(@class, 'at-icon-button')]//mat-icon[text()='close']") # Botón para cerrar el modal de puntos de encuentro (si aparece)
        self.btn_aceptar_condiciones = (By.XPATH, "//button[contains(., 'ACEPTAR')]") # Botón para aceptar términos y condiciones (si aparece)
    def ir_a_nueva_reserva_de_remis(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nueva_reserva)) # Esperamos a que el botón de nueva reserva sea clickeable
        elemento.click() # Hacemos click en el botón de nueva reserva
    def ir_a_nuevo_envio(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nuevo_envio)) # Esperamos a que el botón de nuevo envío sea clickeable
        elemento.click() # Hacemos click en el botón de nuevo envío 
    def ir_a_nueva_mensajeria(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nueva_mensajeria)) # Esperamos a que el botón de nueva mensajería sea clickeable
        elemento.click() # Hacemos click en el botón de nueva mensajería
        btn_aceptar = self.wait.until(EC.presence_of_element_located(self.btn_aceptar_condiciones)) # Esperamos a que el botón de aceptar términos y condiciones sea clickeable
        self.driver.execute_script("arguments[0].click();", btn_aceptar) # Hacemos click en el botón de aceptar términos y condiciones utilizando JavaScript (esto puede ayudar a evitar problemas de elementos superpuestos o no clickeables)
        time.sleep(2) # Esperamos 2 segundos para que se procese el click en aceptar términos y condiciones (puedes ajustar este tiempo según sea necesario)
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
        time.sleep(2) # Esperamos 2 segundos para que se abra el modal de soporte telefónico (puedes ajustar este tiempo según sea necesario)
        pyautogui.press('esc') # Presionamos la tecla 'Esc' para la ventana emergente de soporte telefónico (puedes ajustar esta lógica según sea necesario)
        time.sleep(1) # Esperamos 1 segundo para asegurarnos de que el modal se haya cerrado (puedes ajustar este tiempo según sea necesario)
    def ir_a_puntos_de_encuentro(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_puntos_de_encuentro)) # Esperamos a que el botón de puntos de encuentro sea clickeable
        elemento_x = self.wait.until(EC.element_to_be_clickable(self.btn_puntos_de_encuentro)) # Esperamos a que el botón de puntos de encuentro sea clickeable
        elemento_x.click() # Hacemos click en el botón de puntos de encuentro
    def ir_a_cambiar_contraseña(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_cambiar_contraseña)) # Esperamos a que el botón de cambiar contraseña sea clickeable
        elemento.click() # Hacemos click en el botón de cambiar contraseña
    def ir_a_terminos_y_condiciones(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_terminos_y_condiciones)) # Esperamos a que el botón de términos y condiciones sea clickeable
        elemento.click() # Hacemos click en el botón de términos y condiciones
    def cerrar_sesion(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_cerrar_sesion)) # Esperamos a que el botón de cerrar sesión sea clickeable
        elemento.click() # Hacemos click en el botón de cerrar sesión para cerrar la sesión actual (puedes ajustar esta lógica según sea necesario) 
    