import time
from selenium import webdriver
import unittest



	
class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		
	def test_search_reg1(self):
		browser = self.browser
		browser.get("http://suninjuly.github.io/registration1.html")	
		input1 = browser.find_element_by_class_name('first_block .first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_class_name('first_block .second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_class_name('first_block .third')
		input3.send_keys("123@mail.ru")
		input4 = browser.find_element_by_class_name('second_block .first')
		input4.send_keys("79897735722")
		input5 = browser.find_element_by_class_name("second_block .second")
		input5.send_keys("kemerovo 15")
		time.sleep(1)
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		
	def test_search_reg2(self):
		browser = self.browser
		browser.get("http://suninjuly.github.io/registration2.html")
		input1 = browser.find_element_by_class_name('first_block .first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_class_name('first_block .second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_class_name('first_block .third')
		input3.send_keys("123@mail.ru")
		input4 = browser.find_element_by_class_name('second_block .first')
		input4.send_keys("79897735722")
		input5 = browser.find_element_by_class_name("second_block .second")
		input5.send_keys("kemerovo 15")
		time.sleep(1)
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		

if __name__ == "__main__":
    unittest.main()
	
#FAILED (errors=1)
	
	
