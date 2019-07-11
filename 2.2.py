from selenium import webdriver
import math
from math import log,sin
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True