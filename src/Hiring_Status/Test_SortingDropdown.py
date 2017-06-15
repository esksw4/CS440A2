from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import Functions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1
from datetime import date
from datetime import time 
from datetime import datetime
from datetime import timedelta

class Test_SortingDropdown(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.base_url = "http://portal.qa.calipercorp.com/users/sign_in"
    self.verificationErrors = []
    self.accept_next_alert = True

  def is_element_present(self, how, what):
    try:
      self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
      return False
    return True

  def is_alert_present(self):
    try:
      self.driver.switch_to_alert()
    except NoAlertPresentException as e:
      return False
    return True

  def close_alert_and_get_its_text(self):
    try:
      alert = self.driver.switch_to_alert()
      alert_text = alert.text
      if self.accept_next_alert:
        alert.accept()
      else:
        alert.dismiss()
      return alert_text
    finally:
      self.accept_next_alert = True

  def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

  def test_sortingDropdown(self):
    checkNumError = 0
    testName = "Sorting Dropdown"
    driver = Functions.Functions.hiringOPL(self, testName)

    whatToSort = 'Name'
    print('1. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    time1.sleep(5)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(2)
    checkNumError = Functions.Functions.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    whatToSort = 'Date'
    print('2. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_UP)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(2)
    checkNumError = Functions.Functions.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    whatToSort = 'Supervisor'
    print('3. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    time1.sleep(3)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(5)
    
    checkNumError = Functions.Functions.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')