from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button2 = browser.find_element_by_id('book')
    button2.click()
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()