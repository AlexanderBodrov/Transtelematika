from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открыть браузер и развернуть на весь экран.

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window()

try:
    # Зайти на yandex.ru
    link = "https://yandex.ru/"
    browser.get(link)

    # В разделе «Маркет» выбрать «Смартфоны».
    browser.find_element(By.CLASS_NAME, "services-new__icon.services-new__icon_market").click()
    latest_window = browser.window_handles[-1]
    browser.close()
    browser.switch_to.window(latest_window)
    browser.find_element(By.ID, "catalogPopupButton").click()
    browser.find_element(By.CSS_SELECTOR, "#catalogPopup > div > div > div > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > a > span").click()
    browser.find_element(By.CSS_SELECTOR, "div._111XI.main > div:nth-child(5) > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div:nth-child(1) > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > a").click()
    browser.find_element(By.CSS_SELECTOR, "div._8Pmms.a6Vij > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > a").click()
    # Перейти в «Все фильтры».
    browser.find_element(By.CSS_SELECTOR, "div.kQnUO._2jRxX._1LZd1 > div > div:nth-child(5) > div > div > div > a").click()
    # Задать параметр поиска до 20000 рублей
    price = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(1) > div > div > div > div:nth-child(2) > input")
    price.send_keys("20000")
    # Задать Диагональ экрана от 3 дюймов.
    screen_size_button = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(12) > div > button")
    browser.execute_script("arguments[0].scrollIntoView();", screen_size_button)
    if "Диагональ экрана (точно)" in screen_size_button.text:
        screen_size_button.click()
        screen_size = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(12) > div > div > div > div:nth-child(1) > input")
        screen_size.send_keys("3")
    else:
        browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(11) > div > button").click()
        screen_size = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(11) > div > div > div > div:nth-child(1) > input")
        screen_size.send_keys("3")
    # Выбрать не менее 5 любых производителей.
    producers = browser.find_element(By.CSS_SELECTOR, "div._3aaVQ > div:nth-child(1) > div:nth-child(8) > div > button")
    browser.execute_script("arguments[0].scrollIntoView();", producers)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(2) > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(4) > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(5) > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(6) > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(8) > label").click()
    browser.find_element(By.CSS_SELECTOR, "div._307sS._2k6P8 > div > div:nth-child(2) > div:nth-child(9) > label").click()
    # Нажать кнопку «Показать».
    browser.find_element(By.CSS_SELECTOR, "a._2qvOO._3qN-v._1Rc6L").click()
    # Посчитать кол-во смартфонов на одной странице.
    end = browser.find_element(By.CLASS_NAME, "_2UK6L")
    browser.execute_script("arguments[0].scrollIntoView(false);", end)
    phones = browser.find_elements(By.CSS_SELECTOR, "h3._2UHry._2vVOc > a")
    number_of_phones = len(phones)
    print("number_of_phones", number_of_phones)
    # Запомнить последний из списка.
    phone = phones[-1].text
    print("last phone", phone)
    # Изменить Сортировку на другую (по цене/ по рейтингу/ по скидке).
    sort_by_price_button = browser.find_element(By.CLASS_NAME, "_23p69._3D8AA")
    browser.execute_script("arguments[0].scrollIntoView(true);", sort_by_price_button)
    sort_by_price_button.click()
    # Найти и нажать по имени запомненного объекта.
    browser.refresh()
    to_end = browser.find_element(By.CSS_SELECTOR, "h3._2UHry._2vVOc > a")
    to_end.send_keys(Keys.END)
    browser.find_element(By.LINK_TEXT, phone).click()
    latest_window = browser.window_handles[-1]
    browser.close()
    browser.switch_to.window(latest_window)
    rating = browser.find_element(By.CSS_SELECTOR, "div._1EOgH._2I6wc._1NfPD > span._2v4E8").text
    print("smartphone_rating_is", rating)

# Закрыть браузер.
finally:
    print("end")
    browser.quit()
