from selenium import webdriver
from selenium.webdriver.common.by import By

# Caminho do webdriver
caminho = r"C:\Users\thyci\anaconda3\chromedriver"
navegador = webdriver.Chrome(caminho)

navegador.get(r'https://www.hashtagtreinamentos.com/')

# Selecionando vários elementos de uma vez:
# Vamos selecionar pelo find_elements
# vamos clicar no item Blog do menu
# O método find_elements devolve uma lista de elementos, ele tem que ser do mesmo 'nome'.

lista_elementos = navegador.find_elements(By.CLASS_NAME, 'nav-link')
for elemento in lista_elementos:
    if 'blog' in elemento.text.lower():
        elemento.click()
        break
