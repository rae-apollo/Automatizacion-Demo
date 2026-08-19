# 🚗 Automatización de Reservas - Grupo Traslada

Proyecto de automatización de pruebas end-to-end (E2E) para la plataforma de reservas de Traslada, desarrollado con **Python** y **Selenium WebDriver**.

## 🏗️ Arquitectura
Se utilizó el patrón de diseño **Page Object Model (POM)** para separar la lógica de los elementos de la interfaz de los scripts de prueba, facilitando el mantenimiento y la escalabilidad.

## 📋 Flujo Automatizado
1. **Login:** Acceso seguro con credenciales de usuario.
2. **Origen/Destino:** Selección inteligente de direcciones usando sugerencias dinámicas.
3. **Cálculo Asincrónico:** Manejo de esperas dinámicas para la obtención de tarifas (loading states).
4. **Confirmación:** Validación y cierre del proceso de reserva.

## 🛠️ Herramientas utilizadas
* **Lenguaje:** Python 3.14
* **Framework:** Selenium WebDriver
* **Estrategia de Esperas:** Explicit Waits y JavaScript Executor para componentes de Angular Material.