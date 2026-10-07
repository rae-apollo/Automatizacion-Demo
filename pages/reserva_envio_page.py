from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reserva_page import ReservaPage
import time

class ReservaEnvioPage (ReservaPage):
    # Funcion con los elementos y metodos especificos para la reserva de envio, hereda de ReservaPage para reutilizar los metodos de seleccion de origen y destino, y completar piso y departamento.
    def __init__(self, driver):
        super().__init__(driver)  # Llamamos al constructor de la clase base ReservaPage
        self.btn_direccion_retiro = (By.XPATH, "//span[contains(text(), ' ¿Dónde lo vamos a retirar? ')]") # Campo de dirección de retiro
        self.btn_detalle_del_envio = (By.XPATH, "//span[contains(text(), ' Detalle del envío/s ')]") # Boton para abrir el detalle del envío
        self.btn_agregar_envio = (By.XPATH, "//span[contains(text(), 'Agregar')]") # Botón para agregar un nuevo envío
        # Se cambia el nombre del campo de destino para reflejar que es la dirección de entrega del envío
        self.btn_destino = (By.XPATH, "//span[contains(text(), ' ¿Dónde lo entregamos? ')]") # Campo de destino
        self.entrega_input = (By.XPATH, "//span[@placeholder='escriba una dirección, hotel o aeropuerto.']") # Input de destino
        self.btn_piso_depto_entrega = (By.XPATH, "//input[@formcontrolname='apartment']") # Campo de piso y departamento para la entrega (puede aparecer dinámicamente dependiendo de la dirección seleccionada)
        self.btn_paquete = (By.XPATH, "//span[contains(text(), 'Paquete')]") # Botón para seleccionar el tipo de envío como paquete
        self.btn_sobre = (By.XPATH, "//span[contains(text(), 'Sobre (documentación)')]") # Botón para seleccionar el tipo de envío como sobre
        self.input_alto_cm_paquete = (By.XPATH, "//input[@formcontrolname='height']") # Input para el alto del paquete en cm
        self.input_ancho_cm_paquete = (By.XPATH, "//input[@formcontrolname='width']") # Input para el ancho del paquete en cm
        self.input_largo_cm_paquete = (By.XPATH, "//input[@formcontrolname='depth']") # Input para el largo del paquete en cm
        self.input_peso_kg_paquete = (By.XPATH, "//input[@formcontrolname='weight']") # Input para el peso del paquete en kg
        self.checkbox_asegurar_envio = (By.XPATH, "//mat-checkbox[@formcontrolname='isDeclaredValue']") # Checkbox para asegurar el envío
        self.input_valor_declarado = (By.XPATH, "//input[@formcontrolname='insurance']") # Input para el valor declarado del envío
        self.input_cantidad_paquetes = (By.XPATH, "//input[@formcontrolname='packagesNumber']") # Input para la cantidad de paquetes
        self.input_tipo_de_contenido_paquete = (By.XPATH, "//input[@formcontrolname='description']") # Input para el tipo de contenido del envío
        self.input_quien_recibe_el_paquete = (By.XPATH, "//input[@formcontrolname='recipientName']") # Input para el nombre de la persona que recibe el paquete
        self.input_dni_recibe_paquete = (By.XPATH, "//input[@formcontrolname='recipientIdentificationNumber']") # Input para el DNI de la persona que recibe el paquete
        self.input_cpais_telefono = (By.XPATH, "//input[@formcontrolname='countryCode']") # Input ingresar el codigo de pais para el numero de teléfono del destinatario o persona que recibe el paquete.
        self.input_carea_telefono = (By.XPATH, "//input[@formcontrolname='areaCode']") # Input para el número de teléfono del destinatario o persona que recibe el paquete.
        self.input_numero_telefono = (By.XPATH, "//input[@formcontrolname='mobile']") # Input para el número de teléfono del destinatario o persona que recibe el paquete.
        # Campo para sobre (documentación)
        self.input_tipo_de_contenido_sobre = (By.XPATH, "//input[@formcontrolname='description']") # Input para el tipo de contenido del sobre
        # TODO : Agregar Opciones , Requerimientos de firmas , centro de costos, Medio de pago, observaciones, etc. (dependiendo de la complejidad del flujo de reserva de envío)
    
    # Funcon que selecciona la dirección de retiro, similar a la función seleccionar_origen pero con el campo de dirección de retiro.
    def seleccionar_direccion_retiro(self, direccion):
        activador = self.wait.until(EC.element_to_be_clickable(self.btn_direccion_retiro))
        activador.click() # Hacemos click en el campo de dirección de retiro para activar el input
        time.sleep(1) # Esperamos 1 segundo para que el input se active (puedes ajustar este tiempo según sea necesario)    
        input_retiro = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'dirección')]")))
        input_retiro.click() # Hacemos click en el input de dirección de retiro para asegurarnos de que esté activo
        input_retiro.clear() # Limpiamos el input de dirección de retiro
        for letra in direccion:
            input_retiro.send_keys(letra) # Ingresamos la dirección letra por letra para simular la escritura humana
            time.sleep(0.1) # Esperamos 0.1 segundos entre cada letra para que se carguen las sugerencias (puedes ajustar este tiempo según sea necesario)
        time.sleep(2) # Esperamos 2 segundos para que se carguen las sugerencias (puedes ajustar este tiempo según sea necesario)
        xpath_sugerencia = f"//div[contains(@class, 'cursor-pointer')]//span[contains(text(), '{direccion}')]" # XPath dinámico para encontrar la sugerencia que contiene la dirección ingresada
        try:
            sugerencia = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_sugerencia))) # Esperamos a que la sugerencia que coincide con la dirección ingresada sea visible
            sugerencia.click() # Hacemos click en la sugerencia que coincide con la dirección ingresada
        except:
            input_retiro.send_keys(Keys.ARROW_DOWN)# Si no se encuentra la sugerencia, presionamos Enter para seleccionar la primera opción (puedes ajustar esta lógica según sea necesario)       
            time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
            input_retiro.send_keys(Keys.ENTER) # Presionamos Enter para seleccionar la primera opción (puedes ajustar esta lógica según sea necesario)
        print(f"Dirección de retiro seleccionada: {direccion}") # Imprimimos la dirección seleccionada para verificar que se haya seleccionado correctamente
    # Función que hace click en el botón de detalle del envío para abrir el formulario de envío.
    def hacer_click_detalle_envio(self):
        detalle_envio = self.wait.until(EC.element_to_be_clickable(self.btn_detalle_del_envio))
        detalle_envio.click() # Hacemos click en el botón de detalle del envío para abrir el formulario de envío
        time.sleep(1) # Esperamos 1 segundo para que se abra el formulario de envío (puedes ajustar este tiempo según sea necesario)
    # Función que hace click en el botón de agregar envío para abrir el formulario de envío.
    def hacer_click_agregar_envio(self):
        agregar_envio = self.wait.until(EC.element_to_be_clickable(self.btn_agregar_envio))
        agregar_envio.click() # Hacemos click en el botón de agregar envío para abrir el formulario de envío
        time.sleep(1) # Esperamos 1 segundo para que se abra el formulario de envío (puedes ajustar este tiempo según sea necesario)
    # Función que completa los detalles del paquete como dimensiones, peso, cantidad de paquetes, tipo de contenido y valor declarado (si aplica)
    def hacer_click_paquete(self):
        paquete = self.wait.until(EC.element_to_be_clickable(self.btn_paquete))
        paquete.click() # Hacemos click en el botón de paquete para seleccionar el tipo de envío como paquete
        time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
    def hacer_click_sobre(self):
        sobre = self.wait.until(EC.element_to_be_clickable(self.btn_sobre))
        sobre.click() # Hacemos click en el botón de sobre para seleccionar el tipo de envío como sobre
        time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
    def completar_detalles_paquete(self, alto_cm, ancho_cm, largo_cm, peso_kg, cantidad_paquetes, tipo_contenido = None, asegurar_envio = False, valor_declarado = None):
        # Completar los detalles del paquete como dimensiones, peso, cantidad de paquetes, tipo de contenido y valor declarado (si aplica)
        self.wait.until(EC.element_to_be_clickable(self.btn_paquete)).click() # Seleccionamos el tipo de envío como paquete
        time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
        self.wait.until(EC.visibility_of_element_located(self.input_alto_cm_paquete)).send_keys(alto_cm) # Ingresamos el alto del paquete en cm
        time.sleep(0.5) # Esperamos 0.5 segundos para que se procese la información (puedes ajustar este tiempo según sea necesario)
        self.wait.until(EC.visibility_of_element_located(self.input_ancho_cm_paquete)).send_keys(ancho_cm) # Ingresamos el ancho del paquete en cm
        time.sleep(0.5) # Esperamos 0.5 segundos para que se procese la información (puedes ajustar este tiempo según sea necesario)
        self.wait.until(EC.visibility_of_element_located(self.input_largo_cm_paquete)).send_keys(largo_cm) # Ingresamos el largo del paquete en cm
        time.sleep(0.5) # Esperamos 0.5 segundos para que se procese la información (puedes ajustar este tiempo según sea necesario)
        self.wait.until(EC.visibility_of_element_located(self.input_peso_kg_paquete)).send_keys(peso_kg) # Ingresamos el peso del paquete en kg
        time.sleep(0.5) # Esperamos 0.5 segundos para que se procese la información (puedes ajustar este tiempo según sea necesario)
        # 3. Asegurar envío y valor declarado
        if asegurar_envio:
        # Hacemos click UNA SOLA VEZ para activar el seguro
            self.wait.until(EC.element_to_be_clickable(self.checkbox_asegurar_envio)).click() #[cite: 16]
            time.sleep(0.5)  # Breve pausa para que Angular habilite el input

        if valor_declarado:
            # Esperamos a que el input sea visible e interactuable
            input_valor = self.wait.until(EC.element_to_be_clickable(self.input_valor_declarado)) #[cite: 16]
            input_valor.clear()
            input_valor.send_keys(str(valor_declarado)) #[cite: 16]
            time.sleep(0.5)
        # Cantidad de paquetes y tipo de contenido son campos obligatorios, por lo que los completamos siempre
        self.wait.until(EC.visibility_of_element_located(self.input_cantidad_paquetes)).clear() # Limpiamos el campo de cantidad de paquetes antes de ingresar el valor
        self.wait.until(EC.visibility_of_element_located(self.input_cantidad_paquetes)).send_keys(cantidad_paquetes) # Ingresamos la cantidad de paquetes
        campo_contenido = self.wait.until(EC.visibility_of_element_located(self.input_tipo_de_contenido_paquete)) # Localizamos el campo de tipo de contenido del paquete
        campo_contenido.clear() # Limpiamos el campo de tipo de contenido del paquete
        campo_contenido.send_keys(tipo_contenido) # Ingresamos el tipo de contenido del paquete
    def completar_detalles_sobre(self, tipo_contenido):
        # Completar los detalles del sobre (documentación) como tipo de contenido
        self.wait.until(EC.element_to_be_clickable(self.btn_sobre)).click() # Seleccionamos el tipo de envío como sobre
        time.sleep(1) # Esperamos 1 segundo para que se procese la selección (puedes ajustar este tiempo según sea necesario)
        campo_contenido = self.wait.until(EC.visibility_of_element_located(self.input_tipo_de_contenido_sobre)) # Localizamos el campo de tipo de contenido del sobre
        campo_contenido.clear() # Limpiamos el campo de tipo de contenido del sobre
        campo_contenido.send_keys(tipo_contenido) # Ingresamos el tipo de contenido del sobre
    def completar_datos_destinatario(self, nombre, dni, codigo_pais, codigo_area, numero_telefono):
        # Completamos los datos del destinatario o persona que recibe el paquete
        self.wait.until(EC.visibility_of_element_located(self.input_quien_recibe_el_paquete)).send_keys(nombre) # Ingresamos el nombre de la persona que recibe el paquete
        self.wait.until(EC.visibility_of_element_located(self.input_dni_recibe_paquete)).send_keys(dni) # Ingresamos el DNI de la persona que recibe el paquete
        self.wait.until(EC.visibility_of_element_located(self.input_cpais_telefono)).send_keys(codigo_pais) # Ingresamos el código de país para el número de teléfono del destinatario
        self.wait.until(EC.visibility_of_element_located(self.input_carea_telefono)).send_keys(codigo_area) # Ingresamos el código de área para el número de teléfono del destinatario
        self.wait.until(EC.visibility_of_element_located(self.input_numero_telefono)).send_keys(numero_telefono) # Ingresamos el número de teléfono del destinatario