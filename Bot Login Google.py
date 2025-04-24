from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CAMINHO PARA O SEU CHROMEDRIVER
CHROMEDRIVER_PATH = "chromedriver.exe"  # ou "./chromedriver" no Linux/Mac

# SEUS DADOS DE LOGIN (use com cautela)
EMAIL = "seuemail@gmail.com"
SENHA = "suasenha"

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH))
driver.maximize_window()

# Abre a página de login
driver.get("https://accounts.google.com/")

try:
    # Espera o campo de email aparecer
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(EMAIL)
    driver.find_element(By.ID, "identifierNext").click()

    # Espera o campo de senha aparecer
    senha_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    time.sleep(1)  # Pequeno delay para estabilidade
    senha_input.send_keys(SENHA)
    driver.find_element(By.ID, "passwordNext").click()

    print("Login feito (ou tentativa realizada).")

except Exception as e:
    print("Erro durante o login:", e)

# Aguarda alguns segundos para você visualizar o resultado
time.sleep(5)

# Encerra o navegador
driver.quit()