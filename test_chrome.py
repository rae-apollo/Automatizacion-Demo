from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.google.com")

    print(f"\nEl titulo de la pagina es: {driver.title} ")
    assert "Google" in driver.title

    time.sleep(2)
    driver.quit()