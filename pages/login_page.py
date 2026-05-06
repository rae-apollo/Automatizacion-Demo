from selenium.webdriver.common.by import By

class LoginPage: 
    def __init__(self, driver):
        self.driver = driver
        # Aqui definimos las direcciones de los elementos.
        self.username_field = (By.XPATH, "//input[@formcontrolname='username']") # Campo de usuario
        self.password_field = (By.XPATH, "//input[@formcontrolname='password']") # Campo de password
        self.login_button = (By.XPATH, "//button[contains(., 'Ingresar')]") # Boton Ingresar
    def ingresar_credenciales(self, username, password):
        self.driver.find_element(*self.username_field).clear() # Limpiamos el campo de usuario
        self.driver.find_element(*self.username_field).send_keys(username) # Ingresamos el usuario
        self.driver.find_element(*self.password_field).clear() # Limpiamos el campo de password
        self.driver.find_element(*self.password_field).send_keys(password) # Ingresamos el password
        self.driver.find_element(*self.login_button).click() # Hacemos click en el boton de ingresar
    
