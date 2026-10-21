import time 
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from pages.reserva_mensajeria import ReservaMensajeriaPage
from data.data_login import LOGIN_WEB_CLIENTES

USUARIO_VALIDO, PASSWORD_VALIDO, _ = LOGIN_WEB_CLIENTES[0]

def test_reserva_mensajeria(driver, record_property):
    """ CASO 1 : Reserva de mensajería"""
    # 1. Login y navegación
    login_page = LoginPage(driver)
    menu = MenuComponent(driver)
    reserva_mensajeria_page = ReservaMensajeriaPage(driver)
    login_page.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO)
    menu.ir_a_nueva_mensajeria()
    WebDriverWait(driver, 10).until(EC.url_contains("couriers"))
    reserva_mensajeria_page.hacer_click_indicaciones()
    reserva_mensajeria_page.hacer_click_agregar_indicacion()
    reserva_mensajeria_page.hacer_click_donde_vamos()
    reserva_mensajeria_page.seleccionar_origen("Defensa 814")
    reserva_mensajeria_page.completar_piso_departamento("Piso 5 Depto Q")
    reserva_mensajeria_page.completar_indicaciones("Retirar carta documento")
    reserva_mensajeria_page.completar_datos_contacto("Juan Perez", "54", "11", "62452754")
    reserva_mensajeria_page.hacer_click_agregar_envio_mensajeria()
    reserva_mensajeria_page.hacer_click_agregar_indicacion()
    reserva_mensajeria_page.hacer_click_donde_vamos()
    reserva_mensajeria_page.seleccionar_destino("Av. Belgrano 553")
    reserva_mensajeria_page.completar_piso_departamento("Piso 2 Depto A")
    reserva_mensajeria_page.completar_indicaciones("Entregar en recepción")
    reserva_mensajeria_page.completar_datos_contacto("Maria Lopez", "54", "11", "12345678")
    reserva_mensajeria_page.hacer_click_agregar_envio_mensajeria()
    reserva_mensajeria_page.hacer_click_continuar()
    reserva_mensajeria_page.hacer_click_confirmar()
