from selenium import webdriver
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
button1 = browser.find_element_by_link_text("224592")
button1.click()
input1 = browser.find_element_by_tag_name("div>input.form-control")
input1.send_keys("Dmitriy")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Testerovich")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Moscow")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button2 = browser.find_element_by_css_selector(".btn")
button2.click()