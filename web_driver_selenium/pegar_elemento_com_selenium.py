from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


caminho = r"C:\Users\thyci\anaconda3\chromedriver"
driver = webdriver.Chrome(caminho)

url = "https://www.hashtagtreinamentos.com/"

driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'firstname').send_keys('Diego')
driver.find_element(By.ID, 'email').send_keys('deigo_batista@hotmail.com')
driver.find_element(By.CLASS_NAME, 'botao-formulario').click()
