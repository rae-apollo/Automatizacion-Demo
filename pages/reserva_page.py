from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

class ReservaPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Espera explícita para manejar elementos dinámicos
        self.btn_origen = (By.XPATH, "//span[contains(text(), '¿Dónde vamos a buscarte?')]") # Campo de origen
        self.origen_input = (By.XPATH, "//span[@placeholder='escriba una dirección, hotel o aeropuerto.']") # Input de origen
        self.input_piso_depto = (By.XPATH, "//input[@formcontrolname='apartment']") # Campo de piso y departamento (puede aparecer dinámicamente dependiendo de la dirección seleccionada)
        self.btn_destino = (By.XPATH, "//span[contains(text(), '¿A dónde querés ir?')]") # Campo de destino
        self.btn_continuar = (By.XPATH, "//button//span[contains(text(), 'Continuar')]")
        self.btn_confirmar = (By.XPATH, "//button//span[contains(text(), 'Confirmar')]") # Botón de confirmar para avanzar al siguiente paso del proceso de reserva
    def seleccionar_origen(self, direccion):
        activador = self.wait.until(EC.element_to_be_clickable(self.btn_origen))
        activador.click() # Hacemos click en el campo de origen para activar el input
        time.sleep(1) # Esperamos 1 segundo para que el input se active (puedes ajustar este tiempo según sea necesario)    
        input_origen = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'dirección')]")))
        input_origen.click() # Hacemos click en el input de origen para asegurarnos de que esté activo
        input_origen.clear() # Limpiamos el input de origen
        for letra in direccion:
            input_origen.send_keys(letra) # Ingresamos la dirección letra por letra para simular la escritura humana
            time.sleep(0.1) # Esperamos 0.1 segundos entre cada letra para que se carguen las sugerencias (puedes ajustar este tiempo según sea necesario)
        time.sleep(2) # Esperamos 2 segundos para que se carguen las sugerencias (puedes ajustar este tiempo según sea necesario)
        xpath_sugerencia = f"//div[contains(@class, 'cursor-pointer')]//span[contains(text(), '{direccion}')]" # XPath dinámico para encontrar la sugerencia que contiene la dirección ingresada
        try:
            sugerencia = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_sugerencia))) # Esperamos a que la sugerencia que coincide con la dirección ingresada sea visible
            sugerencia.click() # Hacemos click en la sugerencia que coincide con la dirección ingresada
        except:
            input_origen.send_keys(Keys.ARROW_DOWN)# Si no se encuentra la sugerencia, presionamos Enter para seleccionar la primera opción (puedes ajustar esta lógica según sea necesario)       
            time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
            input_origen.send_keys(Keys.ENTER) # Presionamos Enter para seleccionar la primera opción (puedes ajustar esta lógica según sea necesario)
        print(f"Dirección de origen seleccionada: {direccion}") # Imprimimos la dirección seleccionada para verificar que se haya seleccionado correctamente
    def completar_piso_departamento(self, info_adicional=None):
        if not info_adicional:
            print("No se proporciono información adicional, o se omite el campo de piso y departamento.")# Si no se proporciona información adicional, o se omite el campo de piso y departamento, simplemente no hacemos nada y continuamos con el proceso de reserva
            return
        try: 
            espera_corta = WebDriverWait(self.driver, 5) # Espera corta para verificar si aparece el campo de piso y departamento
            campo = espera_corta.until(EC.visibility_of_element_located(self.input_piso_depto)) # Verificamos si aparece el campo de piso y departamento
            self.driver.execute_script("arguments[0].scrollIntoView(true);", campo) # Hacemos scroll hasta el campo de piso y departamento para asegurarnos de que esté visible
            campo.clear() # Limpiamos el campo de piso y departamento
            campo.send_keys(info_adicional) # Ingresamos la información adicional en el campo de piso y departamento
            print(f"Información adicional ingresada en el campo de piso y departamento: {info_adicional}") # Imprimimos la información adicional ingresada para verificar que se haya ingresado correctamente
        except:
            print("El campo de piso y departamento no apareció, se omite este paso.") # Si el campo de piso y departamento no aparece, simplemente imprimimos un mensaje indicando que se omite este paso y continuamos con el proceso de reserva
    def seleccionar_destino(self, direccion):
        try:
            # 1. Abrir el buscador (click en el campo de destino inicial)
            activador = self.wait.until(EC.element_to_be_clickable(self.btn_destino))
            activador.click()
            time.sleep(1) 
            
            # 2. Localizar y preparar el input real de escritura
            input_destino = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'dirección')]")))
            input_destino.click()
            input_destino.clear()
            
            # 3. Simular escritura humana letra por letra
            for letra in direccion:
                input_destino.send_keys(letra)
                time.sleep(0.1)
            
            # Espera generosa para que Google devuelva los resultados
            print(f"Esperando sugerencias para: {direccion}")
            time.sleep(3) 

            # 4. Intentar seleccionar la sugerencia mediante XPath flexible
            # Filtramos para que contenga parte de la dirección y NO sea 'A disposición'
            texto_busqueda = direccion[:10]
            xpath_sugerencia = f"//div[contains(@class, 'cursor-pointer') and contains(., '{texto_busqueda}') and not(contains(., 'disposición'))]"
            
            try:
                # Intentamos click directo en el elemento de la lista
                sugerencia = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_sugerencia)))
                sugerencia.click()
                print(f"Destino '{direccion}' seleccionado mediante click en lista.")
            except Exception:
                # Si el XPath falla (por cambios en el DOM), usamos el teclado como backup
                print("No se encontró la sugerencia por XPath, forzando selección por teclado...")
                input_destino.click() # Aseguramos foco
                time.sleep(0.5)
                input_destino.send_keys(Keys.ARROW_DOWN) # Baja a 'A disposición'
                time.sleep(0.5)
                input_destino.send_keys(Keys.ARROW_DOWN) # Baja a la primera sugerencia real
                time.sleep(0.5)
                input_destino.send_keys(Keys.ENTER)
                print(f"Destino '{direccion}' seleccionado mediante teclado.")

            # 5. CLICK EN CONTINUAR (Paso final para que el test avance)
            time.sleep(2)
        except Exception as e:
            print(f"Error crítico en seleccionar_destino: {e}")
    def hacer_click_continuar(self):
        try:
            print("Buscando botón de continuar...")
            boton_continuar = self.wait.until(EC.element_to_be_clickable(self.btn_continuar))
            boton = boton_continuar.find_element(By.XPATH, "./..") # Subimos al botón padre
            self.driver.execute_script("arguments[0].click();", boton) # Hacemos scroll hasta el botón de continuar para asegurarnos de que esté visible
            print("Haciendo click en Continuar...")
            time.sleep(2) # Esperamos 2 segundos para que se procese el click (puedes ajustar este tiempo según sea necesario)
        except Exception as e:
            print(f"Error al hacer click en Continuar: {e}")
    def hacer_click_confirmar(self):
        try:
            print("Buscando botón de confirmar...")
            boton_confirmar = self.wait.until(EC.element_to_be_clickable(self.btn_confirmar))
            texto_boton = boton_confirmar.text
            print(f"Texto del botón encontrado: '{texto_boton}'")
            self.driver.execute_script("arguments[0].click();", boton_confirmar) # Hacemos scroll hasta el botón de confirmar para asegurarnos de que esté visible
            print("Haciendo click en Confirmar...")
            time.sleep(2) # Esperamos 2 segundos para que se procese el click (puedes ajustar este tiempo según sea necesario)
        except Exception as e:
            print(f"Error al hacer click en Confirmar: {e}")