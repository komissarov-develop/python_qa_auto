import math
import time
from selenium import webdriver





try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    submit = browser.find_element_by_css_selector('button')
    submit.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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




#alert = browser.switch_to.alert
#alert.accept() //принять алерт

#alert = browser.switch_to.alert
#alert_text = alert.text  //текст из алерт

#confirm = browser.switch_to.alert
#confirm.accept()
#confirm.dismiss()

#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()