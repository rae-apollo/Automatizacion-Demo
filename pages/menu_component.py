from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Espera explícita para manejar elementos dinámicos

        self.btn_nueva_reserva = (By.XPATH, "//span[contains(text(), 'Nueva reserva de remis')]") # Botón para abrir el menú de nueva reserva
        self.btn_nuevo_envio = (By.XPATH, "//span[contains(text(), 'Nuevo envío')]") # Botón para abrir el menú de nuevo envío
    def ir_a_nueva_reserva_de_remis(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nueva_reserva)) # Esperamos a que el botón de nueva reserva sea clickeable
        elemento.click() # Hacemos click en el botón de nueva reserva
    def ir_a_nuevo_envio(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_nuevo_envio)) # Esperamos a que el botón de nuevo envío sea clickeable
        elemento.click() # Hacemos click en el botón de nuevo envío 
