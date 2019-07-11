from selenium import webdriver
import math
from math import log,sin
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button1 = browser.find_element_by_class_name("btn")
button1.click()
confirm = browser.switch_to.alert
confirm.accept()
x_e = browser.find_element_by_id("input_value")
x = x_e.text
y = log(abs(12*sin(int(x))))
pole = browser.find_element_by_id("answer")
pole.send_keys(str(y))
button = browser.find_element_by_class_name("btn")
button.click()

