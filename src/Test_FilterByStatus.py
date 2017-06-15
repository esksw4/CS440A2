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

class Test_FilterByStatus(unittest.TestCase):
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

  def test_FilterByHiringStatus(self):
    checkNumError = 0
    testName = "Filter by Status"
    driver = Functions.Functions.hiringOPL(self, testName)

    # filter by Pending
    buttonStatus = 'Pending'
    print('1. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    # filter by Hired
    buttonStatus = 'Hired'
    print('2. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee =Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    # filter by Hired
    buttonStatus = 'Not hired'
    print('3. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[3]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')