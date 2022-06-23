from selenium import webdriver
from selenium.webdriver.common.by import By

# Caminho do webdriver
caminho = r"C:\Users\thyci\anaconda3\chromedriver"
navegador = webdriver.Chrome(caminho)

navegador.get(r'https://www.hashtagtreinamentos.com/')

# Selecionando pela tag: Selecionando o titulo do site

titulo_h1 = navegador.find_element(By.TAG_NAME, 'h1').text
print(titulo_h1)
print('')

# Selecionando pelo Partial Link Text (ou Link_TEXT):
# Quero conseguir pegar o número de watsapp de contato.
# Partial Link Text (Ele pega atarves de uma parte escrita no link)
# Link_TEXT (Ele pega com o nome do link completo):

numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text
print(numero_whatsapp)
print('')
