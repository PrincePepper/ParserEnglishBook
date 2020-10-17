# Сайт от куда скачивалась книга уже стал усторевать и он постепенно переежает на новый адрес
# из-за этого есть лишние действия в коде
# Семен Середа, 2020

import time
from bs4 import BeautifulSoup
from selenium import webdriver

# ссылка нашего учебника на сайте biblio-online
BASE_URL = 'https://www.biblio-online.ru/viewer/angliyskiy-yazyk-dlya-estestvennonauchnyh-napravleniy-450653#page/1'

driver = webdriver.Chrome()  # запуск веб драйвера под гугл хром

driver.get('https://www.biblio-online.ru/login')  # переход на страницу авторизации
time.sleep(5)  # время для прогрузки страницы
driver.find_element_by_id('go-to-urait').click()  # закрытие диалогового окна, о том что сайт переехал :)
email = driver.find_element_by_id('login')  # нахождение html элемента по id - login
email.send_keys('your@email.ru')  # вставка почты
time.sleep(0.5)
passwd = driver.find_element_by_name('password')  # нахождение html элемента по id - password
passwd.send_keys('yourpassword')  # вставка пароля
time.sleep(0.5)
next = driver.find_element_by_id('button1id').click()  # авторизация
time.sleep(5)  # время для прогрузки страницы
driver.get(BASE_URL)  # переход на страницу нашего учебника
SCROLL_PAUSE_TIME = 1  # задержка между сколлами страницы

last_height = driver.execute_script("return document.body.scrollHeight")
scheight = 1145  # шаг сколла(у вас может отличаться)
count = 0  # номер нашей страницы
while True:
    time.sleep(SCROLL_PAUSE_TIME)  # ждем прогрузки/прокрутки страницы
    driver.execute_script("window.scrollTo(0, window.scrollY + %s);" % scheight)  # наш сколл
    new_height = driver.execute_script("return window.scrollY")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    url_svg = "https://www.biblio-online.ru/viewer/getPage/21BDEACF-1230-4460-A3C6-E2FBDAEB91AE/" + str(count)
    driver.get(url_svg)

    count += 1
    if new_height == last_height:
        break
    last_height = new_height