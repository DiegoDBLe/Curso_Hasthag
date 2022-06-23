from selenium import webdriver
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)