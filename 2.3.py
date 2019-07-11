from selenium import webdriver
import math
from math import log,sin
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x_e = browser.find_element_by_id("input_value")
x = x_e.text
y = log(abs(12*sin(int(x))))
browser.execute_script("window.scrollBy(0, 150);")
input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))
button1 = browser.find_element_by_class_name("form-check-label")
button1.click()
button2 = browser.find_element_by_id("robotsRule")
button2.click()
button3 = browser.find_element_by_class_name("btn")
button3.click()
