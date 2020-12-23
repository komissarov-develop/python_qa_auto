import math
import time
from selenium import webdriver





try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    submit = browser.find_element_by_css_selector('button')
    submit.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    num = browser.find_element_by_id('input_value')
    x = num.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    submit = browser.find_element_by_css_selector('button')
    submit.click()
    

finally:
    time.sleep(10)

    browser.quit()




#browser.switch_to.window(window_name) - переход на новое окно
#new_window = browser.window_handles[1]  - вы даёт имя второй вкладки
#first_window = browser.window_handles[0] - имя текущей владки

