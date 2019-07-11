from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("div>input.form-control")
input1.send_keys("Dmitriy")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Testerovich")
input3 = browser.find_element_by_class_name("input.form-control.city")
input3.send_keys("Moscow")
input4 = browser.find_element_by_id("#country")
input4.send_keys("Russia")
button = find_element_by_css_selector(".btn")
button.click()
