import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()

    

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_id('book')
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    num = browser.find_element_by_id('input_value')
    x = num.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    submit = browser.find_element_by_id('solve')
    submit.click()
    
    

finally:
    time.sleep(30)

    browser.quit()


#browser.implicitly_wait(5) - ждём 5 сек для всех элементов

#проверка не активности кнопки после в течении 5 сек
#button = WebDriverWait(browser, 5).until_not(
#        EC.element_to_be_clickable((By.ID, "verify"))
#    )



