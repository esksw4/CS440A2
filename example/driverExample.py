from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
URL = "https://portal.caliperqaaws.com/users/sign_in"
driver.get("%s" % URL)
driver.find_element_by_id("user_email").clear()
driver.find_element_by_id("user_email").send_keys(1)
# type User Password
driver.find_element_by_id("user_password").clear()
driver.find_element_by_id("user_password").send_keys(2)
# click Enter
driver.find_element_by_id("login-btn").click()
time.sleep(3)
# time1.sleep(timeAfterLogin)
elem = driver.find_element_by_class_name('alert.alert-error')
print(elem)

driver.quit()