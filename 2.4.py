from selenium import webdriver
import os
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Dimon")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Dimonich")
input3 = browser.find_element_by_name("email")
input3.send_keys("mail@mail.com")
element = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'xxx.txt')
element.send_keys(file_path)
button1 = browser.find_element_by_class_name("btn")
button1.click()
