from selenium import webdriver
import math
from math import log,sin
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)
button1 = browser.find_element_by_id("robotsRule")
button1.click()
button2 = browser.find_element_by_id("robotCheckbox")
button2.click()
box = browser.find_element_by_id("treasure")
x = box_value = box.get_attribute("valuex")
y = log(abs(12*sin(int(x))))
pole = browser.find_element_by_id("answer")
pole.send_keys(str(y))
button = browser.find_element_by_class_name("btn")
button.click()

