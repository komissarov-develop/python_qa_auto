import math
import time
from selenium import webdriver





try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    num = browser.find_element_by_id('input_value')
    x = num.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radioButton = browser.find_element_by_css_selector("[value='robots']")
    radioButton.click()
    submit = browser.find_element_by_css_selector('button')
    submit.click()

finally:
    time.sleep(10)

    browser.quit()



    #browser.execute_script("document.title='Script executing';alert('Robots at work');") //alert обычный
    #browser.execute_script("window.scrollBy(0, 100);") //скролл на 100 пикселей вниз
    #scroll+click
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()