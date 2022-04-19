from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    browser.execute_script("input = document.getElementsByTagName('input')[0];input.scrollIntoView(true);")
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()

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