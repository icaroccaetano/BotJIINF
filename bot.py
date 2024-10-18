from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def main():
    while True:
        driver = webdriver.Chrome()
        driver.implicitly_wait(60)
        driver.minimize_window()
        driver.get("https:/unificada.com")
        torcidometro =driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div[2]/div[2]")
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div[2]/div[2]")
        divfilha = torcidometro.find_element(By.XPATH, "//*[text()='Coisa Ruim']")
        div_acima = torcidometro.find_element(By.XPATH, "//*[text()='Coisa Ruim']/../..")
        driver.implicitly_wait(10)
        button = div_acima.find_element(By.XPATH, ".//button")  
        button.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        msg = driver.switch_to.alert.text
        agora = datetime.now()

        # Formata a data e o horário
        data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{data_formatada}  - {driver.switch_to.alert.text}")
        driver.switch_to.alert.accept()
        driver.close()

main()