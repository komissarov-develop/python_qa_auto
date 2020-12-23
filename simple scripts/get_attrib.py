import math
import time
from selenium import webdriver



link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
     
    treasure = browser.find_element_by_id('treasure')
    treasure_open = treasure.get_attribute("valuex")
    x = treasure_open
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radioButton = browser.find_element_by_css_selector("[value='robots']")
    radioButton.click()
    submit = browser.find_element_by_css_selector('button')
    submit.click()

finally:
    time.sleep(30)

    browser.quit()

    