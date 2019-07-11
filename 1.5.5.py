from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
browser.get("http://suninjuly.github.io/selects1.html")
a1 = browser.find_element_by_id("num1")  #поиск числа 1
b1 = browser.find_element_by_id("num2")  #поиск числа 2
a = int(a1)
b = int(b1)
summa = (a + b)
select = Select(browser.find_element_by_css_selector("custom-select"))
select.select_by_value("summa")
button = browser.find_element_by_css_selector(".btn")
button.click()

