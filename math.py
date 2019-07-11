from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
x_e = browser.find_element_by_id("num1")  #поиск числа 1
y_e = browser.find_element_by_id("num2")  #поиск числа 2
x = x_e.text
y = y_e.text