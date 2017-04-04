from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://google.com")
window0 = driver.window_handles[0]

body = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
window1 = driver.window_handles[1]
time.sleep(2)

driver.switch_to.window(window0)
time.sleep(3)
driver.get('http://bing.com')

driver.switch_to.window(window1)
driver.get("http://www.facebook.com")
time.sleep(3)

driver.switch_to.window(window0)
driver.get("http://www.youtube.com")
time.sleep(2)

#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
#time.sleep(2)

driver.switch_to.window(window1)
time.sleep(3)

driver.switch_to.window(window0)
driver.find_element_by_tag_name('body').click()
driver.get("http://www.facebook.com")


driver.quit()

#RESULT: youtube on the first window