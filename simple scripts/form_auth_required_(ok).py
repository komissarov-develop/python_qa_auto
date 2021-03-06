﻿import time
from selenium import webdriver





try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
    input_last_name.send_keys("Petrov")

    input_email = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
    input_email.send_keys("1@mail.ru")

    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    

finally:
    time.sleep(10)

    browser.quit()