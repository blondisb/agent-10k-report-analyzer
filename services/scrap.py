from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver de Chrome (asegúrate de tener chromedriver instalado)
driver = webdriver.Chrome()

try:
    # Abrir la página de búsqueda
    url = "https://www.sec.gov/edgar/search/#/q=mazda&filter_forms=10-K"
    driver.get(url)

    # Esperar a que se cargue la tabla
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Buscar el primer enlace de tipo "10-K" (en la columna "Form & File")
    first_10k_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '10-K')]"))
    )

    # Hacer clic en el enlace
    first_10k_link.click()

    # Esperar a que se cargue la nueva página (el documento .htm)
    time.sleep(3)  # Puedes usar WebDriverWait si conoces el selector exacto

    # Obtener el contenido HTML del documento
    html_content = driver.page_source

    # Guardar el contenido en un archivo
    with open("mazda_10-k.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Documento descargado correctamente.")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()