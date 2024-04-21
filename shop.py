# Shop: отображение страницы товара
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

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()
driver.find_element(By.CSS_SELECTOR, '.masonry-done>li:nth-child(3)>a').click()

if driver.find_element(By.CSS_SELECTOR, '.product_title').text == 'HTML5 Forms':
    print('YES, HTML5 Forms')
else:
    print('NO, HTML5 Forms')

driver.quit()

# Shop: количество товаров в категории
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()
driver.find_element(By.CSS_SELECTOR, '.product-categories>li:nth-child(2)>a').click()

if len(driver.find_elements(By.CSS_SELECTOR, '.products>li')) == 3:
    print('Three books displayed')
else:
    print('No three books displayed')

driver.quit()

# Shop: сортировка товаров
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()

if driver.find_element(By.XPATH, "//option[@value='menu_order']").get_attribute('selected'):
    print('Default sorting')
sort_select = Select(driver.find_element(By.CLASS_NAME, 'orderby'))
sort_select.select_by_value('price-desc')

sort_select = Select(driver.find_element(By.CLASS_NAME, 'orderby'))
if driver.find_element(By.XPATH, "//option[@value='price-desc']").get_attribute('selected'):
    print('Sort by price: high to low')

driver.quit()

# Shop: отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()

driver.find_element(By.CSS_SELECTOR, '.products>li:nth-child(1)>a').click()

assert driver.find_element(By.CSS_SELECTOR, '.price del .woocommerce-Price-amount').text == '₹600.00'
assert driver.find_element(By.CSS_SELECTOR, '.price ins .woocommerce-Price-amount').text == '₹450.00'

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located([By.CSS_SELECTOR, '.images a'])).click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located([By.CLASS_NAME, 'pp_close'])).click()

driver.quit()

# Shop: проверка цены в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

email = ''
password = ''

# My Account
driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(2)>a').click()

driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.NAME, 'login').click()

# Shop
driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()

# HTML5 WebApp Development
driver.find_element(By.CSS_SELECTOR, '.products>li:nth-child(4) a:nth-child(2)').click()

# Проверка корзины
WebDriverWait(driver, 10).until_not(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cartcontents'), '0 Items'))
assert driver.find_element(By.CSS_SELECTOR, '.cartcontents').text == '1 Item'
assert driver.find_element(By.CSS_SELECTOR, '.amount').text == '₹180.00'

# Переход в корзину
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount')))
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.order-total .woocommerce-Price-amount')))

driver.quit()

# Shop: работа в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

# Shop
driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()

# Скролим и добавляем книги
driver.execute_script("window.scrollBy(0,300);")
driver.find_element(By.CSS_SELECTOR, '.products>li:nth-child(4) a:nth-child(2)').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.products>li:nth-child(5) a:nth-child(2)').click()

# Переход в корзину
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

# Удаляем первый элемент
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.product-remove>.remove').click()

# Undo
driver.find_element(By.CSS_SELECTOR, '.woocommerce-message>a').click()

# Очистим и увеличим количество
driver.find_element(By.CSS_SELECTOR, '.shop_table .cart_item:nth-child(1) input').clear()
driver.find_element(By.CSS_SELECTOR, '.shop_table .cart_item:nth-child(1) input').send_keys(3)

# Обновим корзину
driver.find_element(By.CSS_SELECTOR, '.actions>.button').click()

# Проверка количества
assert driver.find_element(By.CSS_SELECTOR, '.shop_table .cart_item:nth-child(1) input').get_attribute('value') == '3'

# Применить купон
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.coupon>.button').click()

assert driver.find_element(By.CSS_SELECTOR, '.woocommerce-error>li').text == 'Please enter a coupon code.'

driver.quit()

# Shop: покупка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

# Shop
driver.find_element(By.CSS_SELECTOR, '#main-nav>li:nth-child(1)>a').click()

# Скролим и добавляем книгу
driver.execute_script("window.scrollBy(0,300);")
driver.find_element(By.CSS_SELECTOR, '.products>li:nth-child(4) a:nth-child(2)').click()
time.sleep(5)

# Переход в корзину
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

# Проверяем и нажимаем PROCEED TO CHECKOUT
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a')))
driver.find_element(By.CSS_SELECTOR, '.wc-proceed-to-checkout>a').click()

# Провеяем наличие поля
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#billing_first_name_field>.input-text')))

# Заполняем обязательные поля
driver.find_element(By.CSS_SELECTOR, '#billing_first_name_field>.input-text').send_keys('Marcus')
driver.find_element(By.CSS_SELECTOR, '#billing_last_name_field>.input-text').send_keys('Fenix')
driver.find_element(By.CSS_SELECTOR, '#billing_email_field>.input-text').send_keys('MarcusFenix@gears.com')
driver.find_element(By.CSS_SELECTOR, '#billing_phone_field>.input-text').send_keys('+180621232820')

# Выбираем страну
driver.find_element(By.CSS_SELECTOR, '.select2-container').click()
driver.find_element(By.CSS_SELECTOR, '#s2id_autogen1_search').send_keys('Russia')
driver.find_element(By.CSS_SELECTOR, '#select2-result-label-394>.select2-match').click()

driver.find_element(By.CSS_SELECTOR, '#billing_address_1_field>.input-text').send_keys('улица Пушкина, дом Колотушкина')

driver.find_element(By.CSS_SELECTOR, '#billing_city_field>.input-text').send_keys('New York')
driver.find_element(By.CSS_SELECTOR, '#billing_state_field>.input-text').send_keys('Russia')
driver.find_element(By.CSS_SELECTOR, '#billing_postcode_field>.input-text').send_keys('6300000')

# Выбираем способ оплаты
driver.execute_script("window.scrollBy(0,900);")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '#payment_method_cheque').click()
driver.find_element(By.ID, 'place_order').click()

# Проверяем
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element([By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'],
                                     'Thank you. Your order has been received.'))
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element([By.CSS_SELECTOR, '.shop_table.order_details tr:nth-child(3)>td'],
                                     'Check Payments'))
time.sleep(5)

driver.quit()
