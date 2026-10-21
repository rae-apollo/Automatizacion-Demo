from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reserva_page import ReservaPage
from pages.reserva_envio_page import ReservaEnvioPage
import time

class ReservaMensajeriaPage(ReservaEnvioPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_indicacion = (By.XPATH, "//span[contains(text(), ' Indicaciones ')]") # Campo de indicaciones.
        self.btn_agregar_indicacion = (By.XPATH, "//span[contains(text(), 'Agregar indicación')]") # Botón para agregar indicacion.
        self.btn_donde_vamos = (By.XPATH, "//span[contains(text(), ' ¿Dónde vamos? ')]") # Campo de piso y departamento (puede aparecer dinámicamente dependiendo de la dirección seleccionada)
        self.input_indicacion = (By.XPATH, "//textarea[@formcontrolname='indications']") # Campo de indicaciones.

    def hacer_click_indicaciones (self):
        indicaciones = self.wait.until(EC.element_to_be_clickable(self.btn_indicacion))
        indicaciones.click() # Hacemos click en el campo de indicaciones para activar el input
        time.sleep(1) # Esperamos 1 segundo para que el input se active (puedes ajustar este tiempo según sea necesario)
    def hacer_click_agregar_indicacion(self):
        agregar_indicacion = self.wait.until(EC.element_to_be_clickable(self.btn_agregar_indicacion))
        agregar_indicacion.click() # Hacemos click en el botón de agregar indicación para abrir el formulario de indicación
        time.sleep(1) # Esperamos 1 segundo para que se abra el formulario de indicación (puedes ajustar este tiempo según sea necesario)
    def hacer_click_donde_vamos(self):
        donde_vamos = self.wait.until(EC.element_to_be_clickable(self.btn_donde_vamos))
        donde_vamos.click() # Hacemos click en el campo de piso y departamento para activar el input
        time.sleep(2) # Esperamos 1 segundo para que el input se active (puedes ajustar este tiempo según sea necesario)
    def completar_indicaciones(self, indicacion=None):
        if not indicacion:
            return
        try:
            campo_indicacion = self.wait.until(EC.element_to_be_clickable(self.input_indicacion)) # Esperamos a que el campo de indicaciones sea clickeable
            campo_indicacion.click() # Hacemos click en el campo de indicaciones para asegurarnos de que esté activo
            campo_indicacion.clear() # Limpiamos el campo de indicaciones
            campo_indicacion.send_keys(indicacion) # Ingresamos la indicación
            print(f"Indicaciones ingresadas en el campo de indicaciones: {indicacion}") # Imprimimos las indicaciones ingresadas para verificar que se hayan ingresado correctamente
        except Exception as e:
            print(f"Error al completar el campo de indicaciones: {e}")
        time.sleep(1) # Esperamos 1 segundo para que se procese la información ingresada (puedes ajustar este tiempo según sea necesario)
    def completar_datos_contacto(self, nombre, codigo_pais, codigo_area, numero_telefono):
        ## Esta función completa los datos de contacto de la persona que envia o recibe la mensajería, sin requerir el DNI.
        return self.completar_datos_destinatario(
            nombre=nombre, 
            codigo_pais=codigo_pais, 
            codigo_area=codigo_area, 
            numero_telefono=numero_telefono,
            dni=None  # DNI no es obligatorio para la mensajería, por lo que se establece como None
            )
