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
    import Functions
    import automatedSmokeTest
    # checkNumError = 0
    Functions.GUIdisplay.testName = "Filter by Status"
    driver = Functions.Functions.hiringOPL(self)

    # filter by Pending
    buttonStatus = 'Pending'
    automatedSmokeTest.GUIFunctions.outputDisplayConsole("1. Filter by %s" %buttonStatus, Functions.GUIdisplay.testName,'display')
    driver.find_element_by_xpath("//div[@id='statusTypes']/div[1]/label[1]").click()
    time1.sleep(4)

    checkEmpty = Test_FilterByStatus.is_element_present(self, By.XPATH, "//td[@class='dataTables_empty']")
    if checkEmpty == True:
      automatedSmokeTest.GUIFunctions.outputDisplayConsole("There are no %S assessees." %(buttonStatus), Functions.GUIdisplay.testName,'display')
    else:
      tableText = driver.find_element_by_id("hiring-status-table_info").text
      systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
      filterWorks = Functions.Functions.checkStatusList(driver, listAssessee, buttonStatus)
      if filterWorks == 0: 
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("The list is not filtered by %s status." %(buttonStatus), Functions.GUIdisplay.testName,'se')
      else:
        # filter by Hired
        buttonStatus = 'Hired'
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("2. Filter by %s" %buttonStatus, Functions.GUIdisplay.testName,'display')
        driver.find_element_by_xpath("//div[@id='statusTypes']/div[1]/label[1]").click()
        driver.find_element_by_xpath("//div[@id='statusTypes']/div[2]/label[1]").click()
        time1.sleep(4)

        checkEmpty = Test_FilterByStatus.is_element_present(self, By.XPATH, "//td[@class='dataTables_empty']")
        if checkEmpty == True:
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("There are no %S assessees." %(buttonStatus), Functions.GUIdisplay.testName,'display')
        else:
          tableText = driver.find_element_by_id("hiring-status-table_info").text
          systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
          filterWorks = Functions.Functions.checkStatusList(driver, listAssessee, buttonStatus)
          if filterWorks == 0: 
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("The list is not filtered by %s status." %(buttonStatus), Functions.GUIdisplay.testName,'se')
          else:
            # filter by Hired
            buttonStatus = 'Not hired'
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("3. Filter by %s" %buttonStatus, Functions.GUIdisplay.testName,'display')
            driver.find_element_by_xpath("//div[@id='statusTypes']/div[2]/label[1]").click()
            driver.find_element_by_xpath("//div[@id='statusTypes']/div[3]/label[1]").click()
            time1.sleep(4)

            checkEmpty = Test_FilterByStatus.is_element_present(self, By.XPATH, "//td[@class='dataTables_empty']")
            if checkEmpty == True:
              automatedSmokeTest.GUIFunctions.outputDisplayConsole("There are no %S assessees." %(buttonStatus), Functions.GUIdisplay.testName,'display')
            else:
              tableText = driver.find_element_by_id("hiring-status-table_info").text
              systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
              filterWorks = Functions.Functions.checkStatusList(driver, listAssessee, buttonStatus)
              if filterWorks == 0: 
                automatedSmokeTest.GUIFunctions.outputDisplayConsole("The list is not filtered by %s status." %(buttonStatus), Functions.GUIdisplay.testName,'se')
              else:
                automatedSmokeTest.GUIFunctions.outputDisplayConsole("The list is correctly filtered according to the status.", Functions.GUIdisplay.testName,'s')


if __name__ == "__main__":
    unittest.main(warnings ='ignore')