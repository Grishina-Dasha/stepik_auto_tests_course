from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(x+y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = int(x_element.text)
    y_element = browser.find_element_by_id('num2')
    y = int(y_element.text)
    z = calc(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()