# Registration_login: регистрация аккаунта
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

email = ''
password = ''

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(2)>a').click()

driver.find_element(By.ID, 'reg_email').send_keys(email)
driver.find_element(By.ID, 'reg_password').send_keys(password)
driver.find_element(By.NAME, 'register').click()

driver.quit()

# Registration_login: логин в систему
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

email = ''
password = ''

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(2)>a').click()

driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.NAME, 'login').click()

assert driver.find_element(By.CSS_SELECTOR, '.woocommerce-MyAccount-navigation li:nth-child(6)>a')

driver.quit()
