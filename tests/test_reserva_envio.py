import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from pages.reserva_envio_page import ReservaEnvioPage
from data.data_login import LOGIN_WEB_CLIENTES

USUARIO_VALIDO, PASSWORD_VALIDO, _ = LOGIN_WEB_CLIENTES[0]

@pytest.mark.parametrize("tipo_item, detalle_item, descripcion_caso", [
    ("paquete_unico", {
        "alto_cm": "30", "ancho_cm": "20", "largo_cm": "10", "peso_kg": "2", 
        "asegurar_envio": True, "valor_declarado": "180000", 
        "cantidad_paquetes": "1", "tipo_contenido": "Caja chica"},
        "CASO 1 : Reserva de envío (Paquete único)"
    ),
    ("paquete_y_sobre_documentacion", {
        "alto_cm": "30", "ancho_cm": "20", "largo_cm": "10", "peso_kg": "2", 
        "asegurar_envio": True, "valor_declarado": "180000", 
        "cantidad_paquetes": "1", "tipo_contenido": "Caja chica"}, 
        "CASO 2 : Reserva de envío (Paquete y Sobre con documentación)"
)
], ids=["CASO 1 : Reserva de envío (Paquete unico)", "CASO 2 : Reserva de envio (Paquete y Sobre con documentacion)"]) 
def test_reserva_envio(driver, record_property, tipo_item, detalle_item, descripcion_caso):
    # Agregamos la descripción del caso al reporte de pytest
    record_property("description", descripcion_caso)
    # 1. Login y navegación
    login_page = LoginPage(driver)
    menu = MenuComponent(driver)
    reserva_envio_page = ReservaEnvioPage(driver)
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO)
    menu.ir_a_nuevo_envio()
    WebDriverWait(driver, 10).until(EC.url_contains("shipping"))
    # 2. Selección de Origen y Destino
    reserva_envio_page.seleccionar_direccion_retiro("Defensa 814")
    time.sleep(3)
    reserva_envio_page.completar_piso_departamento("Piso 5 Depto Q")
    time.sleep(2)
    reserva_envio_page.hacer_click_detalle_envio()
    time.sleep(2)
    reserva_envio_page.hacer_click_agregar_envio()
    time.sleep(2)
    reserva_envio_page.seleccionar_destino("Av. Belgrano 553")
    time.sleep(3)
    reserva_envio_page.completar_piso_departamento("Piso 2 Depto A")
    time.sleep(2)
    # 3. Primer ítem: Paquete
    reserva_envio_page.completar_detalles_paquete(
        alto_cm=detalle_item["alto_cm"],
        ancho_cm=detalle_item["ancho_cm"],
        largo_cm=detalle_item["largo_cm"],
        peso_kg=detalle_item["peso_kg"],
        asegurar_envio=detalle_item["asegurar_envio"],
        valor_declarado=detalle_item["valor_declarado"],
        cantidad_paquetes=detalle_item["cantidad_paquetes"],
        tipo_contenido=detalle_item["tipo_contenido"]
    )
    reserva_envio_page.completar_datos_destinatario(
        nombre="Juan Perez",
        dni="12345678",
        codigo_pais="+54",
        codigo_area="11",
        numero_telefono="12345678"
    )
    reserva_envio_page.hacer_click_agregar_envio() # Guarda el primer paquete
    # 4. Segundo ítem (Solo si el test actual es 'paquete_y_sobre_documentacion')
    if tipo_item == "paquete_y_sobre_documentacion":
        reserva_envio_page.hacer_click_agregar_envio() # Clic para abrir el nuevo formulario de ítem
        time.sleep(1)
        reserva_envio_page.seleccionar_destino("Av. San Juan 1234")
        time.sleep(3)
        reserva_envio_page.hacer_click_sobre()         # Cambia a la pestaña/opción 'Sobre'
        time.sleep(2)
        reserva_envio_page.completar_detalles_sobre("Carta documento")
        time.sleep(1)
        reserva_envio_page.completar_datos_destinatario(
            nombre="Maria Lopez", 
            dni="87654321",
            codigo_pais="+54",
            codigo_area="11",
            numero_telefono="87654321"
        )
        time.sleep(2)
        reserva_envio_page.hacer_click_agregar_envio() # Guarda el segundo ítem (Sobre)

    # 5. Finalizar reserva y confirmación
    reserva_envio_page.hacer_click_continuar()
    time.sleep(2)
    reserva_envio_page.hacer_click_confirmar()
    time.sleep(2)
    
    driver.save_screenshot("screenshot_reserva_envio_exitosa.png")
    assert "shipping" in driver.current_url, f"Se esperaba que la URL contenga 'shipping' pero se obtuvo '{driver.current_url}'"
    
    try:
        codigo_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'bg-green-500')]"))
        )
        codigo_reserva = codigo_element.text.strip()
        record_property("status_code", codigo_reserva)
    except Exception:
        record_property("status_code", "ERROR")
        
    time.sleep(3)