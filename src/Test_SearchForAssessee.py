from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# import Functions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1
from datetime import date
from datetime import time 
from datetime import datetime
from datetime import timedelta

class Test_SearchForAssessee(unittest.TestCase):
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

  def test_searchForAssessee(self):
    import Functions
    import automatedSmokeTest

    Functions.GUIdisplay.testName = "Search For Assessee"
    driver = Functions.Functions.hiringOPL(self)

    str1 = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[")
    str2 = str(1)
    str3 = str("]/td[2]/div/div")
    str_element = str1 + str2 + str3
    existAssesseeName = driver.find_element_by_xpath(str_element).text
    driver.find_element_by_xpath("//input[@id='hiring-status-mainSearch']").send_keys(existAssesseeName)
    time1.sleep(2)

    tableText = driver.find_element_by_id("hiring-status-table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    # print(systemAssessee)
    # print(listAssessee)
    check = None
    time1.sleep(1)
    for j in range(1, listAssessee+1):
      str2 = str(j)
      str_element = str1 + str2 + str3
      check = driver.find_element_by_xpath(str_element).text
      # print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
      # print("test_searchForAssessee check: ", check)
      # print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    if check != existAssesseeName:
      automatedSmokeTest.GUIFunctions.outputDisplayConsole("%s couldn't be found. Searching for assessee function is broken." %existAssesseeName, Functions.GUIdisplay.testName,'se')
    else:
      automatedSmokeTest.GUIFunctions.outputDisplayConsole("%s was found succesfully." %existAssesseeName, Functions.GUIdisplay.testName,'s')
        # checkNumError += 1

    # Functions.Functions.checkForError(checkNumError, testName)
if __name__ == "__main__":
    unittest.main(warnings ='ignore')