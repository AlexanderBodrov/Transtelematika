# import pytest_bdd
# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select



# Открыть браузер и развернуть на весь экран.
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window()


try:


    #
    # # Зайти на yandex.ru
    # link = "https://market.yandex.ru/catalog--smartfony"
    link = "https://yandex.ru/"
    browser.get(link)

    # В разделе «Маркет» выбрать «Смартфоны».
    browser.find_element(By.CLASS_NAME, "services-new__icon.services-new__icon_market").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.find_element(By.CSS_SELECTOR, "ul._381y5._21Njf > li:nth-child(9) > div").click()
    browser.find_element(By.CSS_SELECTOR, "body > div._111XI.main > div:nth-child(5) > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div:nth-child(1) > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > a > div > div").click()
    browser.find_element(By.CSS_SELECTOR, "div._8Pmms.a6Vij > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > a").click()
    # Перейти в «Все фильтры».
    filters = browser.find_element(By.PARTIAL_LINK_TEXT, "Все фильтры")
    browser.execute_script("return arguments[0].scrollIntoView(true);", filters)
    filters.click()
    # Задать параметр поиска до 20000 рублей и Диагональ экрана от 3 дюймов.
    price = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(1) div:nth-child(2) > input")
    price.send_keys("20000")
    browser.refresh()
    # Выбрать не менее 5 любых производителей.
    # time.sleep(10)

    producers = browser.find_element(By.CLASS_NAME, "_307sS._2k6P8")
    browser.execute_script("return arguments[0].scrollIntoView(true);", producers)
    # browser.find_element(By.CLASS_NAME, "_34OG2").click()
    # time.sleep(3)
    one = producers.find_elements(By.CLASS_NAME, "cyT3Q")
    print(len(one))
    # one.click()
    # two = browser.find_element(By.XPATH, '/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[8]/div/div/div/div[2]/div[2]/label/div')
    # two.click()
    # three = producers.find_element(By.ID, "470013")
    # three.click()
    # four = producers.find_element(By.ID, "15292504")
    # four.click()
    # five = producers.find_element(By.ID, "963630")
    # five.click()
    # six = producers.find_element(By.ID, "153061")
    # six.click()

    # # Нажать кнопку «Показать».
    # browser.find_element(By.CSS_SELECTOR, "body > div._111XI.main > section > div:nth-child(2) > div > div > div:nth-child(3) > div > div > a._2qvOO._3qN-v._1Rc6L").click()
    # # Посчитать кол-во смартфонов на одной странице.
    # phones = browser.find_elements(By.CSS_SELECTOR, "div.data-index")
    # phone = browser.find_element(By.CSS_SELECTOR, "div.data-index")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", more)
    # q = len(browser.find_elements(By.TAG_NAME, "h3"))

    # for i in range(5):
    #     for phone in phones:
    #         # phone = browser.find_element(By.TAG_NAME, "h3")
    #         phone.send_keys(Keys.PAGE_DOWN)
    #         # browser.
    #         # a = phone.find_element(By.CLASS_NAME, "page-cneevxtu00u > div > div > div > div > div:nth-child()") #page-cneevxtu00u > div > div > div > div > div:nth-child(9)
    #         b = phone.get_attribute("data-item-index")
    #         # a = a.__getattribute__("data-item-index")
    #         time.sleep(1)
    #         print(b)
    # # for

finally:
    # browser.quit()
    print("end")
# # Запомнить последний из списка.
# Изменить Сортировку на другую (по цене/ по рейтингу/ по
# скидке).
# Найти и нажать по имени запомненного объекта.
# Вывести рейтинг выбранного товара.
# Закрыть браузер.