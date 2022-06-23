from selenium import webdriver
from selenium.webdriver.common.by import By


caminho = r"C:\Users\thyci\anaconda3\chromedriver"
driver = webdriver.Chrome(caminho)

url = "https://www.americanas.com.br/?epar=bp_br_00_go_sch_brand_americanas_202002&utm_medium=buscappc&utm_source=google&utm_campaign=marca:acom%3bmidia:buscappc%3bformato:branding%3bsubformato:00%3bidcampanha:sch_brand_americanas_202002&opn=YZMEZP&WT.srch=1&gclid=Cj0KCQjwntCVBhDdARIsAMEwACnl_w3KtxHDvVTfVgPAMO9q6iwa7DHh6Ha22GirvIff_dzSbzUxYoAaAlzbEALw_wcB/"

driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div[4]/div/div/div/a').click()
driver.find_element(By.ID, 'email-input').send_keys('deigo_batista@hotmail.com')
driver.find_element(By.ID, 'password-input').send_keys('Levi0605@')
driver.find_element(By.ID, 'login-button').click()
