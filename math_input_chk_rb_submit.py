import math
import time
from selenium import webdriver



link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radioButton = browser.find_element_by_css_selector("[value='robots']")
    radioButton.click()
    submit = browser.find_element_by_css_selector('button')
    submit.click()

finally:
    time.sleep(30)

    browser.quit()

    