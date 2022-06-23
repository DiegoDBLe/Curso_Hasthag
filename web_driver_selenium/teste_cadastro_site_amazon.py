from selenium import webdriver
from selenium.webdriver.common.by import By


caminho = r"C:\Users\thyci\anaconda3\chromedriver"
driver = webdriver.Chrome(caminho)

url = "https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=79547423725&hvpone=&hvptwo=&hvadid=591863875878&hvpos=&hvnetw=g&hvrand=2624926192053731661&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9101510&hvtargid=kwd-10573980&hydadcr=26346_11691057&gclid=Cj0KCQjwntCVBhDdARIsAMEwACkimrcPG5J0HT7UIEu9rupV_FgKE8h4w1wS_fMPDbjkBuEjWglJwHAaAqBvEALw_wcB"

driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID, 'createAccountSubmit').click()
driver.find_element(By.ID, 'ap_customer_name').send_keys('teste_automatizado')
driver.find_element(By.ID, 'ap_email').send_keys('teste_automatizado@teste')
driver.find_element(By.ID, 'ap_password').send_keys('123456')
driver.find_element(By.ID, 'ap_password_check').send_keys('123456')
driver.find_element(By.ID, 'continue').click()

