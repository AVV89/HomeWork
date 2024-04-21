# Home: добавление комментария

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,300);")

driver.find_element(By.CSS_SELECTOR, ".themify_builder_sub_row.sub_row_1-0-2>.sub_column:nth-child(1) a").click()
driver.find_element(By.CSS_SELECTOR, ".reviews_tab>a").click()

driver.find_element(By.CSS_SELECTOR, 'a.star-5').click()
driver.find_element(By.ID, "comment").send_keys("Nice book!")
driver.find_element(By.ID, "author").send_keys("Marcus Fenix")
driver.find_element(By.ID, "email").send_keys("MarcusFenix@gears.com")
driver.find_element(By.ID, "submit").click()

driver.quit()
