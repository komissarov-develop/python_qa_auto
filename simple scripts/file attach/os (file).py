﻿import math
import time
import os
from selenium import webdriver





try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("vlad")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("nagiev")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("1@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file1 = browser.find_element_by_id('file')
    file1.send_keys(file_path)
    button = browser.find_element_by_tag_name('button')
    button.click()
    

finally:
    time.sleep(10)

    browser.quit()



    #current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    #element.send_keys(file_path)