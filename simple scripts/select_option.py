import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver





link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link) 
    num1 = browser.find_element_by_id('num1')
    x = num1.text
    num2 = browser.find_element_by_id('num2')
    y = num2.text
    sum_el = int(x) + int(y)
    sum_el = str(int(x)+int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_el)
    submit = browser.find_element_by_css_selector('button')
    submit.click()

finally:
    time.sleep(5)

    browser.quit()

    