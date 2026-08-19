from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage: 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Espera explícita para manejar elementos dinámicos
        # Aqui definimos las direcciones de los elementos de la pagina auth/login.
        self.username_field = (By.XPATH, "//input[@formcontrolname='username']") # Campo de usuario
        self.password_field = (By.XPATH, "//input[@formcontrolname='password']") # Campo de password
        self.login_button = (By.XPATH, "//button[contains(., 'Ingresar')]") # Boton Ingresar
        self.recover_password_button = (By.XPATH, "//button[contains(., 'Recuperar contraseña')]") # Boton recuperar contraseña
        self.create_account_button = (By.XPATH, "//button[contains(., 'Crear cuenta')]") # Boton crear cuenta
        self.txt_mensaje_error = (By.XPATH, "//span[contains(@class, 'content-message')]") # Mensaje de error en caso de login fallido
        self.btn_cerrar_mensaje_error = (By.XPATH, "//button[contains(., 'Cerrar')]") # Botón para cerrar el mensaje de error
    def iniciar_sesion(self, username, password):
        self.driver.get("https://clientes.traslada.com.ar/auth/login") # Navegamos a la página de login
        self.ingresar_credenciales(username, password) # Ingresamos las credenciales de prueba

    def ingresar_credenciales(self, username, password):
        self.driver.find_element(*self.username_field).clear() # Limpiamos el campo de usuario
        self.driver.find_element(*self.username_field).send_keys(username) # Ingresamos el usuario
        self.driver.find_element(*self.password_field).clear() # Limpiamos el campo de password
        self.driver.find_element(*self.password_field).send_keys(password) # Ingresamos el password
        self.driver.find_element(*self.login_button).click() # Hacemos click en el boton de ingresar    
    def obtener_mensaje_error(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.txt_mensaje_error)) # Esperamos a que el mensaje de error sea visible
        return elemento.text # Retornamos el texto del mensaje de error
    def cerrar_mensaje_error(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.btn_cerrar_mensaje_error)) # Esperamos a que el botón de cerrar mensaje de error sea clickeable
        self.driver.execute_script("arguments[0].click();", elemento) # Hacemos click en el botón para cerrar el mensaje de error utilizando JavaScript (esto puede ayudar a evitar problemas de elementos superpuestos o no clickeables)
        elemento.click() # Hacemos click en el botón para cerrar el mensaje de error
